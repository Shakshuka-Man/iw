from __future__ import annotations

import hashlib
import json
import random
import string
import uuid
from dataclasses import asdict, dataclass, field, fields, is_dataclass, MISSING
from enum import StrEnum
from typing import Any, Optional, Union, get_type_hints, get_origin, get_args


# ---- ID Generation ---------------------------------------------------------

_SHORT_ID_CHARS = string.ascii_letters + string.digits
_SHORT_ID_FIRST_CHARS = string.ascii_letters


class IDGenerator:
    """Deterministic ID generator. A single shared instance ensures uniqueness
    across all call sites without requiring manual ID management."""

    def __init__(self, seed: int = 0):
        self._rng = random.Random(seed)

    def next_uuid(self) -> str:
        return str(uuid.UUID(int=self._rng.getrandbits(128), version=4))

    def next_short(self, length: int = 8) -> str:
        first = self._rng.choice(_SHORT_ID_FIRST_CHARS)
        rest = ''.join(self._rng.choice(_SHORT_ID_CHARS) for _ in range(length - 1))
        return first + rest

    def seed(self, value: int) -> None:
        self._rng = random.Random(value)


_id = IDGenerator()


def reset_ids(seed: int = 0) -> None:
    """Reset the shared ID generator. Ids are drawn from one seeded sequence, so a world's ids depend on
    everything generated before it in the same process. Call this before building a world to make its
    output reproducible no matter what else was built first (the build script does)."""
    _id.seed(seed)


# ---- Enums -----------------------------------------------------------------

class TrackedItemDataType(StrEnum):
    TEXT = "text"
    NUMBER = "number"
    XML = "xml"
    YAML = "yaml"  # a structured document; addressed with the engine's $-script (see RUN_SCRIPT)


class TrackedItemVisibility(StrEnum):
    EVERYONE = "everyone"
    AI_ONLY = "ai_only"
    PLAYER_ONLY = "player_only"
    HIDDEN = "hidden"
    HIDDEN_BORING = "hidden_boring"


class TrackedItemInitialValueSource(StrEnum):
    SAME = "same"
    CHARACTER = "character"
    PLAYER = "player"


class TrackedItemAction(StrEnum):
    SET = "set"
    ADD = "add"
    SUBTRACT = "subtract"
    REPLACE = "replace"


class Inequality(StrEnum):
    IS_EXACTLY = "is_exactly"
    AT_LEAST = "at_least"
    AT_MOST = "at_most"
    NOT_EQUAL = "not_equal"


class EffectType(StrEnum):
    SHOW_MESSAGE = "effectShowMessage"
    GIVE_INFO = "effectGiveInfo"
    TELL_AI = "effectTellAIWhatToDo"
    CHANGE_MAIN_INSTRUCTIONS = "effectChangeMainInstructions"
    MODIFY_INSTRUCTION_BLOCK = "effectModifyInstructionBlock"
    CHANGE_AUTHOR_STYLE = "effectChangeAuthorStyle"
    CHANGE_DESCRIPTION_INSTRUCTIONS = "effectChangeDescriptionInstructions"
    CHANGE_OBJECTIVE = "effectChangeObjective"
    CHANGE_BACKGROUND = "effectChangeBackground"
    CHANGE_FIRST_ACTION = "effectChangeFirstAction"
    CHANGE_VICTORY_CONDITION = "effectChangeVictoryCondition"
    CHANGE_DEFEAT_CONDITION = "effectChangeDefeatCondition"
    CHANGE_PC_NAME = "effectChangePCName"
    CHANGE_PC_DESCRIPTION = "effectChangePCDescription"
    CHANGE_PC_SKILL = "effectChangePCSkill"
    SET_TRACKED_ITEM_VALUE = "effectSetTrackedItemValue"
    RUN_SCRIPT = "effectRunScript"  # data is a $-script block, e.g. "for each $member in $party\n  $member.hp += 5"
    FIRE_RANDOM_TRIGGER = "effectFireRandomTrigger"
    MODIFY_KEYWORD_BLOCK = "effectModifyKeywordBlock"
    ENDS_GAME = "effectEndsGame"
    MODIFY_TRACKED_ITEM_DETAILS = "effectModifyTrackedItemDetails"
    PRESENT_CHOICE = "effectPresentChoice"
    REQUEST_INPUT = "effectRequestInput"


class ConditionType(StrEnum):
    ON_TURN = "triggerOnTurn"
    ON_EVENT = "triggerOnEvent"
    ON_CHARACTER = "triggerOnCharacter"
    ON_TRACKED_ITEM = "triggerOnTrackedItem"
    ON_RANDOM_CHANCE = "triggerOnRandomChance"
    ON_PAW_SCRIPT = "triggerOnPawScript"  # data is a $-script expression, e.g. "$party.count()>1"
    PREREQS = "triggerPrereqs"


class LogicOperator(StrEnum):
    AND = "and"
    OR = "or"


# Tracked item ids the engine provides itself, so a trigger may reference them without the world
# declaring them. `turn_number` is the one we rely on (a condition on it is the "every turn" idiom).
# If you hit a validation error naming an id you know the engine supplies, add it here.
BUILTIN_TRACKED_ITEM_IDS: set[str] = {"turn_number"}


# ---- Dataclasses -----------------------------------------------------------

@dataclass(eq=False)
class ImagePromptDetails:
    illustrGenre: str = ""
    illustrClothes: str = ""
    illustrSetting: str = ""
    illustrSubject: str = ""
    illustrAppearance: str = ""
    illustrIsCharacter: bool = True
    illustrExpressionPosition: str = ""


@dataclass(eq=False)
class PermissionsOnceShared:
    sharing: bool = True
    editing: bool = True


@dataclass(eq=False)
class PortraitPromptDetails:
    illustrGenre: str = ""
    illustrClothes: str = ""
    illustrSetting: str = ""
    illustrSubject: str = ""
    illustrAppearance: str = ""
    illustrIsCharacter: bool = True
    illustrExpressionPosition: str = ""


@dataclass(eq=False)
class VictoryDefeatCondition:
    condition: str
    text: str
    alreadyFired: bool = False


@dataclass(eq=False)
class InitialTrackedItemValue:
    id: str
    name: str
    # A plain value, or a list of values for the player to choose between when this character is picked.
    initialPCValue: str | list[str] = ""
    visibility: TrackedItemVisibility = TrackedItemVisibility.AI_ONLY
    initialValueBasedOnPC: TrackedItemInitialValueSource = TrackedItemInitialValueSource.CHARACTER
    # Newer engine field: a $-script yielding the choices for this per-character value. None -> stripped.
    initialPCValueChoicesScript: Optional[str] = None


@dataclass(eq=False)
class TrackedItem:
    name: str
    id: str = field(default_factory=_id.next_short)
    dataType: TrackedItemDataType = TrackedItemDataType.TEXT
    visibility: TrackedItemVisibility = TrackedItemVisibility.EVERYONE
    description: str = ""
    updateInstructions: str = ""
    initialValue: str = ""
    initialValueBasedOnPC: TrackedItemInitialValueSource = TrackedItemInitialValueSource.SAME
    autoUpdate: bool = False
    # Newer engine fields (structured-data / $-script feature). Default None so they are stripped from
    # output unless set -- worlds that predate the feature serialise exactly as before. `variableName`
    # is the item's $-script handle (the engine derives it from the name, same rule as as_substitution).
    variableName: Optional[str] = None
    enforceFormat: Optional[bool] = None
    formatSchema: Optional[str] = None
    formatExample: Optional[str] = None
    driftAcknowledgedForName: Optional[str] = None
    # Only meaningful when initialValueBasedOnPC is PLAYER: the choices the player picks between, given
    # either literally or as a $-script yielding them. `initialValue` is then the default selection.
    # (The CHARACTER-mode equivalents live on InitialTrackedItemValue, per character.)
    initialValueChoices: Optional[list[str]] = None
    initialValueChoicesScript: Optional[str] = None

    @property
    def variable_name(self) -> str:
        """The item's handle: its `variableName` if one is set, otherwise the name lowercased with spaces
        replaced by underscores. The engine derives `variableName` from the name, but the two can now
        diverge -- a renamed item keeps its original handle -- so it is this, not the visible `name`, that
        a `$`-script or a substitution refers to. (The raw `variableName` field may be None; this never is.)"""
        return self.variableName or self.name.replace(" ", "_").lower()

    def as_substitution(self) -> str:
        """This item's `variable_name` wrapped as a `<<...>>` substitution token -- the form used to
        reference it inside trigger and instruction text."""
        return f"<<{self.variable_name}>>"


@dataclass(eq=False)
class NPC:
    name: str
    id: str = field(default_factory=_id.next_short)
    detail: str = ""
    one_liner: str = ""
    appearance: str = ""
    location: str = ""
    secret_info: str = ""
    names: list[str] = field(default_factory=list)
    img_appearance: str = ""
    img_clothing: str = ""


@dataclass(eq=False)
class InstructionBlock:
    name: str
    content: str = ""
    id: str = field(default_factory=_id.next_short)
    selectedAIProfiles: Optional[list[str]] = None


@dataclass(eq=False)
class LoreBookEntry:
    name: str
    content: str = ""
    id: str = field(default_factory=_id.next_short)
    keywords: list[str] = field(default_factory=list)


@dataclass(eq=False)
class PossibleCharacter:
    name: str
    description: str = ""
    portrait: str = ""
    portraitPromptDetails: PortraitPromptDetails = field(default_factory=PortraitPromptDetails)
    fullSizePortrait: str = ""
    portraitOptions: list[str] = field(default_factory=list)
    fullSizePortraitOptions: list[str] = field(default_factory=list)
    currentPortraitIndex: int = 0
    characterId: str = field(default_factory=_id.next_short)
    skills: dict[str, int] = field(default_factory=dict)
    initialTrackedItemValues: list[InitialTrackedItemValue] = field(default_factory=list)


@dataclass(eq=False)
class TriggerEffect:
    type: EffectType
    data: Any
    id: str = field(default_factory=_id.next_uuid)
    trackedItemID: Optional[str] = None


@dataclass(eq=False)
class TriggerCondition:
    data: Any
    id: str = field(default_factory=_id.next_uuid)
    type: Optional[ConditionType] = None
    category: Optional[str] = None
    trackedItemID: Optional[str] = None
    inequality: Optional[Inequality] = None
    operator: Optional[LogicOperator] = None

    def __post_init__(self) -> None:
        # A logic group's `data` is its sub-conditions. Parsed JSON hands those over as raw dicts, so
        # build them out here: a group then holds TriggerConditions however it was constructed, which is
        # what the library's own groups already hold and what validate() walks. Nesting is handled by
        # recursion -- each sub-condition runs this in turn. Only logic groups get this treatment; other
        # list-valued `data` (character ids, trigger ids) is a list of plain strings.
        if self.category == "logic" and isinstance(self.data, list):
            self.data = [
                _build(TriggerCondition, sub) if isinstance(sub, dict) else sub
                for sub in self.data
            ]


@dataclass(eq=False)
class TriggerEvent:
    name: str
    id: str = field(default_factory=_id.next_short)
    triggerEffects: list[TriggerEffect] = field(default_factory=list)
    triggerConditions: list[TriggerCondition] = field(default_factory=list)
    advancedLogic: Optional[bool] = None
    triggerOnStartOfGame: Optional[bool] = None
    canTriggerMoreThanOnce: Optional[bool] = None


# ---- World -----------------------------------------------------------------

_OPTIONAL_FIELDS: set[str] = {
    "descriptionRequest", "summaryRequest", "charSelectText",
    "instructionBlocks", "loreBookEntries", "trackedItems", "NPCs",
    "version", "autoAdvanceVersion", "designNotes", "evaluationRequest",
}


def _convert(hint, val):
    """Convert a JSON value to the appropriate Python type based on a type hint."""
    if val is None:
        return None
    origin = get_origin(hint)
    args = get_args(hint)
    if origin is Union:
        non_none = [a for a in args if a is not type(None)]
        if len(non_none) == 1:
            return _convert(non_none[0], val)
        return val
    if origin is list and args:
        return [_convert(args[0], item) for item in val]
    if origin is dict:
        return val
    if is_dataclass(hint):
        return _build(hint, val)
    if isinstance(hint, type) and issubclass(hint, StrEnum):
        return hint(val)
    return val


_IGNORED_FIELDS = {"positionInList"}


def _build(cls, data: dict):
    """Construct a dataclass instance from a dict, recursively converting nested types."""
    hints = get_type_hints(cls)
    known = {f.name for f in fields(cls)} | _IGNORED_FIELDS
    unknown = set(data) - known
    if unknown:
        raise NotImplementedError(
            f"{cls.__name__} has no fields for: {', '.join(sorted(unknown))}"
        )
    kwargs = {}
    for f in fields(cls):
        if f.name not in data:
            continue
        kwargs[f.name] = _convert(hints[f.name], data[f.name])
    return cls(**kwargs)


def _strip_none(obj):
    """Recursively remove None values from dicts (and nested structures)."""
    if isinstance(obj, dict):
        return {k: _strip_none(v) for k, v in obj.items() if v is not None}
    if isinstance(obj, list):
        return [_strip_none(x) for x in obj]
    return obj


@dataclass(eq=False)
class World:
    favorite: bool = False
    title: str = ""
    description: str = ""
    background: str = ""
    instructions: str = ""
    authorStyle: str = ""
    recommendedAIModel: Optional[str] = None
    firstInput: str = ""
    objective: str = ""

    imageModel: str = "manticore"
    imageStyle: str = "photo_1"
    illustrationStyleNonCharacterLowPriority: str = ""
    illustrationStyleNonCharacterHighPriority: str = ""
    illustrationStyleCharacterLowPriority: str = ""
    illustrationStyleCharacterHighPriority: str = ""
    imageStyleCharacterPre: str = ""
    imageStyleCharacterPost: str = ""
    imageStyleNonCharacterPre: str = ""
    imageStyleNonCharacterPost: str = ""

    nsfw: bool = False
    mature: bool = False
    contentWarnings: str = ""
    enableAISpecificInstructionBlocks: bool = False

    previewImage: str = ""
    fullSizePreviewImage: str = ""
    previewImageOptions: list[str] = field(default_factory=list)
    fullSizePreviewImageOptions: list[str] = field(default_factory=list)
    currentPreviewImageIndex: int = -1

    imagePromptDetails: ImagePromptDetails = field(default_factory=ImagePromptDetails)
    permissionsOnceShared: PermissionsOnceShared = field(default_factory=PermissionsOnceShared)

    allowChangeCharacterName: bool = True
    allowChangeCharacterDescription: bool = True
    allowChangeCharacterSkills: bool = False
    allowChangeCharacterItemValues: bool = False
    allowChangeCharacterPortrait: bool = True
    allowChangeCharacterNewPortrait: bool = True

    evaluationRequest: str = ""

    schemaVersion: Optional[float] = 2.2
    skills: list[str] = field(default_factory=list)
    hideSkillSystem: bool = False
    possibleCharacters: list[PossibleCharacter] = field(default_factory=list)
    triggerEvents: list[TriggerEvent] = field(default_factory=list)
    victoryCondition: Optional[VictoryDefeatCondition] = None
    defeatCondition: Optional[VictoryDefeatCondition] = None

    # Optional fields — only included in JSON when non-default
    descriptionRequest: str = ""
    summaryRequest: str = ""
    charSelectText: Optional[str] = None
    instructionBlocks: list[InstructionBlock] = field(default_factory=list)
    loreBookEntries: list[LoreBookEntry] = field(default_factory=list)
    trackedItems: list[TrackedItem] = field(default_factory=list)
    NPCs: list[NPC] = field(default_factory=list)
    version: str = "0.01"
    autoAdvanceVersion: bool = True
    designNotes: Optional[str] = None

    def summary(self) -> str:
        """A readable account of what is in this world. Print it before and after a change to see
        exactly what that change did."""

        def row(label: str, count: int, names: list[str]) -> str:
            detail = f"   {', '.join(names)}" if names else ""
            return f"  {label:<25}{count:>5}{detail}"

        # Length, not count, is what a world spends the AI's context budget on: the main brief plus
        # every extra instruction block, and separately the KIBs, all measured in characters.
        instruction_length = len(self.instructions) + sum(len(block.content) for block in self.instructionBlocks)
        kib_length = sum(len(entry.content) for entry in self.loreBookEntries)

        lines = [
            f"  {'title':<25}{'':>5}   {self.title or '(none)'}",
            # The cast, split by the role the engine gives them: the people you can *be*, and the
            # people you can only meet. They are different types and different fields, and a world that
            # has plenty of one and none of the other is usually a world with a bug in it.
            row("playable characters", len(self.possibleCharacters), [c.name for c in self.possibleCharacters]),
            row("NPCs", len(self.NPCs), [n.name for n in self.NPCs]),
            row("Extra instruction blocks", len(self.instructionBlocks), [b.name for b in self.instructionBlocks]),
            row("instruction length", instruction_length, []),
            # Keyword instruction blocks -- KIBs. The engine's own effect for rewriting one is
            # `effectModifyKeywordBlock`, though the field it stores them in is `loreBookEntries`.
            row("KIBs (lore books)", len(self.loreBookEntries), [e.name for e in self.loreBookEntries]),
            row("KIB length", kib_length, []),
            row("tracked items", len(self.trackedItems), []),
        ]
        for item in self.trackedItems:
            lines.append(f"  {'':<25}    - {item.name}  ({item.dataType}, {item.visibility})")
        lines.append(row("trigger events", len(self.triggerEvents), []))
        return "\n".join(lines)

    def validate(self) -> None:
        """Check the world hangs together: nothing named twice, and nothing referring to something that
        isn't there. Raises ValueError listing every problem found.

        Triggers reference tracked items, instruction blocks and characters by id. A reference to an id
        that no longer exists produces a world the engine will load happily and then quietly ignore --
        the trigger simply never does anything. That is a miserable bug to find by playing, so we refuse
        to emit it."""
        errors: list[str] = []

        def duplicates(noun: str, field_name: str, values: list[str]) -> None:
            seen: set[str] = set()
            for value in values:
                if value in seen:
                    errors.append(f"Two {noun}s share the same {field_name}: {value!r}.")
                seen.add(value)

        duplicates("tracked item", "id", [item.id for item in self.trackedItems])
        # Names matter as much as ids: a tracked item's name *is* its <<substitution_token>>, so two
        # items with the same name give you a token that could mean either.
        duplicates("tracked item", "name", [item.name for item in self.trackedItems])
        duplicates("instruction block", "id", [block.id for block in self.instructionBlocks])
        duplicates("character", "id", [character.characterId for character in self.possibleCharacters])

        tracked_ids = {item.id for item in self.trackedItems} | BUILTIN_TRACKED_ITEM_IDS
        block_ids = {block.id for block in self.instructionBlocks}
        character_ids = {character.characterId for character in self.possibleCharacters}

        def check_tracked(value, where: str) -> None:
            if isinstance(value, str) and value and value not in tracked_ids:
                errors.append(
                    f"{where} refers to tracked item id {value!r}, which is not in the world. If this "
                    "is an engine built-in, add it to iw.BUILTIN_TRACKED_ITEM_IDS."
                )

        def check_conditions(conditions: list[TriggerCondition], where: str) -> None:
            for condition in conditions:
                check_tracked(condition.trackedItemID, where)
                if isinstance(condition.data, dict):
                    check_tracked(condition.data.get("trackedItemID"), where)
                elif condition.category == "logic" and isinstance(condition.data, list):
                    check_conditions(condition.data, where)          # a nested AND/OR group
                elif condition.type == ConditionType.ON_CHARACTER and isinstance(condition.data, list):
                    for character_id in condition.data:
                        if character_id not in character_ids:
                            errors.append(f"{where} is gated on character id {character_id!r}, "
                                          "which is not in the world.")

        for trigger in self.triggerEvents:
            where = f"Trigger {trigger.name!r}"
            check_conditions(trigger.triggerConditions, where)
            for effect in trigger.triggerEffects:
                check_tracked(effect.trackedItemID, where)
                if isinstance(effect.data, dict):
                    check_tracked(effect.data.get("trackedItemID"), where)
                    if effect.type == EffectType.MODIFY_INSTRUCTION_BLOCK:
                        block_id = effect.data.get("id")
                        if block_id not in block_ids:
                            errors.append(f"{where} rewrites instruction block id {block_id!r}, "
                                          "which is not in the world.")

        # The same broken reference usually shows up twice -- a condition names its tracked item both on
        # the condition itself and inside its data. Report the problem, not the plumbing.
        unique = list(dict.fromkeys(errors))
        if unique:
            raise ValueError(
                f"This world does not hang together ({len(unique)} problem"
                f"{'s' if len(unique) > 1 else ''}):\n  - " + "\n  - ".join(unique)
            )

    def to_dict(self) -> dict:
        raw = asdict(self)
        result = {}
        for f in fields(self):
            val = raw[f.name]
            if f.name in _OPTIONAL_FIELDS:
                if f.default is not MISSING and val == f.default:
                    continue
                if f.default_factory is not MISSING and val == f.default_factory():
                    continue
            if isinstance(val, list):
                val = [_strip_none(item) for item in val]
            result[f.name] = val
        for key in ("trackedItems", "NPCs"):
            for i, item in enumerate(result.get(key, [])):
                item["positionInList"] = i
        return result

    def to_json(self) -> str:
        """The world, as the JSON the engine loads.

        Validates first, and raises rather than emit a world that does not hang together. This is the
        one door out of the library, so it is the right place for that check: an invalid world is not a
        thing you ever want to have written to a file, and a caller who has to remember to ask for the
        check is a caller who will one day forget."""
        self.validate()
        return json.dumps(self.to_dict(), indent=4)

    @classmethod
    def from_dict(cls, data: dict) -> World:
        # Re-seed the ID generator with the hash of the data to avoid ID collisions
        _id.seed(int(hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest(), 16))
        return _build(cls, data)

    @classmethod
    def from_json(cls, json_str: str) -> World:
        return cls.from_dict(json.loads(json_str))
