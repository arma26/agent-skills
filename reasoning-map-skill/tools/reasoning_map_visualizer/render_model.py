"""Internal render model for reasoning-map exporters."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RenderNode:
    raw_id: str
    display_id: str
    kind: str
    title: str
    label: str
    status: str
    visibility: str
    deficiencies: tuple[str, ...]
    style_tokens: tuple[str, ...]
    source: dict[str, Any]


@dataclass(frozen=True)
class RenderEdge:
    raw_id: str
    display_id: str
    from_id: str
    to_id: str
    relation: str
    status: str
    visibility: str
    style_tokens: tuple[str, ...]
    source: dict[str, Any]


@dataclass(frozen=True)
class RenderGraph:
    graph_id: str
    title: str
    scope: str | None
    status: str
    warnings: tuple[str, ...]
    nodes: tuple[RenderNode, ...]
    edges: tuple[RenderEdge, ...]


def build_render_graph(
    graph: dict[str, Any],
    *,
    warnings: tuple[str, ...] = (),
) -> RenderGraph:
    """Convert a selected reasoning graph into a backend-facing render model."""
    nodes = tuple(_build_node(node) for node in graph["nodes"])
    node_ids = {node.raw_id for node in nodes}
    edges = tuple(
        _build_edge(edge)
        for edge in graph["edges"]
        if edge["from"] in node_ids and edge["to"] in node_ids
    )
    return RenderGraph(
        graph_id=graph["graph_id"],
        title=graph.get("title", graph["graph_id"]),
        scope=graph.get("scope"),
        status=graph.get("status", "active"),
        warnings=warnings,
        nodes=nodes,
        edges=edges,
    )


def _build_node(node: dict[str, Any]) -> RenderNode:
    deficiencies = tuple(str(item) for item in node.get("deficiencies", ()))
    kind = str(node.get("kind", "node"))
    title = str(node["title"])
    label_lines = [title, f"[{kind}]"]
    if deficiencies:
        noun = "deficiency" if len(deficiencies) == 1 else "deficiencies"
        label_lines.append(f"{len(deficiencies)} {noun}")
    style_tokens = [f"kind:{kind}"]
    style_tokens.append(f"status:{node.get('status', 'active')}")
    style_tokens.append(f"visibility:{node.get('visibility', 'normal')}")
    if deficiencies:
        style_tokens.append("deficient")
    return RenderNode(
        raw_id=str(node["id"]),
        display_id=str(node["id"]),
        kind=kind,
        title=title,
        label="\n".join(label_lines),
        status=str(node.get("status", "active")),
        visibility=str(node.get("visibility", "normal")),
        deficiencies=deficiencies,
        style_tokens=tuple(style_tokens),
        source=dict(node),
    )


def _build_edge(edge: dict[str, Any]) -> RenderEdge:
    relation = str(edge.get("type", "relates_to"))
    style_tokens = [
        f"relation:{relation}",
        f"status:{edge.get('status', 'active')}",
        f"visibility:{edge.get('visibility', 'normal')}",
    ]
    return RenderEdge(
        raw_id=str(edge["id"]),
        display_id=str(edge["id"]),
        from_id=str(edge["from"]),
        to_id=str(edge["to"]),
        relation=relation,
        status=str(edge.get("status", "active")),
        visibility=str(edge.get("visibility", "normal")),
        style_tokens=tuple(style_tokens),
        source=dict(edge),
    )
