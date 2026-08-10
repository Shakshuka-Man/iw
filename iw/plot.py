import copy
import warnings
from dataclasses import dataclass, field
from . import iw, tools

# Cap on the states one reachability search may visit. A search runs over the product of the stages of
# a plotline and everything it transitively `requires`, so it is exponential in the size of that
# cluster in the worst case. Past the cap we give up on the cluster and say so, rather than grinding.
_MAX_SEARCH_STATES = 200_000


class PlotReachabilityWarning(UserWarning):
    """A plot stage some character can never reach. Not necessarily a bug -- a character-gated branch
    is unreachable to everyone else by design -- so this warns rather than raises."""


class PlotContentWarning(UserWarning):
    """An instruction block or tracked item whose value may not be what the author intended: two
    plotlines fighting over it, or a stage that leaves a stale value in place. Both can be deliberate,
    so these warn rather than raise."""


@dataclass
class PlotStageDetails:
    """One layer of a plot stage's content, re-applied every turn the stage is active: the text of each
    instruction block, the value of each tracked item, and any extra effects. `characters` scopes the
    layer -- empty means everyone (see PlotStage)."""
    characters: iw.PossibleCharacter | list[iw.PossibleCharacter] = field(default_factory=list)
    instruction_blocks: dict[iw.InstructionBlock, str] = field(default_factory=dict)
    tracked_items: dict[iw.TrackedItem, str] = field(default_factory=dict)
    additional_effects: list[iw.TriggerEffect] = field(default_factory=list)

@dataclass
class PlotStage:
    """A state the plot can be in. Its content comes in layers: `plot_details` is what everyone sees
    while the plot is here (so it must not name characters), and each entry in
    `character_specific_plot_details` names the characters it applies to and is applied *after*
    `plot_details` -- so it can override the same instruction block or tracked item for those
    characters. A character may appear in at most one of these entries.

    A stage does not declare that it is the first one. By default the plotline starts at whichever stage
    nothing transitions into, and exactly one stage must fit that description -- name a `starting_stage`
    on the `Plotline` when that is not true of your plot. Both fields may be assigned after
    construction, which is what lets you declare a stage, wire the transition that reaches it, and only
    then write the content you arrive at -- the order the plot actually reads in.

    `description` is for you, not for the engine: it is never emitted, and nothing reads it but the
    warnings and errors below. A complaint about "stage '3'" tells you nothing when you have thirty of
    them; one about "stage '3' (the secret passage)" tells you where to look."""
    plot_details: PlotStageDetails | None = None
    character_specific_plot_details: list[PlotStageDetails] = field(default_factory=list)
    internal_id: str | None = None
    description: str | None = None

@dataclass
class PlotTransition:
    starting_stage: PlotStage | list[PlotStage]
    ending_stage: PlotStage
    transition_event: str = None
    trigger_on_scenario: str = None
    show_message: str | None = None
    end_game: bool = False
    can_continue: bool | None = None
    # Cross-plotline "synergy" gates: PlotStages belonging to *other* plotlines. Stages from the same
    # plotline are OR'd (any one qualifies); different plotlines are AND'd (each must hold). You must
    # list every qualifying stage explicitly -- e.g. for "Fire adept or beyond" you pass the adept,
    # expert AND master stages. We deliberately do NOT provide a "this stage and everything after it"
    # shorthand: that would only be meaningful for strictly linear plotlines, and plotlines are not
    # assumed to be linear (a stage can branch), so there is no well-defined "after".
    requires: list[PlotStage] = field(default_factory=list)
    # Set once, on the turn the transition fires -- unlike a PlotStage's tracked_items, which are
    # re-applied every turn the stage is active.
    tracked_items: dict[iw.TrackedItem, str] = field(default_factory=dict)
    additional_conditions: list[iw.TriggerCondition] = field(default_factory=list)
    additional_effects: list[iw.TriggerEffect] = field(default_factory=list)
    characters: iw.PossibleCharacter | list[iw.PossibleCharacter] = field(default_factory=list)
    internal_id: str | None = None

@dataclass
class Plotline:
    """A named plot: stages + transitions that advance independently of other plotlines, with its own
    stage tracker, per-turn gate, and situation-slot pool (all namespaced by `name`). The trackers are
    resolved during the build (on an internal copy -- your object is left untouched); pass your own to
    control them, or leave them None to auto-create `<name> Stage` / `<name> Change`."""
    name: str
    plot_stages: list[PlotStage]
    plot_transitions: list[PlotTransition]
    plot_stage_tracker: iw.TrackedItem | None = None
    plot_change_tracker: iw.TrackedItem | None = None
    # Where the plot begins. Left None, it is deduced: the one stage nothing transitions into. Name it
    # when the transitions cannot say -- a plot that loops back to its opening has no such stage, and a
    # plot you want to begin partway through has more than one.
    starting_stage: PlotStage | None = None


def _as_list(value):
    """Coerce a single value or a list into a list (used for the single-or-list parameters, so the
    rest of the code -- and the type checker -- can treat them uniformly)."""
    return value if isinstance(value, list) else [value]


def _names_character(character, field) -> bool:
    """Does a `characters` field (of a transition or a details layer) name this character?

    Compare by characterId, never by object identity. The handler deep-copies the plotlines it is given,
    which clones the PossibleCharacters the stages and transitions point at -- so they are no longer the
    same objects as the ones in `world.possibleCharacters`. PossibleCharacter is `eq=False`, so `in`
    would be an identity test, and would silently never match."""
    if character is None:
        return False
    return character.characterId in {c.characterId for c in _as_list(field)}


def _stage_label(stage: PlotStage) -> str:
    """How a stage is named in a warning or an error. The internal id is what the emitted JSON uses, so
    it always appears; the description, if the author gave one, is what makes the message mean anything
    to them."""
    if stage.description:
        return f"{stage.internal_id!r} ({stage.description})"
    return repr(stage.internal_id)


class PlotlineHandler:
    """Builds the tracked items and trigger events that implement one or more plotlines on top of the
    raw `iw` trigger machinery. Construct with a world and a list of Plotlines, then call `run()` to
    get a new World with everything added. Neither the input world nor the given plotlines are
    modified -- both are deep-copied first.

    With `shared_gate=False` (default) each plotline gets its own per-turn change gate, so plotlines
    advance independently and several may advance in the same turn. With `shared_gate=True` a single
    gate is shared, allowing at most one advance across all plotlines per turn."""

    def __init__(self, world: iw.World, plotlines: list[Plotline], shared_gate: bool = False):
        self.world = world
        # Work on deep copies so the caller's plotlines/stages/transitions are never mutated (ids and
        # trackers get resolved onto these copies, not the originals). Copying the whole list in one
        # call preserves cross-plotline `requires` references -- a stage referenced in `requires` and
        # the same stage inside its plotline copy to the one object.
        self.plotlines = copy.deepcopy(plotlines)
        self.shared_gate = shared_gate

        # Every stage and transition must belong to exactly one plotline (this also catches a stage or
        # transition accidentally listed twice). Reusing one across plotlines would corrupt id
        # assignment and ownership, so we reject it outright.
        seen = set()
        for plotline in self.plotlines:
            for item in [*plotline.plot_stages, *plotline.plot_transitions]:
                if id(item) in seen:
                    raise ValueError("A plot stage or transition appears in more than one plotline.")
                seen.add(id(item))

        self.shared_change_tracker = None
        if shared_gate:
            self.shared_change_tracker = iw.TrackedItem(
                name="Plot Change",
                dataType=iw.TrackedItemDataType.NUMBER,
                visibility=iw.TrackedItemVisibility.HIDDEN,
                initialValue="1",
            )

        # Per-plotline derived state, keyed by id(plotline). The trackers themselves are resolved in
        # place on each Plotline (see _setup_plotline); these dicts hold the rest.
        self._slots: dict[int, list[iw.TrackedItem]] = {}          # situation-slot pool
        self._situations: dict[int, dict[int, list[str]]] = {}     # id(stage) -> ordered situations
        self._initial: dict[int, PlotStage] = {}                   # id(plotline) -> its initial stage
        self.stage_owner: dict[int, Plotline] = {}                 # id(stage) -> owning plotline

        # Phase 1: set every plotline up before any triggers are built, so cross-plotline `requires`
        # references can be resolved in phase 3 (run()).
        for plotline in self.plotlines:
            self._setup_plotline(plotline)
            for stage in plotline.plot_stages:
                self.stage_owner[id(stage)] = plotline

        # Phase 2: with every stage's owner known, check each plotline's transitions are well-formed and
        # work out where it starts (which the transitions define), then search the whole plot for content
        # nobody can ever reach. Reachability is cross-plotline (a `requires` gate reads other plotlines'
        # stages), so it runs over all of them at once.
        for plotline in self.plotlines:
            self._validate_transitions(plotline)
            initial = self._find_initial_stage(plotline)
            self._initial[id(plotline)] = initial
            # The tracker starts at the opening stage, rather than at a sentinel the start-of-game
            # trigger then replaces. Written here rather than where the tracker is made because which
            # stage is the opening one is not known until the transitions have been read -- and written
            # even to a tracker you supplied, since a plot whose tracker starts elsewhere is at a stage
            # it never entered.
            plotline.plot_stage_tracker.initialValue = str(initial.internal_id)

        # Content warnings first, so they are still emitted if reachability then finds a hard error.
        self._warn_contested_targets()
        for plotline in self.plotlines:
            self._warn_stale_content(plotline)
        self._validate_reachability()

    def _setup_plotline(self, plotline: Plotline):
        stages = plotline.plot_stages
        transitions = plotline.plot_transitions

        # Every referenced character must exist in the world's possibleCharacters.
        world_character_ids = {character.characterId for character in self.world.possibleCharacters}
        referenced = [
            *(character
              for stage in stages
              for details in self._stage_layers(stage)
              for character in _as_list(details.characters)),
            *(character for transition in transitions for character in _as_list(transition.characters)),
        ]
        for character in referenced:
            if character.characterId not in world_character_ids:
                raise ValueError(
                    f"Character {character.name!r} (plotline {plotline.name!r}) is not in the "
                    "world's possibleCharacters."
                )

        # A stage's everyone-layer applies to everyone, so it must not name characters; and a character
        # may be named by at most one of the stage's character-specific layers (two layers covering the
        # same character at the same stage would race to set the same blocks and items).
        for stage in stages:
            if stage.plot_details is not None and _as_list(stage.plot_details.characters):
                raise ValueError(
                    f"A stage's plot_details applies to everyone and must not name characters "
                    f"(plotline {plotline.name!r}); use character_specific_plot_details instead."
                )
            covered: dict[str, iw.PossibleCharacter] = {}
            for details in stage.character_specific_plot_details:
                characters = _as_list(details.characters)
                if not characters:
                    raise ValueError(
                        f"Every character_specific_plot_details entry must name at least one character "
                        f"(plotline {plotline.name!r}); use plot_details for content that applies to "
                        "everyone."
                    )
                for character in characters:
                    if character.characterId in covered:
                        raise ValueError(
                            f"Character {character.name!r} appears in more than one "
                            f"character_specific_plot_details entry on the same stage "
                            f"(plotline {plotline.name!r})."
                        )
                    covered[character.characterId] = character

        # `can_continue` is only meaningful on an end-game transition, where it is required.
        for transition in transitions:
            if transition.end_game and transition.can_continue is None:
                raise ValueError(
                    f"An end_game transition must set can_continue (plotline {plotline.name!r})."
                )
            if not transition.end_game and transition.can_continue is not None:
                raise ValueError(
                    f"can_continue may only be set on an end_game transition (plotline {plotline.name!r})."
                )

        # Resolve the trackers in place, namespaced by the plotline name.
        if plotline.plot_stage_tracker is None:
            plotline.plot_stage_tracker = iw.TrackedItem(
                name=f"{plotline.name} Stage",
                dataType=iw.TrackedItemDataType.NUMBER,
                visibility=iw.TrackedItemVisibility.HIDDEN,
                initialValue="0",
            )
        if self.shared_gate:
            plotline.plot_change_tracker = self.shared_change_tracker
        elif plotline.plot_change_tracker is None:
            plotline.plot_change_tracker = iw.TrackedItem(
                name=f"{plotline.name} Change",
                dataType=iw.TrackedItemDataType.NUMBER,
                visibility=iw.TrackedItemVisibility.HIDDEN,
                initialValue="1",
            )

        self._assign_internal_ids(stages, transitions)
        self._situations[id(plotline)], self._slots[id(plotline)] = self._compute_situation_slots(plotline)

    def _validate_transitions(self, plotline: Plotline):
        """A transition must have at least one starting stage, and may only reference stages of its own
        plotline (advancing another plotline's tracker would corrupt it). Checked once every stage's
        owner is known, so the reachability walk below can trust the graph."""
        for transition in plotline.plot_transitions:
            starting_stages = _as_list(transition.starting_stage)
            if not starting_stages:
                raise ValueError(
                    f"A PlotTransition must have at least one starting stage (plotline {plotline.name!r})."
                )
            for stage in starting_stages + [transition.ending_stage]:
                if self.stage_owner.get(id(stage)) is not plotline:
                    raise ValueError(
                        f"A PlotTransition in plotline {plotline.name!r} references a stage that is "
                        "not in that plotline."
                    )

    def _written_targets(self, stage: PlotStage) -> dict[str, str]:
        """Everything any of a stage's layers writes, as {target id -> human label}. Keyed by id, so the
        same block written from two different layers (or two different plotlines) is recognised as one
        target."""
        targets: dict[str, str] = {}
        for details in self._stage_layers(stage):
            for block in details.instruction_blocks:
                targets[block.id] = f"Instruction block {block.name!r}"
            for tracked_item in details.tracked_items:
                targets[tracked_item.id] = f"Tracked item {tracked_item.name!r}"
        return targets

    def _warn_contested_targets(self):
        """Warn when the plot details of two plotlines write the same instruction block or tracked item.
        Stage content is re-applied *every turn*, so the two plotlines do not take turns -- both write it
        every turn, whichever plotline's stage trigger is emitted last wins, and the other's value never
        survives a turn. Usually this means one of them meant to use its own block."""
        writers: dict[str, tuple[str, set[str]]] = {}   # target id -> (label, names of writing plotlines)
        for plotline in self.plotlines:
            for stage in plotline.plot_stages:
                for target_id, label in self._written_targets(stage).items():
                    writers.setdefault(target_id, (label, set()))[1].add(plotline.name)
        for label, names in writers.values():
            if len(names) > 1:
                warnings.warn(
                    f"{label} is written by the plot details of more than one plotline "
                    f"({', '.join(sorted(names))}). Stage content is re-applied every turn, so these "
                    "plotlines overwrite each other: whichever is emitted last wins and the others never "
                    "survive a turn. Give each plotline its own block or item unless this is deliberate.",
                    PlotContentWarning,
                    stacklevel=2,
                )

    def _downstream_stages(self, plotline: Plotline) -> dict[int, set[int]]:
        """id(stage) -> the id()s of the stages reachable from it along this plotline's transitions.
        Deliberately ignores character gates and `requires`: for a warning about stale content we want
        every stage the plot could land on afterwards, not only those one character can force."""
        edges: dict[int, list[PlotStage]] = {}
        for transition in plotline.plot_transitions:
            for start in _as_list(transition.starting_stage):
                edges.setdefault(id(start), []).append(transition.ending_stage)
        downstream: dict[int, set[int]] = {}
        for stage in plotline.plot_stages:
            seen: set[int] = set()
            frontier = list(edges.get(id(stage), []))
            while frontier:
                later = frontier.pop()
                if id(later) in seen:
                    continue
                seen.add(id(later))
                frontier.extend(edges.get(id(later), []))
            downstream[id(stage)] = seen
        return downstream

    def _warn_stale_content(self, plotline: Plotline):
        """Warn when a stage leaves alone a block or item that an earlier stage of the same plotline
        sets. Nothing clears a block or item -- it holds its last value -- so arriving at a stage that
        does not write it means the *previous* stage's text is still showing, describing a situation the
        plot has already left. The usual fix is to have every stage of a plotline write the same set of
        blocks and items."""
        downstream = self._downstream_stages(plotline)
        written = {id(stage): self._written_targets(stage) for stage in plotline.plot_stages}
        by_id = {id(stage): stage for stage in plotline.plot_stages}
        reported: set[tuple[int, str]] = set()
        for stage in plotline.plot_stages:
            for target_id, label in written[id(stage)].items():
                for later_id in downstream[id(stage)]:
                    if target_id in written[later_id] or (later_id, target_id) in reported:
                        continue
                    reported.add((later_id, target_id))
                    later_label = _stage_label(by_id[later_id])
                    warnings.warn(
                        f"{label} is set at stage {_stage_label(stage)} of plotline {plotline.name!r}, "
                        f"but stage {later_label} -- which the plot can reach from there -- never sets "
                        f"it. Arriving at stage {later_label} leaves it still showing the earlier value.",
                        PlotContentWarning,
                        stacklevel=2,
                    )

    def _find_initial_stage(self, plotline: Plotline) -> PlotStage:
        """Where the plotline starts, and where every character starts, since stages are not
        character-gated.

        A named `starting_stage` settles it. Otherwise it is what the transitions say: the one stage
        nothing transitions into. Exactly one stage must fit. Two would mean two places to start, and
        the engine would set the stage tracker twice at game start; none means every stage sits
        downstream of another, so the plot has no way in (you have wired a closed cycle) -- which is
        legal, but only once you say where to enter it."""
        if plotline.starting_stage is not None:
            if not any(stage is plotline.starting_stage for stage in plotline.plot_stages):
                raise ValueError(
                    f"Plotline {plotline.name!r} names a starting_stage "
                    f"({_stage_label(plotline.starting_stage)}) that is not one of its own stages."
                )
            return plotline.starting_stage

        targeted = {id(transition.ending_stage) for transition in plotline.plot_transitions}
        candidates = [stage for stage in plotline.plot_stages if id(stage) not in targeted]
        if len(candidates) != 1:
            found = ", ".join(_stage_label(stage) for stage in candidates) or "none"
            raise ValueError(
                f"Plotline {plotline.name!r} must have exactly one initial stage -- a stage with no "
                f"transition into it, where every character starts -- but {len(candidates)} stages have "
                f"no transition into them ({found}). Give every other stage a transition that reaches "
                "it, or name the plotline's starting_stage to say where to begin."
            )
        return candidates[0]

    def _plotline_dependencies(self) -> dict[int, set[int]]:
        """id(plotline) -> the id()s of the *other* plotlines it reads: those owning a stage named in one
        of its transitions' `requires`. A plotline that reads nobody advances entirely on its own, so it
        can be decided without looking at any other plotline."""
        dependencies: dict[int, set[int]] = {id(plotline): set() for plotline in self.plotlines}
        for plotline in self.plotlines:
            for transition in plotline.plot_transitions:
                for stage in transition.requires:
                    owner = self.stage_owner.get(id(stage))
                    if owner is None:
                        raise ValueError(
                            "A PlotTransition 'requires' a stage that is not in any plotline."
                        )
                    if owner is not plotline:
                        dependencies[id(plotline)].add(id(owner))
        return dependencies

    def _cluster(self, plotline: Plotline, dependencies: dict[int, set[int]]) -> list[Plotline]:
        """The smallest group of plotlines that must be searched together to decide `plotline`: itself
        plus everything it transitively `requires`. The group is closed -- no transition inside it reads
        a plotline outside it -- so the rest of the world cannot affect it and can be ignored. That is
        what keeps this tractable: in the martial-arts world, Fire reads nobody (5 states), Steam reads
        Fire and Water (50), and only Victory needs all four base arts (1250) -- never the 80,000 of the
        full product. A `requires` cycle between plotlines simply lands them in the same group."""
        by_id = {id(p): p for p in self.plotlines}
        group = {id(plotline)}
        frontier = [id(plotline)]
        while frontier:
            current = frontier.pop()
            for dependency in dependencies[current]:
                if dependency not in group:
                    group.add(dependency)
                    frontier.append(dependency)
        return [p for p in self.plotlines if id(p) in group]  # stable order

    def _transition_enabled(self, transition: PlotTransition, plotline: Plotline, state: tuple,
                            slot: dict[int, int], character) -> bool:
        """Can `transition` fire in this state, for this character? `trigger_on_scenario` and
        `additional_conditions` are assumed satisfiable -- we only judge what we can actually decide: the
        character gate, the starting stage, and the `requires` gates (OR within a plotline, AND across
        plotlines, exactly as they compile)."""
        allowed = [c.characterId for c in _as_list(transition.characters)]
        if allowed and (character is None or character.characterId not in allowed):
            return False
        if state[slot[id(plotline)]] not in {id(s) for s in _as_list(transition.starting_stage)}:
            return False
        groups: dict[int, set[int]] = {}
        for stage in transition.requires:
            groups.setdefault(id(self.stage_owner[id(stage)]), set()).add(id(stage))
        return all(state[slot[owner]] in stages for owner, stages in groups.items())

    def _explore(self, cluster: list[Plotline], character) -> tuple[set[int], set[int], bool]:
        """Search every way one character can advance the plotlines in `cluster`, returning the id()s of
        the stages they can reach, the id()s of the transitions that can fire, and whether the search
        completed (False if it hit the state cap).

        A state is one current stage per plotline in the cluster -- the product, because a `requires`
        gate reads where the *other* plotlines stand, so a transition's availability is a property of the
        whole cluster, not of one plotline. Nothing ever forces a plotline to advance: it sits at its
        stage until one of its own transitions fires. That is what makes this a plain BFS over reachable
        tuples, and what lets a character hold one plotline still while advancing another to line up a
        synergy gate.

        A transition that ends the game for good (`end_game` with `can_continue` False) is recorded as
        firing, but its resulting state is never expanded -- nothing can advance after it."""
        slot = {id(plotline): index for index, plotline in enumerate(cluster)}
        start = tuple(id(self._initial[id(plotline)]) for plotline in cluster)
        seen_states = {start}
        reached_stages = set(start)
        fired_transitions: set[int] = set()
        frontier = [start]
        while frontier:
            state = frontier.pop()
            for plotline in cluster:
                for transition in plotline.plot_transitions:
                    if not self._transition_enabled(transition, plotline, state, slot, character):
                        continue
                    fired_transitions.add(id(transition))
                    reached_stages.add(id(transition.ending_stage))
                    if transition.end_game and not transition.can_continue:
                        continue
                    advanced = list(state)
                    advanced[slot[id(plotline)]] = id(transition.ending_stage)
                    advanced = tuple(advanced)
                    if advanced not in seen_states:
                        if len(seen_states) >= _MAX_SEARCH_STATES:
                            return reached_stages, fired_transitions, False
                        seen_states.add(advanced)
                        frontier.append(advanced)
        return reached_stages, fired_transitions, True

    def _validate_reachability(self):
        """Check, for every character, that every stage can be reached and every transition can fire --
        searching each plotline against the cluster it actually depends on (see `_cluster`).

        Errors (dead content, always a bug): a stage no character can reach; a character-specific layer
        for a character who can never reach its stage; a transition that can never fire for a character
        it names, or for anyone at all. Warnings (often deliberate -- a character-gated branch is
        unreachable to everyone else by design): a stage some character cannot reach."""
        dependencies = self._plotline_dependencies()
        characters = self.world.possibleCharacters or [None]

        # (id(plotline), characterId) -> what that character can reach / fire in that plotline. A
        # plotline is 'undetermined' if its search hit the state cap; we then say nothing about it
        # rather than reporting errors we cannot stand behind.
        reached: dict[tuple[int, str | None], set[int]] = {}
        fired: dict[tuple[int, str | None], set[int]] = {}
        undetermined: set[int] = set()
        for plotline in self.plotlines:
            cluster = self._cluster(plotline, dependencies)
            for character in characters:
                key = (id(plotline), character.characterId if character is not None else None)
                reached[key], fired[key], complete = self._explore(cluster, character)
                if not complete:
                    undetermined.add(id(plotline))
        for plotline_id in undetermined:
            plotline = next(p for p in self.plotlines if id(p) == plotline_id)
            warnings.warn(
                f"Plotline {plotline.name!r} depends on too many other plotlines to search "
                f"({_MAX_SEARCH_STATES:,}+ possible states), so its reachability could not be fully "
                "determined. Its stages and transitions have not been checked.",
                PlotReachabilityWarning,
                stacklevel=2,
            )
            # The search is what normally reports an unreachable stage, and it did not run. A stage with
            # nothing transitioning into it that is not where the plot begins is unreachable on the
            # transitions alone, so say that much without searching.
            targeted = {id(transition.ending_stage) for transition in plotline.plot_transitions}
            for stage in plotline.plot_stages:
                if id(stage) not in targeted and stage is not self._initial[plotline_id]:
                    warnings.warn(
                        f"Stage {_stage_label(stage)} of plotline {plotline.name!r} has no transition "
                        "into it and is not where the plot begins, so nothing can ever reach it.",
                        PlotReachabilityWarning,
                        stacklevel=2,
                    )

        errors: list[str] = []
        for plotline in self.plotlines:
            if id(plotline) in undetermined:
                continue
            for character in characters:
                key = (id(plotline), character.characterId if character is not None else None)
                who = f"Character {character.name!r}" if character is not None else "The player"
                for stage in plotline.plot_stages:
                    if id(stage) in reached[key]:
                        continue
                    warnings.warn(
                        f"{who} can never reach stage {_stage_label(stage)} of plotline "
                        f"{plotline.name!r}.",
                        PlotReachabilityWarning,
                        stacklevel=2,
                    )
                    # ...and if we wrote content specifically for them there, it is dead.
                    for details in stage.character_specific_plot_details:
                        if _names_character(character, details.characters):
                            errors.append(
                                f"{who} has character-specific plot details at stage "
                                f"{_stage_label(stage)} of plotline {plotline.name!r}, but can never "
                                "reach that stage."
                            )
                for transition in plotline.plot_transitions:
                    if _names_character(character, transition.characters) and id(transition) not in fired[key]:
                        errors.append(
                            f"Transition {transition.internal_id!r} of plotline {plotline.name!r} (into "
                            f"stage {_stage_label(transition.ending_stage)}) is restricted to "
                            f"{character.name!r} (among others), but can never fire for them: its "
                            "starting stage is out of reach, or its `requires` can never hold when they "
                            "are there."
                        )

            for stage in plotline.plot_stages:
                if not any(id(stage) in reached[(id(plotline), c.characterId if c is not None else None)]
                           for c in characters):
                    errors.append(
                        f"Stage {_stage_label(stage)} of plotline {plotline.name!r} is unreachable: no "
                        "character can ever reach it."
                    )
            for transition in plotline.plot_transitions:
                if not any(id(transition) in fired[(id(plotline), c.characterId if c is not None else None)]
                           for c in characters):
                    errors.append(
                        f"Transition {transition.internal_id!r} of plotline {plotline.name!r} (into stage "
                        f"{_stage_label(transition.ending_stage)}) can never fire: no character can ever "
                        "satisfy it."
                    )

        if errors:
            raise ValueError(
                "The plot has unreachable content:\n  - " + "\n  - ".join(errors)
            )

    def _assign_internal_ids(self, stages, transitions):
        """Assign a distinct internal_id to every stage and transition that doesn't already have one.
        Numbered in separate spaces within the plotline; the string form of the lowest unused positive
        integer. Caller-provided ids are kept; duplicates are an error. A stage's internal_id doubles
        as its plotline's stage-tracker value."""
        for items in (stages, transitions):
            provided = [item.internal_id for item in items if item.internal_id is not None]
            if len(set(provided)) != len(provided):
                raise ValueError("Duplicate internal_id among a plotline's stages or transitions.")
            used = set(provided)
            next_id = 1
            for item in items:
                if item.internal_id is None:
                    while str(next_id) in used:
                        next_id += 1
                    item.internal_id = str(next_id)
                    used.add(str(next_id))

    def _compute_situation_slots(self, plotline: Plotline):
        """For each stage, the ordered distinct outgoing situations; a slot pool sized to the busiest
        stage. Every situation is read from one of these shared hidden text slots, so the engine only
        evaluates this plotline's slot pool, not every situation in it."""
        stage_situations = {id(stage): [] for stage in plotline.plot_stages}
        for transition in plotline.plot_transitions:
            if transition.trigger_on_scenario is None:
                continue
            for stage in _as_list(transition.starting_stage):
                situations = stage_situations.get(id(stage))
                if situations is not None and transition.trigger_on_scenario not in situations:
                    situations.append(transition.trigger_on_scenario)
        slot_count = max((len(situations) for situations in stage_situations.values()), default=0)
        situation_slots = [
            iw.TrackedItem(
                name=f"{plotline.name} Situation {index + 1}",
                dataType=iw.TrackedItemDataType.TEXT,
                visibility=iw.TrackedItemVisibility.HIDDEN,
                initialValue=" ",
            )
            for index in range(slot_count)
        ]
        return stage_situations, situation_slots

    def _tracked_item_effects(self, tracked_items: dict[iw.TrackedItem, str]) -> list[iw.TriggerEffect]:
        """One SET effect per tracked item, setting it to its value."""
        return [
            tools.set_tracked_item(tracked_item, value)
            for tracked_item, value in tracked_items.items()
        ]

    def _stage_layers(self, stage: PlotStage) -> list[PlotStageDetails]:
        """A stage's content layers in application order: the everyone-layer first (if any), then the
        character-specific ones -- which are therefore free to override it for their characters."""
        layers = [stage.plot_details] if stage.plot_details is not None else []
        return layers + stage.character_specific_plot_details

    def _content_effects(self, details: PlotStageDetails) -> list[iw.TriggerEffect]:
        """One content layer's effects: overwrite each instruction block with its text, set each
        tracked item to its value, then run the layer's extra effects."""
        return [
            iw.TriggerEffect(
                type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
                data={"id": block.id, "content": content},
            )
            for block, content in details.instruction_blocks.items()
        ] + self._tracked_item_effects(details.tracked_items) + details.additional_effects

    def _character_conditions(self, details: PlotStageDetails) -> list[iw.TriggerCondition]:
        """The condition restricting a layer to its characters -- empty for the everyone-layer."""
        characters = _as_list(details.characters)
        if not characters:
            return []
        return [iw.TriggerCondition(
            type=iw.ConditionType.ON_CHARACTER,
            category="condition",
            data=[character.characterId for character in characters],
        )]

    def _at_stage_condition(self, plotline: Plotline, stage: PlotStage) -> iw.TriggerCondition:
        """A fresh condition: `plotline`'s stage tracker is exactly at `stage`. Built per call because
        every condition carries its own id."""
        tracker = plotline.plot_stage_tracker
        assert tracker is not None  # resolved during setup
        return tools.tracked_item_is(tracker, str(stage.internal_id))

    def _layer_trigger_name(self, base: str, details: PlotStageDetails) -> str:
        """A layer's trigger name: the stage's name, plus the characters it is scoped to (if any)."""
        characters = _as_list(details.characters)
        if not characters:
            return base
        return f"{base} ({', '.join(character.name for character in characters)})"

    def _slot_effects(self, plotline: Plotline, stage: PlotStage) -> list[iw.TriggerEffect]:
        """One SET effect per situation slot: slot i holds this stage's i-th outgoing situation, with
        any leftover slots set to a single space so they stay inert."""
        situations = self._situations[id(plotline)][id(stage)]
        return [
            tools.set_tracked_item(slot, situations[index] if index < len(situations) else " ")
            for index, slot in enumerate(self._slots[id(plotline)])
        ]

    def _synergy_conditions(self, transition: PlotTransition) -> list[iw.TriggerCondition]:
        """Resolve `requires` into conditions on other plotlines' stage trackers. Required stages are
        grouped by their owning plotline: within a plotline they are OR'd (any listed stage qualifies);
        the per-plotline groups are then AND'd in with the rest of the transition's conditions."""
        groups: dict[int, list[PlotStage]] = {}
        owners: dict[int, Plotline] = {}
        for stage in transition.requires:
            owner = self.stage_owner.get(id(stage))
            if owner is None:
                raise ValueError("A PlotTransition 'requires' a stage that is not in any plotline.")
            groups.setdefault(id(owner), []).append(stage)
            owners[id(owner)] = owner

        conditions = []
        for owner_id, stages in groups.items():
            matches = [self._at_stage_condition(owners[owner_id], stage) for stage in stages]
            if len(matches) == 1:
                conditions.append(matches[0])
            else:
                # Any of this plotline's listed stages satisfies the requirement.
                conditions.append(iw.TriggerCondition(
                    category="logic",
                    operator=iw.LogicOperator.OR,
                    data=matches,
                ))
        return conditions

    def _build_reset_trigger(self, change_tracker: iw.TrackedItem, name: str) -> iw.TriggerEvent:
        """Open a per-turn gate (set its change tracker to 0) every turn, before any other plot
        trigger. A non-start-of-game trigger needs at least one condition to fire, so we gate it on a
        trivially-true one: the built-in `turn_number` is always >= 1."""
        # `turn_number` is an engine built-in, so it is named by a raw id rather than a TrackedItem.
        return iw.TriggerEvent(
            name=f"{name}: reset per-turn change gate",
            canTriggerMoreThanOnce=True,
            triggerConditions=[tools.tracked_item_is("turn_number", "1", iw.Inequality.AT_LEAST)],
            triggerEffects=[tools.set_tracked_item(change_tracker, "0")],
        )

    def _build_start_triggers(self, plotline: Plotline, stage: PlotStage) -> list[iw.TriggerEvent]:
        """Set the stage tracker and apply the opening stage's content, before the first turn and on any
        later turn the plot is back at that stage. The first trigger runs for whichever character was
        chosen -- it carries the stage tracker, the situation slots, and the everyone-layer's content.
        Each character-specific layer then gets its own trigger, emitted after it so it can override the
        same blocks and items.

        Gated on being at the stage, exactly as every other stage's triggers are. Without that condition
        a mid-game firing would drag the plot back to its opening every turn; with it, a plot that loops
        round to where it began is served the same way it was on turn one."""
        stage_tracker = plotline.plot_stage_tracker
        assert stage_tracker is not None  # resolved during setup

        base_effects = [
            tools.set_tracked_item(stage_tracker, str(stage.internal_id)),
        ] + self._slot_effects(plotline, stage)
        if stage.plot_details is not None:
            base_effects = self._content_effects(stage.plot_details) + base_effects

        name = f"{plotline.name}: start of game (stage {stage.internal_id})"
        triggers = [iw.TriggerEvent(
            name=name,
            triggerOnStartOfGame=True,
            triggerMidGame=True,
            canTriggerMoreThanOnce=True,
            triggerConditions=[self._at_stage_condition(plotline, stage)],
            triggerEffects=base_effects,
        )]
        for details in stage.character_specific_plot_details:
            triggers.append(iw.TriggerEvent(
                name=self._layer_trigger_name(name, details),
                triggerOnStartOfGame=True,
                triggerMidGame=True,
                canTriggerMoreThanOnce=True,
                triggerConditions=[
                    self._at_stage_condition(plotline, stage),
                    *self._character_conditions(details),
                ],
                triggerEffects=self._content_effects(details),
            ))
        return triggers

    def _build_transition_trigger(self, plotline: Plotline, transition: PlotTransition) -> iw.TriggerEvent:
        """Build the trigger for a single transition: require this plotline's gate open and the plot at
        one of the starting stage(s) (plus the scenario, character, synergy `requires`, and any extra
        conditions), then claim the gate, advance the stage tracker, and run the transition's effects."""
        starting_stages = _as_list(transition.starting_stage)
        ending_number = transition.ending_stage.internal_id
        stage_tracker = plotline.plot_stage_tracker
        change_tracker = plotline.plot_change_tracker
        assert stage_tracker is not None and change_tracker is not None  # resolved during setup
        stage_situations = self._situations[id(plotline)]
        slots = self._slots[id(plotline)]

        # Per starting stage: the plot is at that stage, and (if there's a scenario) the slot holding
        # that scenario for that stage has fired.
        branches = []
        for stage in starting_stages:
            branch = [self._at_stage_condition(plotline, stage)]
            if transition.trigger_on_scenario is not None:
                slot = slots[stage_situations[id(stage)].index(transition.trigger_on_scenario)]
                branch.append(iw.TriggerCondition(
                    type=iw.ConditionType.ON_EVENT,
                    category="condition",
                    data=slot.as_substitution(),
                ))
            branches.append(branch)

        if len(branches) == 1:
            starting_conditions = branches[0]
            advanced_logic = False
        else:
            starting_conditions = [iw.TriggerCondition(
                category="logic",
                operator=iw.LogicOperator.OR,
                data=[
                    branch[0] if len(branch) == 1 else iw.TriggerCondition(
                        category="logic", operator=iw.LogicOperator.AND, data=branch
                    )
                    for branch in branches
                ],
            )]
            advanced_logic = True

        and_conditions = [
            # Require this plotline's per-turn gate to be open.
            tools.tracked_item_is(change_tracker, "0"),
            *starting_conditions,
        ]
        if transition.characters:
            and_conditions.append(iw.TriggerCondition(
                type=iw.ConditionType.ON_CHARACTER,
                category="condition",
                data=[character.characterId for character in _as_list(transition.characters)],
            ))

        # Cross-plotline synergy gates, then caller-supplied extra conditions. Any logic group among
        # them (a synergy OR, or a user-built group) forces advancedLogic.
        synergy = self._synergy_conditions(transition)
        and_conditions.extend(synergy)
        and_conditions.extend(transition.additional_conditions)
        if any(condition.category == "logic" for condition in synergy + transition.additional_conditions):
            advanced_logic = True

        # A logic group is only valid under advancedLogic, where the engine expects a single root
        # group, so wrap the AND in one. Otherwise a flat, implicitly-AND'd list is enough.
        if advanced_logic:
            conditions = [iw.TriggerCondition(
                category="logic",
                operator=iw.LogicOperator.AND,
                data=and_conditions,
            )]
        else:
            conditions = and_conditions

        effects = [
            # Claim the per-turn gate so no later transition in this plotline advances this turn.
            tools.set_tracked_item(change_tracker, "1"),
            # Advance the stage tracker to this transition's ending stage.
            tools.set_tracked_item(stage_tracker, str(ending_number)),
            # Set once, here, rather than every turn like a stage's tracked items.
            *self._tracked_item_effects(transition.tracked_items),
        ]
        if transition.transition_event is not None:
            effects.append(iw.TriggerEffect(type=iw.EffectType.TELL_AI, data=transition.transition_event))
        if transition.show_message is not None:
            effects.append(iw.TriggerEffect(type=iw.EffectType.SHOW_MESSAGE, data=transition.show_message))
        if transition.end_game:
            effects.append(iw.TriggerEffect(type=iw.EffectType.ENDS_GAME, data=transition.can_continue))
        effects.extend(transition.additional_effects)

        return iw.TriggerEvent(
            name=f"{plotline.name} Transition {transition.internal_id}",
            canTriggerMoreThanOnce=True,
            advancedLogic=advanced_logic or None,
            triggerConditions=conditions,
            triggerEffects=effects,
        )

    def _build_stage_triggers(self, plotline: Plotline, stage: PlotStage) -> list[iw.TriggerEvent]:
        """Build the triggers for a single stage: whenever the tracker reaches the stage's id, apply its
        content. Not gated on the change tracker, so they fire the same turn a transition arrives. The
        first trigger carries the situation slots and the everyone-layer's content; each
        character-specific layer follows, adding a character condition so it overrides the same blocks
        and items for its characters only."""
        base_effects = self._slot_effects(plotline, stage)
        if stage.plot_details is not None:
            base_effects = self._content_effects(stage.plot_details) + base_effects

        name = f"{plotline.name} Stage {stage.internal_id}"
        triggers = [iw.TriggerEvent(
            name=name,
            canTriggerMoreThanOnce=True,
            triggerConditions=[self._at_stage_condition(plotline, stage)],
            triggerEffects=base_effects,
        )]
        for details in stage.character_specific_plot_details:
            triggers.append(iw.TriggerEvent(
                name=self._layer_trigger_name(name, details),
                canTriggerMoreThanOnce=True,
                triggerConditions=[
                    self._at_stage_condition(plotline, stage),
                    *self._character_conditions(details),
                ],
                triggerEffects=self._content_effects(details),
            ))
        return triggers

    def run(self) -> None:
        """Add every plotline's tracked items and triggers to the input world, in place.

        Within a plotline, triggers are evaluated top-to-bottom, once per turn, so order is
        load-bearing: reset (opens the gate) -> start/transitions (advance) -> stage triggers (apply
        content). Plotlines are emitted in order; with a shared gate there is one reset up front."""
        # Add the trackers, unless an item with the same id is already present.
        trackers = []
        if self.shared_gate:
            trackers.append(self.shared_change_tracker)
        for plotline in self.plotlines:
            trackers.append(plotline.plot_stage_tracker)
            if not self.shared_gate:
                trackers.append(plotline.plot_change_tracker)
            trackers.extend(self._slots[id(plotline)])
        for tracker in trackers:
            if not any(item.id == tracker.id for item in self.world.trackedItems):
                self.world.trackedItems.append(tracker)

        triggers = []
        if self.shared_gate:
            triggers.append(self._build_reset_trigger(self.shared_change_tracker, "Plot"))
        for plotline in self.plotlines:
            if not self.shared_gate:
                triggers.append(self._build_reset_trigger(plotline.plot_change_tracker, plotline.name))
            triggers.extend(self._build_start_triggers(plotline, self._initial[id(plotline)]))
            for transition in plotline.plot_transitions:
                triggers.append(self._build_transition_trigger(plotline, transition))
            for stage in plotline.plot_stages:
                triggers.extend(self._build_stage_triggers(plotline, stage))
        self.world.triggerEvents.extend(triggers)


def add_plots(world: iw.World, plotlines: list[Plotline], shared_gate: bool = False) -> None:
    """Build all the given plotlines into `world`, in place: the tracked items and triggers they compile
    to are added to the world you pass in. The plotlines (and their stages/transitions) are deep-copied,
    so nothing you pass in as a plotline is modified -- but the world itself is. `shared_gate` controls
    the per-turn mutex (see PlotlineHandler)."""
    PlotlineHandler(world, plotlines, shared_gate=shared_gate).run()


def add_single_plot(world: iw.World, plot_stages: list[PlotStage],
                    plot_transitions: list[PlotTransition],
                    starting_stage: PlotStage | None = None) -> None:
    """Single-plotline convenience: build one plotline named "Plot" and add it to `world`, in place. For
    a custom name or trackers, call add_plots with an explicit Plotline (see add_plots). `starting_stage`
    says where the plot begins; left out, it is deduced from the transitions (see Plotline)."""
    add_plots(world, [Plotline("Plot", plot_stages, plot_transitions, starting_stage=starting_stage)])
