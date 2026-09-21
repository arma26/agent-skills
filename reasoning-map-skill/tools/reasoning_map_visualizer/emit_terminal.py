"""Terminal inspection view for reasoning-map render models."""

from __future__ import annotations

from collections import defaultdict

from .render_model import RenderEdge, RenderGraph, RenderNode
from .render_semantics import node_layer


def emit_terminal(graph: RenderGraph) -> str:
    """Render a reasoning-map render model as a readable terminal summary."""
    node_by_id = {node.raw_id: node for node in graph.nodes}
    outgoing: dict[str, list[RenderEdge]] = defaultdict(list)
    incoming: dict[str, list[RenderEdge]] = defaultdict(list)
    for edge in graph.edges:
        outgoing[edge.from_id].append(edge)
        incoming[edge.to_id].append(edge)

    lines = [f"Graph: {graph.title}", f"Graph ID: {graph.graph_id}"]
    if graph.scope:
        lines.append(f"Scope: {graph.scope}")
    if graph.warnings:
        lines.append("Warnings:")
        for warning in graph.warnings:
            lines.append(f"- {warning}")

    layer_nodes: dict[int, list[RenderNode]] = defaultdict(list)
    for node in graph.nodes:
        layer_nodes[node_layer(node)].append(node)

    for layer in sorted(layer_nodes):
        lines.append("")
        lines.append(f"Layer {layer}")
        for node in sorted(layer_nodes[layer], key=lambda item: (item.title.lower(), item.raw_id)):
            lines.extend(_emit_node_block(node, outgoing, incoming, node_by_id))

    return "\n".join(lines) + "\n"


def _emit_node_block(
    node: RenderNode,
    outgoing: dict[str, list[RenderEdge]],
    incoming: dict[str, list[RenderEdge]],
    node_by_id: dict[str, RenderNode],
) -> list[str]:
    lines = [f"- {node.raw_id} [{node.kind}] {node.title}"]
    if node.status != "active" or node.visibility != "normal":
        lines.append(f"  State: status={node.status}, visibility={node.visibility}")
    if node.deficiencies:
        deficiencies = ", ".join(node.deficiencies)
        lines.append(f"  Deficiencies: {deficiencies}")
    if incoming[node.raw_id]:
        lines.append(f"  Incoming: {_format_edges(incoming[node.raw_id], node_by_id)}")
    if outgoing[node.raw_id]:
        lines.append(f"  Outgoing: {_format_edges(outgoing[node.raw_id], node_by_id)}")
    return lines


def _format_edges(edges: list[RenderEdge], node_by_id: dict[str, RenderNode]) -> str:
    parts: list[str] = []
    for edge in sorted(edges, key=lambda item: (item.relation, item.from_id, item.to_id, item.raw_id)):
        counterpart_id = edge.to_id
        if edge.to_id not in node_by_id:
            counterpart_id = edge.from_id
        parts.append(f"{edge.relation} -> {counterpart_id}")
    return "; ".join(parts)
