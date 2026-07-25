"""Navigation: pure calculation over the jump graph -- pathfinding, and what the AI is told about a system.

Two technologies and one hard limit. The inertial resonator moves you *within* a system and needs no fuel;
the jump drive moves you *between* them, but only through naturally occurring jump points, and only if
your ship can survive one that hard. The prose that explains all this to the AI -- the resonator, the jump
drive, the galactic web of jump points -- is setting lore and lives in `setting.py`.

This file is pure calculation: it holds no world objects and writes no tracked items -- it does not even
import `iw`. `systems` holds the map's *data* (the nodes, and the jump links `ALL_JUMP_LINKS` between
them, each edge carrying a difficulty -- soft points are wide and forgiving, hard ones barely there); this
is the *logic* over that data. The solver answers the only question the graph is really asked: from here,
in a ship that can survive jumps *this* hard, what can I reach and how long does it take? The routes out to
each sector gateway are precomputed once, at import, into `_GATEWAY_PATHS` -- there are 126 systems and the
AI asks constantly.

The *triggers* that actually move you and rewrite the sheet on arrival -- the six jump slots, and the
per-system info and path tables -- are not here. They write the character sheet, so they live in
`player_details` beside the items they maintain, and call the three functions this file exposes
(`info_json`, `paths_json`, `adjacent_jumps`) to do the sums. The six-jump-slots trick is documented there.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Optional, Union

from .enums import JumpDifficulty, StarClusters
from .systems import ALL_JUMP_LINKS, JumpLink, System, get_all_jump_links, get_systems


# ==== The jump graph: the solver =================================================================
#
# `systems` owns the map's data -- the nodes, and the jump links (`ALL_JUMP_LINKS`) between them. This is
# the logic over that data: the solver, the gateway-route precompute, and the two serializations the
# character sheet is fed on arrival (`info_json` -> "Current system info", `paths_json` -> "Current sector
# paths").


@dataclass
class PathToGateway:
    minimum_difficulty: str
    length: int
    duration_days: int
    path: list[str]

    @staticmethod
    def duration_of(path: list[str], durations: dict[tuple[str, str], int]) -> int:
        """Sum the duration of each hop along a path."""
        return sum(durations.get((path[i], path[i + 1]), 0) for i in range(len(path) - 1))


def _difficulty_level(d: JumpDifficulty) -> int:
    return {"Soft": 0, "Moderate": 1, "Hard": 2}.get(d.value, 0)


def _build_link_duration_map() -> dict[tuple[str, str], int]:
    """Build a map from (system1_name, system2_name) -> duration_days for all jump links."""
    durations = {}
    for jl in get_all_jump_links():
        n1, n2 = jl.system1.name, jl.system2.name
        durations[(n1, n2)] = jl.duration_days
        durations[(n2, n1)] = jl.duration_days
    return durations


def canonical_path(
    start: Union[str, "System"],
    end: Union[str, "System"],
    max_difficulty: Union[JumpDifficulty, str],
) -> Optional[tuple[list[str], int]]:
    """
    Return the canonical path from start to end using only jumps of permitted
    difficulty or easier, along with the total duration in days.

    Tie-breaking: shortest length -> fewest hard jumps ->
    fewest moderate jumps -> lexicographically last path.

    start, end: system name (str) or System instance.
    max_difficulty: maximum difficulty allowed per jump (Hard = allow all).
    Returns (path, duration_days) or None if no path exists.
    """
    start_name = start.name if isinstance(start, System) else start
    end_name = end.name if isinstance(end, System) else end
    if start_name == end_name:
        return [start_name], 0
    if isinstance(max_difficulty, str):
        max_difficulty = JumpDifficulty.from_str(max_difficulty)
    max_level = _difficulty_level(max_difficulty)

    by_name = {s.name: s for s in get_systems()}
    if start_name not in by_name or end_name not in by_name:
        return None

    durations = _build_link_duration_map()
    neighbors: dict[str, list[tuple[str, JumpDifficulty]]] = {n: [] for n in by_name}
    for jl in get_all_jump_links():
        d = jl.difficulty
        if _difficulty_level(d) <= max_level:
            n1, n2 = jl.system1.name, jl.system2.name
            neighbors[n1].append((n2, d))
            neighbors[n2].append((n1, d))

    current: dict[str, tuple[int, int, list[str]]] = {
        start_name: (0, 0, [start_name])
    }
    visited_length: dict[str, int] = {start_name: 0}

    while current:
        if end_name in current:
            path = current[end_name][2]
            return path, PathToGateway.duration_of(path, durations)
        next_level: dict[str, tuple[int, int, list[str]]] = {}
        for node, (h, m, path) in current.items():
            for nb, diff in neighbors[node]:
                new_path = path + [nb]
                new_len = len(new_path) - 1
                if nb in visited_length and visited_length[nb] < new_len:
                    continue
                new_h = h + (1 if diff == JumpDifficulty.Hard else 0)
                new_m = m + (1 if diff == JumpDifficulty.Moderate else 0)
                if nb not in next_level:
                    next_level[nb] = (new_h, new_m, new_path)
                    if nb not in visited_length:
                        visited_length[nb] = new_len
                else:
                    old_h, old_m, old_path = next_level[nb]
                    if (new_h < old_h) or (
                        new_h == old_h and new_m < old_m
                    ) or (
                        new_h == old_h and new_m == old_m and tuple(new_path) > tuple(old_path)
                    ):
                        next_level[nb] = (new_h, new_m, new_path)
        current = next_level

    return None


def _dominates(
    la: int, da: int,
    lb: int, db: int,
) -> bool:
    """True if (la, da) dominates (lb, db): no worse on either and strictly better on one."""
    return la <= lb and da <= db and (la < lb or da < db)


def _compute_paths_from_gateway(
    gateway: System,
    jump_links: list[JumpLink],
) -> dict[str, list[tuple[int, int, int, list[str]]]]:
    """Every worthwhile route from one gateway to every system it can reach.

    A breadth-first sweep out from `gateway`. For each system it keeps only the *non-dominated* routes:
    one route beats another when it is no worse on both hop count and hardest jump and strictly better on
    at least one (see `_dominates`), so a longer path survives only if it is gentler, and a harder path
    only if it is shorter. Among routes that tie on (length, hardest jump) it keeps the lexicographically
    last path -- the same arbitrary-but-stable tie-break `canonical_path` uses. Duration is carried along
    on each route but is never a ranking key.

    Returns `system_name -> [(length, max_difficulty_level, duration_days, path), ...]`, each list already
    pruned to that non-dominated frontier. `_compute_gateway_paths` turns these into `PathToGateway`s."""
    by_name = {s.name: s for s in get_systems()}
    durations = _build_link_duration_map()
    neighbors: dict[str, list[tuple[str, JumpDifficulty]]] = {name: [] for name in by_name}
    for jl in jump_links:
        n1, n2, d = jl.system1.name, jl.system2.name, jl.difficulty
        neighbors[n1].append((n2, d))
        neighbors[n2].append((n1, d))
    best: dict[str, list[tuple[int, int, int, list[str]]]] = {}
    from collections import deque
    q: deque[tuple[str, int, int, int, list[str]]] = deque([(gateway.name, 0, 0, 0, [gateway.name])])
    best[gateway.name] = [(0, 0, 0, [gateway.name])]
    while q:
        name, length, max_d, dur, path = q.popleft()
        if name in best and not any((length, max_d) == (b[0], b[1]) for b in best[name]):
            continue
        for nb, diff in neighbors[name]:
            new_len = length + 1
            new_max_d = max(max_d, _difficulty_level(diff))
            new_dur = dur + durations.get((name, nb), 0)
            new_path = path + [nb]
            if nb not in best:
                best[nb] = []
            if any(_dominates(b[0], b[1], new_len, new_max_d) for b in best[nb]):
                continue
            best[nb] = [b for b in best[nb] if not _dominates(new_len, new_max_d, b[0], b[1])]
            same = [b for b in best[nb] if (b[0], b[1]) == (new_len, new_max_d)]
            if same:
                existing_path = same[0][3]
                if tuple(new_path) > tuple(existing_path):
                    best[nb] = [b for b in best[nb] if (b[0], b[1]) != (new_len, new_max_d)]
                    best[nb].append((new_len, new_max_d, new_dur, new_path))
                    q.append((nb, new_len, new_max_d, new_dur, new_path))
            else:
                best[nb].append((new_len, new_max_d, new_dur, new_path))
                q.append((nb, new_len, new_max_d, new_dur, new_path))
    return best


def _level_to_difficulty(level: int) -> str:
    return ["soft", "medium", "hard"][level] if 0 <= level <= 2 else "hard" # TODO: This feels redundant with _difficulty level. Should both this and that live in enums.py?


# The six sector gateways, in a fixed order, keyed the way the store and `info_json` refer to them.
_GATEWAY_KEYS = ("sol", "polaris", "canopus", "antares", "hyades", "alcyone")


def _compute_gateway_paths(jump_links: list[JumpLink]) -> dict[str, dict[str, list[PathToGateway]]]:
    """Precompute, for every system, the non-dominated routes to each sector gateway.

    Returns `system_name -> {gateway_key -> [PathToGateway, ...]}`. The `"gateway_system"` key holds the
    routes out of a system's *own* cluster -- what `info_json` shows an outer-sector player. The graph
    owns this derived data, so `System` stays pure node data and knows nothing about routes."""
    systems = get_systems()
    by_name = {s.name: s for s in systems}
    store: dict[str, dict[str, list[PathToGateway]]] = {
        s.name: {key: [] for key in ("gateway_system", *_GATEWAY_KEYS)}
        for s in systems
    }
    gateways = ["Sol", "Polaris", "Canopus", "Antares", "Ain", "Alcyone"]
    gateway_systems = [by_name.get(g) for g in gateways]
    for gw, key in zip(gateway_systems, _GATEWAY_KEYS):
        if gw is None:
            continue
        paths_map = _compute_paths_from_gateway(gw, jump_links)
        for s in systems:
            if s.name == gw.name:
                continue
            if s.name not in paths_map:
                continue
            for length, max_level, dur, path in paths_map[s.name]:
                store[s.name][key].append(PathToGateway(
                    minimum_difficulty=_level_to_difficulty(max_level),
                    length=length,
                    duration_days=dur,
                    path=list(reversed(path)),
                ))
    cluster_gateway = {
        StarClusters.INNER_SYSTEMS: "sol",
        StarClusters.ANTARES: "antares",
        StarClusters.CANOPUS: "canopus",
        StarClusters.POLARIS: "polaris",
        StarClusters.HYADES: "hyades",
        StarClusters.PLEIADES: "alcyone",
    }
    for s in systems:
        key = cluster_gateway.get(s.cluster)
        if key is None:
            continue
        store[s.name]["gateway_system"].extend(store[s.name][key])
    return store


# Computed once, at import: there are 126 systems and the AI asks for these paths constantly.
_GATEWAY_PATHS: dict[str, dict[str, list[PathToGateway]]] = _compute_gateway_paths(ALL_JUMP_LINKS)


def _paths_to_json(paths: list[PathToGateway]) -> list[dict]:
    return [
        {"minimum_difficulty": p.minimum_difficulty, "length": p.length, "duration_days": p.duration_days, "path": p.path}
        for p in paths
    ]


def info_json(system: System) -> str:
    """Everything the AI is told about the system you are currently in, as JSON.

    Held by the "Current system info" tracked item. Unlike the lore entry (`System.to_lore_json`) this
    carries the full descriptions, every neighbouring system across the graph, and the precomputed routes
    out of the cluster -- because there is only ever one of these in play, for the system you stand in."""
    info: dict = {
        "name": system.name,
        "cluster": system.cluster.value,
        "star": system.star,
        "description": system.description,
        "population": system.population,
        "stellar_objects": [
            {"name": obj.name, "description": obj.desc, "population": obj.population}
            for obj in system.stellar_objects
        ],
    }

    neighbors = []
    for jl in ALL_JUMP_LINKS:
        if jl.system1.name == system.name:
            other = jl.system2
        elif jl.system2.name == system.name:
            other = jl.system1
        else:
            continue
        neighbors.append({
            "name": other.name,
            "cluster": other.cluster.value,
            "jump_difficulty": jl.difficulty.value,
            "short_description": other.short_description or other.description,
        })
    info["neighboring_systems"] = neighbors

    paths = _GATEWAY_PATHS[system.name]
    if system.cluster == StarClusters.INNER_SYSTEMS:
        info["paths_to_polaris"] = _paths_to_json(paths["polaris"])
        info["paths_to_canopus"] = _paths_to_json(paths["canopus"])
        info["paths_to_antares"] = _paths_to_json(paths["antares"])
        info["paths_to_hyades"] = _paths_to_json(paths["hyades"])
        info["paths_to_pleiades"] = _paths_to_json(paths["alcyone"])
    else:
        cluster_name = system.cluster.value.lower().replace(" ", "_")
        info[f"paths_to_leave_{cluster_name}"] = _paths_to_json(paths["gateway_system"])
    return json.dumps(info, separators=(",", ":"))


def paths_json(system: System, max_difficulty: JumpDifficulty) -> str:
    """Canonical paths from `system` to every other system in its cluster, using only jumps up to the
    given difficulty. A JSON string, held by the "Current sector paths" tracked item."""
    cluster_systems = [s for s in get_systems() if s.cluster == system.cluster and s.name != system.name]
    paths = []
    for dest in sorted(cluster_systems, key=lambda s: s.name):
        result = canonical_path(system, dest, max_difficulty)
        if result is not None:
            path, duration_days = result
            paths.append({
                "destination": dest.name,
                "length": len(path) - 1,
                "duration_days": duration_days,
                "path": path,
            })
    return json.dumps(paths, separators=(",", ":"))


# ==== Adjacency ==================================================================================

def adjacent_jumps(system_name: str) -> list[tuple[str, str]]:
    """The (destination, difficulty) pairs leading out of one system, in a stable sorted order.

    Sorted, and that matters: the six jump slots on the sheet are numbered, and slot 3 has to mean the
    same jump point on the turn you arrive somewhere as it does ten turns later when you decide to leave.
    The jump-link table is written in whatever order was convenient; alphabetical is arbitrary too, but it
    is *the same* arbitrary every time. `player_details` pours these into the six jump slots on arrival."""
    links: list[tuple[str, str]] = []
    for link in get_all_jump_links():
        if link.system1.name == system_name:
            links.append((link.system2.name, link.difficulty.value))
        elif link.system2.name == system_name:
            links.append((link.system1.name, link.difficulty.value))
    links.sort()
    return links
