#!/usr/bin/env python3
"""Generate a 2D map of Starlit star systems and jump links.

Run from repo root:
  python3 worlds/starlit/generate_map.py

Writes SVG to generated/starlit_map.svg. Layout uses NetworkX Kamada-Kawai when
available (pip install networkx); otherwise falls back to radial BFS / inner star.
For PNG output, install matplotlib and set USE_MATPLOTLIB=1.
"""

from __future__ import annotations

import argparse
import math
import os
import sys
from pathlib import Path

# Run as a script from anywhere: put worlds/ on the path so `starlit_frontiers` imports as a package.
_worlds_dir = Path(__file__).resolve().parents[1]
if str(_worlds_dir) not in sys.path:
    sys.path.insert(0, str(_worlds_dir))

from starlit_frontiers.systems import get_systems, get_all_jump_links
from starlit_frontiers.navigation import canonical_path
from starlit_frontiers.enums import StarClusters, JumpDifficulty

try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    nx = None
    HAS_NETWORKX = False

USE_MATPLOTLIB = os.environ.get("USE_MATPLOTLIB", "").strip().lower() in ("1", "true", "yes")

# Cluster colors: standard (normal systems) and variant (Sol / gateway)
CLUSTER_STANDARD = {
    StarClusters.INNER_SYSTEMS: "#4a90d9",   # blue
    StarClusters.ANTARES:      "#c23a2b",   # red
    StarClusters.CANOPUS:      "#15803d",   # dark green
    StarClusters.HYADES:       "#d4a017",   # gold / orange
    StarClusters.POLARIS:      "#7c3aed",   # purple
    StarClusters.PLEIADES:     "#0891b2",   # cyan / teal
}
CLUSTER_VARIANT = {
    StarClusters.INNER_SYSTEMS: "#22d3ee",   # cyan
    StarClusters.ANTARES:      "#ec4899",   # pink
    StarClusters.CANOPUS:      "#4ade80",   # light green
    StarClusters.HYADES:       "#eab308",   # yellow
    StarClusters.POLARIS:      "#a78bfa",   # violet
    StarClusters.PLEIADES:     "#67e8f9",   # light cyan
}
# Uninhabited systems (system_is_populated=False)
UNINHABITED_FILL = "#64748b"
# Fallback for unknown cluster
CLUSTER_FALLBACK = "#64748b"
# Gateway name -> cluster (for variant color)
GATEWAY_CLUSTER = {
    "Sol": StarClusters.INNER_SYSTEMS,
    "Polaris": StarClusters.POLARIS,
    "Canopus": StarClusters.CANOPUS,
    "Antares": StarClusters.ANTARES,
    "Ain": StarClusters.HYADES,
    "Alcyone": StarClusters.PLEIADES,
}

# Edge color by jump difficulty
DIFFICULTY_COLOR = {
    JumpDifficulty.Soft:     "#22c55e",
    JumpDifficulty.Moderate: "#eab308",
    JumpDifficulty.Hard:     "#ef4444",
}

# Gateway systems (one per cluster) -- drawn as diamonds on the map
GATEWAY_SYSTEMS = {"Sol", "Polaris", "Canopus", "Antares", "Ain", "Alcyone"}


def distance_to_gateway_by_system(by_name: dict, adj: dict) -> dict[str, int]:
    """For each system, return minimum hop distance to its cluster gateway (Sol for inner, else sector gateway)."""
    gateways = list(GATEWAY_CLUSTER.keys())
    bfs_from = {}
    for gw in gateways:
        if gw in adj:
            bfs_from[gw] = distance_from_sol_bfs(adj, center=gw)
    out = {}
    for name, s in by_name.items():
        cluster = s.cluster
        gw = "Sol" if cluster == StarClusters.INNER_SYSTEMS else SECTOR_GATEWAY.get(cluster)
        if gw and gw in bfs_from and name in bfs_from[gw]:
            out[name] = bfs_from[gw][name]
        else:
            out[name] = 0
    return out

# Inner map: distance-from-Sol gradient (blue = close, deep purple = far)
DISTANCE_COLOR_NEAR = (0x25, 0x63, 0xEB)   # blue-600
DISTANCE_COLOR_FAR  = (0x4C, 0x1D, 0x95)   # violet-900


def build_graph_data():
    """Return (by_name, nodes_by_cluster, edges, adj). adj[name] = set of neighbor names."""
    systems = get_systems()
    links = get_all_jump_links()
    by_name = {s.name: s for s in systems}
    nodes_by_cluster = {}
    for s in systems:
        c = s.cluster or "Unknown"
        nodes_by_cluster.setdefault(c, []).append(s.name)
    for c in nodes_by_cluster:
        nodes_by_cluster[c].sort()
    edges = [(jl.system1.name, jl.system2.name, jl.difficulty) for jl in links]
    adj = {}
    for u, v, _ in edges:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    for s in systems:
        adj.setdefault(s.name, set())
    return by_name, nodes_by_cluster, edges, adj


# ---- Radial BFS layout from Sol ----

# Minimum distance between node centers (dot + label clearance)
MIN_STEP = 72
# Extra nudge iterations to reduce overlap
NUDGE_ITERATIONS = 25

# Five gateways (excluding Sol) for inner star layout -- equally spaced around Sol
OTHER_GATEWAYS = ["Polaris", "Canopus", "Antares", "Ain", "Alcyone"]
STAR_R0 = 220  # radius for gateway positions in star layout

# Other sectors: cluster -> gateway (center of sector map)
SECTOR_GATEWAY = {
    StarClusters.ANTARES: "Antares",
    StarClusters.CANOPUS: "Canopus",
    StarClusters.HYADES: "Ain",
    StarClusters.POLARIS: "Polaris",
    StarClusters.PLEIADES: "Alcyone",
}
# Combined map: inner layout scale (leave room for outer sectors in arcs)
INNER_SCALE = 0.55
# Distance from gateway per BFS ring for sector nodes in combined map
SECTOR_STEP = 70
# Half-width of arc (degrees) for each sector around its gateway direction
ARC_HALF_DEG = 32
SECTOR_SLUG = {
    StarClusters.ANTARES: "antares",
    StarClusters.CANOPUS: "canopus",
    StarClusters.HYADES: "hyades",
    StarClusters.POLARIS: "polaris",
    StarClusters.PLEIADES: "pleiades",
}


def _shortest_paths_from_sol(adj: dict, center: str = "Sol"):
    """BFS from center; return (parent dict, distance dict)."""
    parent = {center: None}
    dist = {center: 0}
    q = [center]
    while q:
        u = q.pop(0)
        d = dist[u] + 1
        for v in adj.get(u, set()):
            if v not in dist:
                dist[v] = d
                parent[v] = u
                q.append(v)
    return parent, dist


def _path_to_gateway(parent: dict, gateway: str) -> list[str]:
    """Return path from Sol to gateway (list [Sol, ..., gateway])."""
    out = []
    u = gateway
    while u is not None:
        out.append(u)
        u = parent.get(u)
    out.reverse()
    return out


def _canonical_path_sol_to_gateway(gateway_name: str) -> list[str] | None:
    """Return the canonical path Sol -> gateway (shortest; then fewest hard/mod; lex last)."""
    return canonical_path("Sol", gateway_name, JumpDifficulty.Hard)


def layout_inner_star(adj: dict, center: str = "Sol"):
    """
    Inner-systems star: only Sol, the five gateways, and systems on the canonical shortest path
    Sol -> gateway (same paths as the route list: shortest length, then easiest difficulty).
    Each arm has waypoints evenly spaced (R0/3, 2*R0/3, R0 for 3-hop path).
    Returns dict name -> (x, y). No other nodes are placed.
    """
    if center not in adj:
        center = next(iter(adj))
    pos = {}
    n_gw = len(OTHER_GATEWAYS)

    # 1) Sol at origin; five gateways at radius R0, angles 72 degrees apart (first at -90 degrees)
    pos[center] = (0.0, 0.0)
    for i, gw in enumerate(OTHER_GATEWAYS):
        angle = math.radians(-90 + i * 360 / n_gw)
        pos[gw] = (STAR_R0 * math.cos(angle), -STAR_R0 * math.sin(angle))

    # 2) For each gateway, get canonical path Sol -> gateway from systems' paths_to_sol; place waypoints evenly.
    path_positions = {}  # name -> list of (angle, radius_fraction)
    for i, gw in enumerate(OTHER_GATEWAYS):
        path = _canonical_path_sol_to_gateway(gw)
        if not path or len(path) < 2:
            continue
        L = len(path) - 1  # number of hops
        angle = math.radians(-90 + i * 360 / n_gw)
        for k, name in enumerate(path):
            if name == center or name == gw:
                continue
            frac = k / L
            path_positions.setdefault(name, []).append((angle, frac))

    for name, placements in path_positions.items():
        if name in pos:
            continue
        avg_angle = sum(p[0] for p in placements) / len(placements)
        avg_frac = sum(p[1] for p in placements) / len(placements)
        r = STAR_R0 * avg_frac
        pos[name] = (r * math.cos(avg_angle), -r * math.sin(avg_angle))

    return pos


def _angle_between_vectors(v1: tuple[float, float], v2: tuple[float, float]) -> float:
    """Angle in [0, pi] radians between two 2D vectors."""
    x1, y1 = v1
    x2, y2 = v2
    d1 = math.hypot(x1, y1)
    d2 = math.hypot(x2, y2)
    if d1 < 1e-9 or d2 < 1e-9:
        return math.pi
    dot = x1 * x2 + y1 * y2
    cos_a = max(-1.0, min(1.0, dot / (d1 * d2)))
    return math.acos(cos_a)


def _min_angle_for_placement(
    px: float,
    py: float,
    adj_on_map: list,
    pos: dict,
    adj: dict,
    on_map: set,
) -> float:
    """
    For a candidate position (px, py) of a new node P with on-map neighbors adj_on_map,
    compute the minimum angle among:
    - angles at P between pairs of links P->A, P->B (new lines between themselves);
    - angles at each neighbor A between the new link A->P and each existing link A->Q (Q on map).
    Returns that minimum in radians, or -1 if P is too close to any neighbor.
    """
    for a in adj_on_map:
        ax, ay = pos[a]
        if math.hypot(px - ax, py - ay) < MIN_STEP:
            return -1.0
    angles = []
    for i, a in enumerate(adj_on_map):
        ax, ay = pos[a]
        for b in adj_on_map[i + 1 :]:
            bx, by = pos[b]
            v1 = (ax - px, ay - py)
            v2 = (bx - px, by - py)
            angles.append(_angle_between_vectors(v1, v2))
        for q in adj.get(a, set()) & on_map:
            qx, qy = pos[q]
            v1 = (px - ax, py - ay)
            v2 = (qx - ax, qy - ay)
            angles.append(_angle_between_vectors(v1, v2))
    return min(angles) if angles else math.pi


def layout_inner_star_then_rest(adj: dict, center: str = "Sol"):
    """
    Full inner map: place the gateway star first (Sol + 5 gateways + path waypoints),
    then add remaining systems iteratively without moving any star positions.
    """
    # 1) Star positions are fixed (never moved)
    pos = layout_inner_star(adj, center=center)
    fixed = set(pos.keys())
    all_nodes = set(adj.keys())
    on_map = set(pos.keys())

    # 2) Iteratively add remaining nodes: most adjacent on map, tie-break fewest not on map
    while True:
        candidates = [n for n in all_nodes - on_map if any(m in on_map for m in adj[n])]
        if not candidates:
            break

        def score(n):
            adj_on = sum(1 for m in adj[n] if m in on_map)
            adj_off = sum(1 for m in adj[n] if m not in on_map)
            return (adj_on, -adj_off)

        best = max(candidates, key=score)
        adj_on_map = [m for m in adj[best] if m in pos]
        if len(adj_on_map) >= 2:
            # Place so the smallest angle (new-new and new-existing) is maximized
            cx = sum(pos[a][0] for a in adj_on_map) / len(adj_on_map)
            cy = sum(pos[a][1] for a in adj_on_map) / len(adj_on_map)
            pair_dists = [
                math.hypot(pos[a][0] - pos[b][0], pos[a][1] - pos[b][1])
                for i, a in enumerate(adj_on_map)
                for b in adj_on_map[i + 1 :]
            ]
            max_pair_dist = max(pair_dists) if pair_dists else MIN_STEP * 2
            r_min = MIN_STEP
            r_max = max(2 * max_pair_dist, MIN_STEP * 3)
            best_min_angle = _min_angle_for_placement(
                cx, cy, adj_on_map, pos, adj, on_map
            )
            best_xy = (cx, cy)
            n_radii = 12
            n_angles = 72
            for ri in range(n_radii + 1):
                r = r_min + (r_max - r_min) * (ri / n_radii) if n_radii else r_min
                for ti in range(n_angles):
                    t = 2 * math.pi * ti / n_angles
                    px = cx + r * math.cos(t)
                    py = cy - r * math.sin(t)
                    min_ang = _min_angle_for_placement(
                        px, py, adj_on_map, pos, adj, on_map
                    )
                    if min_ang > best_min_angle:
                        best_min_angle = min_ang
                        best_xy = (px, py)
            pos[best] = best_xy
        else:
            # One adjacent: place radially outward from it (from Sol)
            (other,) = adj_on_map
            ox, oy = pos[other]
            dist_o = math.hypot(ox, oy)
            if dist_o < 1e-6:
                dx, dy = 1.0, 0.0
            else:
                dx, dy = ox / dist_o, oy / dist_o
            pos[best] = (ox + MIN_STEP * dx, oy + MIN_STEP * dy)
        on_map.add(best)

    # 3) Nudge apart overlapping nodes, but only move non-fixed nodes (never move the star)
    names = [n for n in pos if n not in fixed]
    for _ in range(NUDGE_ITERATIONS):
        moved = False
        for i, a in enumerate(names):
            ax, ay = pos[a]
            for b in names[i + 1 :] + list(fixed):
                if a == b:
                    continue
                bx, by = pos[b]
                d = math.hypot(ax - bx, ay - by)
                if d < MIN_STEP and d > 1e-6:
                    nudge = 0.5 * (MIN_STEP - d) / d
                    dx, dy = (ax - bx) * nudge, (ay - by) * nudge
                    # Only move non-fixed node(s)
                    pos[a] = (ax + dx, ay + dy)
                    if b not in fixed:
                        pos[b] = (bx - dx, by - dy)
                    ax, ay = pos[a]
                    moved = True
        if not moved:
            break
    return pos


def layout_radial_bfs(adj: dict, center: str = "Sol"):
    """Place nodes with Sol at centre; each ring = nodes adjacent to already-placed. Returns dict name -> (x, y)."""
    if center not in adj:
        center = next(iter(adj))
    pos = {}
    parent = {}
    order = [center]
    q = [center]
    parent[center] = None
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                order.append(v)
                q.append(v)
    # Level 0: centre
    pos[center] = (0.0, 0.0)
    # Level 1: neighbours of centre on a circle
    level1 = [n for n in order if n != center and parent[n] == center]
    n1 = len(level1)
    for i, name in enumerate(level1):
        angle = 2 * math.pi * i / n1 - math.pi / 2
        pos[name] = (MIN_STEP * math.cos(angle), -MIN_STEP * math.sin(angle))
    # Levels 2+: place each node relative to parent, then nudge apart
    placed = {center} | set(level1)
    children_of = {}
    for name in order:
        if name == center:
            continue
        p = parent[name]
        children_of.setdefault(p, []).append(name)
    for name in order:
        if name in placed:
            continue
        placed.add(name)
        p = parent[name]
        px, py = pos[p]
        dist_p = math.hypot(px, py)
        if dist_p < 1e-6:
            dx, dy = 1.0, 0.0
        else:
            dx, dy = px / dist_p, py / dist_p
        siblings = children_of.get(p, [])
        idx = siblings.index(name)
        n_sib = len(siblings)
        # Fan siblings: first straight out, then spread by angle
        if n_sib == 1:
            angle_offset = 0.0
        else:
            spread = 0.6
            angle_offset = (idx - (n_sib - 1) / 2) * spread
        cos_a, sin_a = math.cos(angle_offset), math.sin(angle_offset)
        tx = dx * cos_a - dy * sin_a
        ty = dx * sin_a + dy * cos_a
        cx = px + MIN_STEP * tx
        cy = py + MIN_STEP * ty
        # Nudge away from any overlapping placed node
        for _ in range(12):
            nudged = False
            for other, (ox, oy) in list(pos.items()):
                if other == name:
                    continue
                d = math.hypot(cx - ox, cy - oy)
                if d < MIN_STEP and d > 1e-6:
                    nudge = (MIN_STEP - d) / d
                    cx += (cx - ox) * nudge
                    cy += (cy - oy) * nudge
                    nudged = True
            if not nudged:
                break
        pos[name] = (cx, cy)
    # Global nudge: push apart any pair too close
    names = list(pos.keys())
    for _ in range(NUDGE_ITERATIONS):
        moved = False
        for i, a in enumerate(names):
            ax, ay = pos[a]
            for b in names[i + 1 :]:
                bx, by = pos[b]
                d = math.hypot(ax - bx, ay - by)
                if d < MIN_STEP and d > 1e-6:
                    nudge = 0.5 * (MIN_STEP - d) / d
                    dx, dy = (ax - bx) * nudge, (ay - by) * nudge
                    pos[a] = (ax + dx, ay + dy)
                    pos[b] = (bx - dx, by - dy)
                    ax, ay = pos[a]
                    moved = True
        if not moved:
            break
    return pos


def layout_combined(
    by_name: dict,
    nodes_by_cluster: dict,
    edges: list,
    adj: dict,
    center: str = "Sol",
) -> dict[str, tuple[float, float]]:
    """
    Single map with all systems: lay out inner systems first (with room at edges),
    then place each outer sector in the arc corresponding to its gateway.
    """
    # 1) Inner + gateways layout (existing star-then-rest)
    _, _, _, adj_inner = filter_inner_plus_gateways(
        by_name, nodes_by_cluster, edges, adj
    )
    pos = layout_inner_star_then_rest(adj_inner, center=center)
    # Scale inner down so outer sectors fit in arcs around the edges
    for name in list(pos.keys()):
        x, y = pos[name]
        pos[name] = (x * INNER_SCALE, y * INNER_SCALE)

    arc_half_rad = math.radians(ARC_HALF_DEG)

    # 2) Place each outer sector in its gateway's arc
    for cluster, gateway in SECTOR_GATEWAY.items():
        sector_names = set(nodes_by_cluster.get(cluster, []))
        if gateway not in pos or not sector_names:
            continue
        sector_others = sector_names - {gateway}
        if not sector_others:
            continue
        # Sector subgraph
        adj_sector = {n: adj.get(n, set()) & sector_names for n in sector_names}
        _, dist = _shortest_paths_from_sol(adj_sector, gateway)
        # Arc center = direction from Sol to gateway
        gx, gy = pos[gateway]
        arc_center = math.atan2(-gy, gx)
        # Group by distance from gateway, then spread angles within arc
        by_dist = {}
        for n in sector_others:
            d = dist.get(n, 999)
            by_dist.setdefault(d, []).append(n)
        for d in sorted(by_dist.keys()):
            names_at_d = sorted(by_dist[d])
            n = len(names_at_d)
            for i, name in enumerate(names_at_d):
                frac = (i + 1) / (n + 1)
                angle = arc_center - arc_half_rad + (2 * arc_half_rad * frac)
                r = d * SECTOR_STEP
                x = gx + r * math.cos(angle)
                y = gy - r * math.sin(angle)
                pos[name] = (x, y)

    return pos


def fit_canvas(pos, margin=100):
    """Translate and scale pos so all points fit in a canvas with margin. Returns (pos, width, height)."""
    if not pos:
        return pos, 800, 600
    xs = [x for x, _ in pos.values()]
    ys = [y for _, y in pos.values()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    w = max_x - min_x + 2 * margin
    h = max_y - min_y + 2 * margin
    out = {}
    for name, (x, y) in pos.items():
        out[name] = (x - min_x + margin, y - min_y + margin)
    return out, int(math.ceil(w)), int(math.ceil(h))


# Target extent for Kamada-Kawai so fit_canvas produces a spread-out map (fit_canvas only translates)
KAMADA_KAWAI_SCALE = 400
# Combined map has many more nodes; scale layout up so labels don't overlap
COMBINED_MAP_SCALE = 4.0
# Scale all maps up by this factor (canvas and coordinates) for readability
MAP_SCALE = 1.5


def _build_nx_graph(adj: dict, edges: list, weighted: bool = False):
    """Build a NetworkX Graph from adjacency and edge data.
    
    If weighted=True, edges get a 'weight' attribute based on difficulty:
    Soft=1.0, Moderate=2.0, Hard=3.0 (used as desired distance in Kamada-Kawai).
    """
    _DIFFICULTY_DIST = {"Soft": 1.0, "Moderate": 2.0, "Hard": 3.0}
    G = nx.Graph()
    nodes = sorted(adj.keys())
    G.add_nodes_from(nodes)
    seen = set()
    for u, v, diff in edges:
        if u not in adj or v not in adj:
            continue
        key = (min(u, v), max(u, v))
        if key not in seen:
            seen.add(key)
            if weighted:
                G.add_edge(u, v, weight=_DIFFICULTY_DIST.get(diff, 2.0))
            else:
                G.add_edge(u, v)
    return G


def _scale_pos(pos: dict, target_scale: float) -> dict[str, tuple[float, float]]:
    """Scale and flip positions to fit target extent, with y flipped for SVG."""
    xs = [float(p[0]) for p in pos.values()]
    ys = [float(p[1]) for p in pos.values()]
    extent_x = max(xs) - min(xs) if xs else 1.0
    extent_y = max(ys) - min(ys) if ys else 1.0
    extent = max(extent_x, extent_y, 1e-6)
    scale = target_scale / extent
    return {
        name: (float(p[0]) * scale, -float(p[1]) * scale)
        for name, p in pos.items()
    }


def layout_spring(adj: dict, edges: list) -> dict[str, tuple[float, float]] | None:
    """Spring (Fruchterman-Reingold) layout for sector and inner maps."""
    if not HAS_NETWORKX:
        return None
    G = _build_nx_graph(adj, edges)
    if G.order() == 0:
        return None
    pos = nx.spring_layout(G, iterations=500, seed=42)
    return _scale_pos(pos, KAMADA_KAWAI_SCALE)


def layout_kamada_kawai(adj: dict, edges: list) -> dict[str, tuple[float, float]] | None:
    """Kamada-Kawai layout for the combined map, with soft links shorter than hard links."""
    if not HAS_NETWORKX:
        return None
    G = _build_nx_graph(adj, edges, weighted=True)
    if G.order() == 0:
        return None
    dist = dict(nx.shortest_path_length(G, weight="weight"))
    pos = nx.kamada_kawai_layout(G, dist=dist, scale=1.0)
    return _scale_pos(pos, KAMADA_KAWAI_SCALE)


def spread_overlapping_nodes(
    pos: dict[str, tuple[float, float]],
    min_dist: float = 60.0,
    iterations: int = 50,
) -> dict[str, tuple[float, float]]:
    """Push apart nodes that are closer than min_dist to reduce label/edge overlap."""
    pos = {k: list(v) for k, v in pos.items()}
    names = list(pos.keys())
    n = len(names)
    for _ in range(iterations):
        moved = False
        for i in range(n):
            for j in range(i + 1, n):
                ax, ay = pos[names[i]]
                bx, by = pos[names[j]]
                dx = bx - ax
                dy = by - ay
                dist = math.sqrt(dx * dx + dy * dy)
                if dist < min_dist and dist > 0.01:
                    force = (min_dist - dist) / 2.0
                    ux, uy = dx / dist, dy / dist
                    pos[names[i]][0] -= ux * force * 0.5
                    pos[names[i]][1] -= uy * force * 0.5
                    pos[names[j]][0] += ux * force * 0.5
                    pos[names[j]][1] += uy * force * 0.5
                    moved = True
                elif dist < 0.01:
                    pos[names[j]][0] += min_dist * 0.5
                    moved = True
        if not moved:
            break
    return {k: tuple(v) for k, v in pos.items()}


def _point_to_segment_dist(px, py, ax, ay, bx, by):
    """Return (distance, nearest_x, nearest_y) from point (px,py) to segment (ax,ay)-(bx,by)."""
    abx, aby = bx - ax, by - ay
    ab_len_sq = abx * abx + aby * aby
    if ab_len_sq < 1e-12:
        dx, dy = px - ax, py - ay
        return math.sqrt(dx * dx + dy * dy), ax, ay
    t = max(0.0, min(1.0, ((px - ax) * abx + (py - ay) * aby) / ab_len_sq))
    nx_, ny_ = ax + t * abx, ay + t * aby
    dx, dy = px - nx_, py - ny_
    return math.sqrt(dx * dx + dy * dy), nx_, ny_


def push_nodes_from_edges(
    pos: dict[str, tuple[float, float]],
    edges: list[tuple[str, str, ...]],
    min_dist: float = 40.0,
    iterations: int = 50,
) -> dict[str, tuple[float, float]]:
    """Push nodes away from edges they are not endpoints of."""
    pos = {k: list(v) for k, v in pos.items()}
    edge_pairs = []
    seen = set()
    for e in edges:
        u, v = e[0], e[1]
        if u not in pos or v not in pos:
            continue
        key = (min(u, v), max(u, v))
        if key not in seen:
            seen.add(key)
            edge_pairs.append((u, v))
    names = list(pos.keys())
    for _ in range(iterations):
        moved = False
        for node in names:
            px, py = pos[node]
            for u, v in edge_pairs:
                if node == u or node == v:
                    continue
                ax, ay = pos[u]
                bx, by = pos[v]
                dist, cx, cy = _point_to_segment_dist(px, py, ax, ay, bx, by)
                if dist < min_dist and dist > 0.01:
                    force = (min_dist - dist) * 0.3
                    dx, dy = px - cx, py - cy
                    ux, uy = dx / dist, dy / dist
                    pos[node][0] += ux * force
                    pos[node][1] += uy * force
                    moved = True
                elif dist < 0.01:
                    pos[node][1] += min_dist * 0.3
                    moved = True
        if not moved:
            break
    return {k: tuple(v) for k, v in pos.items()}


def escape_svg(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def print_sector_table(names: set, adj: dict, title: str) -> None:
    """Print link count table for systems in names (same format as inner systems table)."""
    neighbours = {n: [] for n in names}
    for u in names:
        for v in adj.get(u, set()):
            neighbours[u].append(v)
    rows = sorted(neighbours.items(), key=lambda x: (-len(x[1]), x[0]))
    print(f"\n{title}")
    print("Count | System              | Linked systems")
    print("------|---------------------|" + "-" * 80)
    for name, nbs in rows:
        count = len(nbs)
        nbs_str = ", ".join(sorted(set(nbs)))
        print(f"  {count:2d}  | {name:<19} | {nbs_str}")
    print(f"\nTotal: {len(names)} systems")


def write_svg(
    by_name: dict,
    edges: list,
    adj: dict,
    out_path: Path,
    distance_from_sol: dict[str, int] | None = None,
    center: str = "Sol",
    pos_override: dict[str, tuple[float, float]] | None = None,
    distance_from_center: dict[str, int] | None = None,
):
    if pos_override is not None:
        pos = dict(pos_override)
    elif HAS_NETWORKX:
        pos = layout_spring(adj, edges)
        if pos is None:
            pos = (
                layout_inner_star_then_rest(adj, center="Sol")
                if distance_from_sol is not None
                else layout_radial_bfs(adj, center=center)
            )
    elif distance_from_sol is not None:
        pos = layout_inner_star_then_rest(adj, center="Sol")
    else:
        pos = layout_radial_bfs(adj, center=center)
    pos, width, height = fit_canvas(pos, margin=100)
    legend_h = 70
    height += legend_h
    # Scale all maps up by MAP_SCALE for readability
    for name in pos:
        x, y = pos[name]
        pos[name] = (x * MAP_SCALE, y * MAP_SCALE)
    width = int(math.ceil(width * MAP_SCALE))
    height = int(math.ceil(height * MAP_SCALE))
    legend_h = int(math.ceil(legend_h * MAP_SCALE))
    node_r = 6 * MAP_SCALE
    font_size = int(round(11 * MAP_SCALE))
    dot_font_size = max(5, int(round(7 * MAP_SCALE)))
    use_distance_shading = False
    max_dist = 0
    if distance_from_center is None:
        distance_from_center = distance_from_sol_bfs(adj, center=center)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'  <rect width="100%" height="100%" fill="#0f172a"/>',
        '  <g id="edges">',
    ]
    for u, v, diff in edges:
        if u not in pos or v not in pos:
            continue
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        color = DIFFICULTY_COLOR.get(diff, DIFFICULTY_COLOR[JumpDifficulty.Soft])
        lines.append(f'    <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="1.2" stroke-opacity="0.9"/>')
    lines.append("  </g>")
    lines.append('  <g id="nodes">')
    for name, (x, y) in pos.items():
        s = by_name.get(name)
        if s is not None and not s.system_is_populated:
            fill = UNINHABITED_FILL
        elif name == "Sol" or name in GATEWAY_SYSTEMS:
            cluster = GATEWAY_CLUSTER.get(name, StarClusters.INNER_SYSTEMS)
            fill = CLUSTER_VARIANT.get(cluster, CLUSTER_FALLBACK)
        else:
            cluster = s.cluster if s else None
            fill = CLUSTER_STANDARD.get(cluster, CLUSTER_FALLBACK)
        if name == "Sol":
            sol_r = node_r * 3.0
            pts = f"{x:.1f},{y - sol_r:.1f} {x + sol_r:.1f},{y:.1f} {x:.1f},{y + sol_r:.1f} {x - sol_r:.1f},{y:.1f}"
            lines.append(f'    <polygon points="{pts}" fill="{fill}" stroke="#e2e8f0" stroke-width="1.2"/>')
        elif name in GATEWAY_SYSTEMS:
            gw_r = node_r * 2.0
            pts = f"{x:.1f},{y - gw_r:.1f} {x + gw_r:.1f},{y:.1f} {x:.1f},{y + gw_r:.1f} {x - gw_r:.1f},{y:.1f}"
            lines.append(f'    <polygon points="{pts}" fill="{fill}" stroke="#e2e8f0" stroke-width="0.8"/>')
        else:
            lines.append(f'    <circle cx="{x:.1f}" cy="{y:.1f}" r="{node_r}" fill="{fill}" stroke="#e2e8f0" stroke-width="0.8"/>')
    lines.append("  </g>")
    lines.append('  <g id="labels" font-family="sans-serif" font-size="{}" fill="#e2e8f0" text-anchor="middle">'.format(font_size))
    for name, (x, y) in pos.items():
        if name == "Sol":
            label_dy = node_r * 3.0 + 14
        elif name in GATEWAY_SYSTEMS:
            label_dy = node_r * 2.0 + 14
        else:
            label_dy = node_r + 14
        lines.append(f'    <text x="{x:.1f}" y="{y:.1f}" dy="{label_dy:.1f}">{escape_svg(name)}</text>')
    lines.append("  </g>")
    legend_font = int(round(14 * MAP_SCALE))
    lines.append(f'  <g id="legend" font-size="{legend_font}" fill="#e2e8f0">')
    ly = height - legend_h + 20
    lx = 40
    for i, c in enumerate(StarClusters):
        lx_c = lx + i * 160
        lines.append(f'    <rect x="{lx_c}" y="{ly}" width="16" height="16" fill="{CLUSTER_STANDARD.get(c, CLUSTER_FALLBACK)}" stroke="#94a3b8"/>')
        lines.append(f'    <text x="{lx_c + 22}" y="{ly + 13}">{escape_svg(c.value)}</text>')
    lx_uninh = lx + len(StarClusters) * 160
    lines.append(f'    <rect x="{lx_uninh}" y="{ly}" width="16" height="16" fill="{UNINHABITED_FILL}" stroke="#94a3b8"/>')
    lines.append(f'    <text x="{lx_uninh + 22}" y="{ly + 13}">Uninhabited</text>')
    lx_jump = lx_uninh + 160
    for i, d in enumerate(JumpDifficulty):
        lx_d = lx_jump + i * 180
        lines.append(f'    <line x1="{lx_d}" y1="{ly + 8}" x2="{lx_d + 24}" y2="{ly + 8}" stroke="{DIFFICULTY_COLOR[d]}" stroke-width="3"/>')
        lines.append(f'    <text x="{lx_d + 30}" y="{ly + 13}">{d.value} Jump</text>')
    lines.append("  </g>")
    lines.append("</svg>")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path}")
    try:
        import cairosvg
        png_path = out_path.with_suffix(".png")
        cairosvg.svg2png(url=str(out_path), write_to=str(png_path), scale=2.0)
        print(f"Wrote {png_path}")
    except ImportError:
        pass


# ---- Optional: networkx + matplotlib for PNG and force-directed layout ----

def main_matplotlib(by_name, nodes_by_cluster, edges, out_png: Path, out_svg: Path):
    import networkx as nx
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D

    G = nx.Graph()
    for name in by_name:
        s = by_name[name]
        G.add_node(name, cluster=s.cluster)
    for u, v, diff in edges:
        G.add_edge(u, v, difficulty=diff)
    pos = layout_kamada_kawai({n: set(G.neighbors(n)) for n in G}, edges)
    if pos is None:
        pos = nx.spring_layout(G, k=2.0, iterations=80, seed=42, scale=1.0)
    else:
        pos = {n: (pos[n][0], -pos[n][1]) for n in pos}  # matplotlib y-up
    fig, ax = plt.subplots(figsize=(24, 18), facecolor="#0f172a")
    ax.set_facecolor("#0f172a")
    edge_groups = {d: [] for d in JumpDifficulty}
    for u, v, data in G.edges(data=True):
        d = data.get("difficulty", JumpDifficulty.Soft)
        edge_groups.setdefault(d, []).append((u, v))
    for diff, edge_list in edge_groups.items():
        if not edge_list:
            continue
        color = DIFFICULTY_COLOR.get(diff, DIFFICULTY_COLOR[JumpDifficulty.Soft])
        nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color=color, alpha=0.9, width=1.0, ax=ax)
    node_groups = {}
    for n in G.nodes():
        s = by_name.get(n)
        node_groups.setdefault(s.cluster if s else None, []).append(n)
    for cluster, nodes in node_groups.items():
        color = CLUSTER_STANDARD.get(cluster, CLUSTER_FALLBACK)
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=color, node_size=80, edgecolors="#e2e8f0", linewidths=0.5, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=5, font_color="#e2e8f0", ax=ax)
    ax.axis("off")
    ax.set_title("Starlit Frontiers -- Star systems and jump links", fontsize=14, color="#e2e8f0")
    legend_elements = (
        [Patch(facecolor=CLUSTER_STANDARD.get(c, CLUSTER_FALLBACK), edgecolor="#e2e8f0", label=c.value) for c in StarClusters]
        + [Line2D([0], [0], color=DIFFICULTY_COLOR[d], linewidth=2, label=f"Jump: {d.value}") for d in JumpDifficulty]
    )
    ax.legend(handles=legend_elements, loc="upper left", fontsize=8, facecolor="#1e293b", edgecolor="#475569", labelcolor="#e2e8f0")
    plt.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_png, dpi=150, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.savefig(out_svg, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"Wrote {out_png}")
    print(f"Wrote {out_svg}")


def distance_from_sol_bfs(adj: dict, center: str = "Sol") -> dict[str, int]:
    """BFS from center; return shortest hop count for each reachable node."""
    dist = {center: 0}
    q = [center]
    while q:
        u = q.pop(0)
        d = dist[u] + 1
        for v in adj.get(u, set()):
            if v not in dist:
                dist[v] = d
                q.append(v)
    return dist


def _distance_to_hex(dist: int, max_dist: int) -> str:
    """Interpolate from blue (dist 0) to deep purple (dist max)."""
    if max_dist <= 0:
        r, g, b = DISTANCE_COLOR_NEAR
    else:
        t = min(1.0, dist / max_dist)
        r = int(DISTANCE_COLOR_NEAR[0] + t * (DISTANCE_COLOR_FAR[0] - DISTANCE_COLOR_NEAR[0]) + 0.5)
        g = int(DISTANCE_COLOR_NEAR[1] + t * (DISTANCE_COLOR_FAR[1] - DISTANCE_COLOR_NEAR[1]) + 0.5)
        b = int(DISTANCE_COLOR_NEAR[2] + t * (DISTANCE_COLOR_FAR[2] - DISTANCE_COLOR_NEAR[2]) + 0.5)
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
    return f"#{r:02x}{g:02x}{b:02x}"


def filter_by_cluster(by_name, nodes_by_cluster, edges, adj, cluster):
    """Restrict to systems in the given cluster; edges only between those systems."""
    names = set(nodes_by_cluster.get(cluster, []))
    if not names:
        return by_name, nodes_by_cluster, edges, adj
    by_name = {n: by_name[n] for n in names if n in by_name}
    edges = [(u, v, d) for u, v, d in edges if u in names and v in names]
    adj = {n: (adj.get(n, set()) & names) for n in names}
    nodes_by_cluster = {cluster: sorted(names)}
    return by_name, nodes_by_cluster, edges, adj


def filter_inner_plus_gateways(by_name, nodes_by_cluster, edges, adj):
    """Restrict to Inner Systems cluster plus all gateway systems (other sectors); edges only between those."""
    inner = set(nodes_by_cluster.get(StarClusters.INNER_SYSTEMS, []))
    names = inner | GATEWAY_SYSTEMS
    names = {n for n in names if n in by_name}
    if not names:
        return by_name, nodes_by_cluster, edges, adj
    by_name = {n: by_name[n] for n in names}
    edges = [(u, v, d) for u, v, d in edges if u in names and v in names]
    adj = {n: (adj.get(n, set()) & names) for n in names}
    nodes_by_cluster = {StarClusters.INNER_SYSTEMS: sorted(inner)}  # legend still only needs inner
    return by_name, nodes_by_cluster, edges, adj


def main():
    parser = argparse.ArgumentParser(description="Generate Starlit star system map (SVG).")
    parser.add_argument(
        "--inner",
        action="store_true",
        help="Map only Inner Systems cluster (Sol-centred).",
    )
    parser.add_argument(
        "--sector",
        choices=[SECTOR_SLUG[c] for c in SECTOR_GATEWAY],
        help="Map only this sector (gateway at centre, concentric rings).",
    )
    parser.add_argument(
        "--all-sectors",
        action="store_true",
        help="Generate map and table for each of the five sectors (Antares, Canopus, Hyades, Polaris, Pleiades).",
    )
    parser.add_argument(
        "--combined",
        action="store_true",
        help="Single map with all systems: inner first (with room at edges), then each sector in its gateway arc.",
    )
    args = parser.parse_args()

    out_dir = _repo_root / "generated"
    by_name_full, nodes_by_cluster_full, edges_full, adj_full = build_graph_data()

    if args.combined:
        pos = (
            layout_kamada_kawai(adj_full, edges_full)
            if HAS_NETWORKX
            else layout_combined(
                by_name_full, nodes_by_cluster_full, edges_full, adj_full
            )
        )
        # Scale up so the canvas is larger and labels are readable
        pos = {name: (x * COMBINED_MAP_SCALE, y * COMBINED_MAP_SCALE) for name, (x, y) in pos.items()}
        pos = spread_overlapping_nodes(pos, min_dist=70.0, iterations=100)
        pos = push_nodes_from_edges(pos, edges_full, min_dist=45.0, iterations=80)
        _, _, _, adj_inner = filter_inner_plus_gateways(
            by_name_full, nodes_by_cluster_full, edges_full, adj_full
        )
        distance_from_sol = distance_from_sol_bfs(adj_inner, center="Sol")
        dist_to_gateway = distance_to_gateway_by_system(by_name_full, adj_full)
        out_svg = out_dir / "starlit_map_combined.svg"
        write_svg(
            by_name_full,
            edges_full,
            adj_full,
            out_svg,
            distance_from_sol=distance_from_sol,
            center="Sol",
            pos_override=pos,
            distance_from_center=dist_to_gateway,
        )
        return

    if args.all_sectors:
        for cluster, gateway in SECTOR_GATEWAY.items():
            by_name, nodes_by_cluster, edges, adj = filter_by_cluster(
                by_name_full.copy(), dict(nodes_by_cluster_full), list(edges_full), dict(adj_full), cluster
            )
            names = set(by_name.keys())
            if not names:
                print(f"Skipping {cluster.value}: no systems")
                continue
            slug = SECTOR_SLUG[cluster]
            out_svg = out_dir / f"starlit_map_{slug}.svg"
            write_svg(by_name, edges, adj, out_svg, distance_from_sol=None, center=gateway)
            print_sector_table(names, adj_full, f"--- {cluster.value} -- systems by number of links ---")
        return

    if args.sector:
        cluster = next(c for c, slug in SECTOR_SLUG.items() if slug == args.sector)
        gateway = SECTOR_GATEWAY[cluster]
        by_name, nodes_by_cluster, edges, adj = filter_by_cluster(
            by_name_full, nodes_by_cluster_full, edges_full, adj_full, cluster
        )
        names = set(by_name.keys())
        if not names:
            print(f"No systems in {cluster.value}", file=sys.stderr)
            raise SystemExit(1)
        out_svg = out_dir / f"starlit_map_{args.sector}.svg"
        write_svg(by_name, edges, adj, out_svg, distance_from_sol=None, center=gateway)
        print_sector_table(names, adj_full, f"--- {cluster.value} -- systems by number of links ---")
        return

    if args.inner:
        by_name, nodes_by_cluster, edges, adj = filter_inner_plus_gateways(
            by_name_full, nodes_by_cluster_full, edges_full, adj_full
        )
        out_svg = out_dir / "starlit_map_inner.svg"
        out_png = out_dir / "starlit_map_inner.png"
        distance_from_sol = distance_from_sol_bfs(adj, center="Sol")
        center = "Sol"
    else:
        by_name, nodes_by_cluster, edges, adj = by_name_full, nodes_by_cluster_full, edges_full, adj_full
        out_svg = out_dir / "starlit_map.svg"
        out_png = out_dir / "starlit_map.png"
        distance_from_sol = None
        center = "Sol"

    dist_to_gateway = distance_to_gateway_by_system(by_name, adj) if by_name is by_name_full else None
    write_svg(by_name, edges, adj, out_svg, distance_from_sol=distance_from_sol, center=center, distance_from_center=dist_to_gateway)
    if USE_MATPLOTLIB:
        try:
            main_matplotlib(by_name, nodes_by_cluster, edges, out_png, out_svg)
        except ImportError:
            print("USE_MATPLOTLIB=1 but networkx/matplotlib not installed; only SVG was written.", file=sys.stderr)


if __name__ == "__main__":
    main()
