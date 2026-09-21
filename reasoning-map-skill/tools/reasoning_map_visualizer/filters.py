"""Select subgraphs from normalized reasoning-map artifacts."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any


CURRENT_STATUSES = {"active"}
VISIBLE_LEVELS = ("normal", "muted", "hidden")


@dataclass(frozen=True)
class SelectionOptions:
    include_muted: bool = False
    include_hidden: bool = False
    all_visibility: bool = False
    all_status: bool = False
    full_graph: bool = False
    focus: str | None = None
    depth: int | None = None


@dataclass(frozen=True)
class SelectionResult:
    graph: dict[str, Any]
    dangling_edges: tuple[dict[str, Any], ...]
    suppressed_node_ids: tuple[str, ...]
    suppressed_edge_ids: tuple[str, ...]


def select_graph(graph: dict[str, Any], options: SelectionOptions | None = None) -> SelectionResult:
    selection = options or SelectionOptions()
    allowed_visibility = _allowed_visibility(selection)

    nodes_by_id = {node["id"]: node for node in graph["nodes"]}
    initially_selected_nodes = {
        node_id: node
        for node_id, node in nodes_by_id.items()
        if _node_selected(node, selection, allowed_visibility)
    }

    edges = graph["edges"]
    dangling_edges = tuple(edge for edge in edges if edge["from"] not in nodes_by_id or edge["to"] not in nodes_by_id)
    selected_edges = [
        edge
        for edge in edges
        if _edge_selected(edge, initially_selected_nodes, selection, allowed_visibility)
    ]
    selected_nodes = initially_selected_nodes

    if selection.focus is not None:
        focused_node_ids = _focused_node_ids(selection.focus, selected_nodes, selected_edges, selection.depth)
        selected_nodes = {node_id: node for node_id, node in selected_nodes.items() if node_id in focused_node_ids}
        selected_edges = [
            edge
            for edge in selected_edges
            if edge["from"] in focused_node_ids and edge["to"] in focused_node_ids
        ]

    suppressed_node_ids = tuple(
        sorted(node_id for node_id in nodes_by_id if node_id not in selected_nodes)
    )
    selected_edge_ids = {selected_edge["id"] for selected_edge in selected_edges}
    suppressed_edge_ids = tuple(
        sorted(
            edge["id"]
            for edge in edges
            if edge["id"] not in selected_edge_ids
        )
    )
    selected_graph = dict(graph)
    selected_graph["nodes"] = list(selected_nodes.values())
    selected_graph["edges"] = selected_edges
    return SelectionResult(
        graph=selected_graph,
        dangling_edges=dangling_edges,
        suppressed_node_ids=suppressed_node_ids,
        suppressed_edge_ids=suppressed_edge_ids,
    )


def _allowed_visibility(selection: SelectionOptions) -> set[str]:
    if selection.full_graph or selection.all_visibility:
        return set(VISIBLE_LEVELS)

    allowed = {"normal"}
    if selection.include_muted:
        allowed.add("muted")
    if selection.include_hidden:
        allowed.add("hidden")
    return allowed


def _node_selected(node: dict[str, Any], selection: SelectionOptions, allowed_visibility: set[str]) -> bool:
    if node.get("visibility", "normal") not in allowed_visibility:
        return False
    if selection.full_graph or selection.all_status:
        return True
    return node.get("status", "active") in CURRENT_STATUSES


def _edge_selected(
    edge: dict[str, Any],
    selected_nodes: dict[str, dict[str, Any]],
    selection: SelectionOptions,
    allowed_visibility: set[str],
) -> bool:
    if edge.get("from") not in selected_nodes or edge.get("to") not in selected_nodes:
        return False
    if edge.get("visibility", "normal") not in allowed_visibility:
        return False
    if selection.full_graph or selection.all_status:
        return True
    return edge.get("status", "active") in CURRENT_STATUSES


def _focused_node_ids(
    focus_node_id: str,
    selected_nodes: dict[str, dict[str, Any]],
    selected_edges: list[dict[str, Any]],
    depth: int | None,
) -> set[str]:
    if focus_node_id not in selected_nodes:
        available = ", ".join(sorted(selected_nodes))
        raise ValueError(f"focus node {focus_node_id!r} is not in the selected graph: {available}")

    if depth is not None and depth < 0:
        raise ValueError("depth must be zero or greater")

    max_depth = 1 if depth is None else depth
    adjacency: dict[str, set[str]] = {node_id: set() for node_id in selected_nodes}
    for edge in selected_edges:
        adjacency[edge["from"]].add(edge["to"])
        adjacency[edge["to"]].add(edge["from"])

    visited = {focus_node_id}
    queue = deque([(focus_node_id, 0)])
    while queue:
        node_id, current_depth = queue.popleft()
        if current_depth >= max_depth:
            continue
        for neighbor_id in adjacency[node_id]:
            if neighbor_id in visited:
                continue
            visited.add(neighbor_id)
            queue.append((neighbor_id, current_depth + 1))
    return visited
