"""Graphviz DOT emission for reasoning-map render models."""

from __future__ import annotations

from collections import defaultdict

from .render_model import RenderGraph, RenderNode, RenderEdge
from .render_semantics import DISPLAY_CLASS_COLORS, node_layer, display_class


NODE_SHAPES = {
    "problem": "box",
    "question": "diamond",
    "goal": "oval",
    "decision": "hexagon",
    "option": "ellipse",
    "risk": "octagon",
    "gap": "note",
}

VISIBILITY_STYLES = {
    "normal": "solid",
    "muted": "dashed",
    "hidden": "dotted",
}

PRIMARY_EDGE_RELATIONS = {"addresses", "challenges", "depends_on", "mitigates", "causes", "leads_to", "supersedes"}
HIDDEN_EDGE_LABEL_RELATIONS = {"supports", "addresses", "raises", "relates_to"}


def emit_dot(graph: RenderGraph) -> str:
    """Render a reasoning-map render model as DOT text."""
    title = _escape_dot_string(graph.title)
    lines = [
        "digraph reasoning_map {",
        '  graph [label="%s", labelloc="t", ranksep="1.4 equally", nodesep="0.45"];' % title,
        "  rankdir=TB;",
        '  node [fontname="Helvetica"];',
        '  edge [fontname="Helvetica"];',
    ]

    for node in graph.nodes:
        lines.append(_emit_node(node))
    lines.extend(_emit_rank_layers(graph.nodes))
    for edge in graph.edges:
        lines.append(_emit_edge(edge))

    lines.append("}")
    return "\n".join(lines) + "\n"


def _emit_node(node: RenderNode) -> str:
    node_id = _escape_dot_string(node.display_id)
    shape = NODE_SHAPES.get(node.kind, "ellipse")
    color = DISPLAY_CLASS_COLORS[_display_class(node)]
    style_parts = ["rounded", VISIBILITY_STYLES.get(node.visibility, "solid")]
    if node.deficiencies:
        style_parts.append("bold")
    if node.status in {"resolved"}:
        style_parts.append("filled")
    fillcolor = _status_fillcolor(node.status)
    label = _escape_dot_string(_node_label(node))
    attrs = [
        f'label="{label}"',
        f'shape="{shape}"',
        f'color="{color}"',
        f'style="{",".join(style_parts)}"',
    ]
    if fillcolor is not None:
        attrs.append(f'fillcolor="{fillcolor}"')
    return f'  "{node_id}" [{", ".join(attrs)}];'


def _emit_edge(edge: RenderEdge) -> str:
    edge_from = _escape_dot_string(edge.from_id)
    edge_to = _escape_dot_string(edge.to_id)
    color = _edge_color(edge)
    style = VISIBILITY_STYLES.get(edge.visibility, "solid")
    attrs = [f'color="{color}"', f'style="{style}"']
    if edge.relation not in PRIMARY_EDGE_RELATIONS:
        attrs.append('constraint="false"')
    if edge.relation not in HIDDEN_EDGE_LABEL_RELATIONS:
        label = _escape_dot_string(edge.relation)
        attrs.insert(0, f'label="{label}"')
    return f'  "{edge_from}" -> "{edge_to}" [{", ".join(attrs)}];'


def _emit_rank_layers(nodes: tuple[RenderNode, ...]) -> list[str]:
    layer_nodes: dict[int, list[RenderNode]] = defaultdict(list)
    for node in nodes:
        layer_nodes[node_layer(node)].append(node)

    lines: list[str] = []
    for layer in sorted(layer_nodes):
        lines.append(f'  subgraph "cluster_layer_{layer}" {{')
        lines.append("    rank=same;")
        lines.append('    color="transparent";')
        lines.append('    penwidth=0;')
        for node in sorted(layer_nodes[layer], key=lambda item: (item.title.lower(), item.raw_id)):
            node_id = _escape_dot_string(node.display_id)
            lines.append(f'    "{node_id}";')
        lines.append("  }")
    return lines
def _node_label(node: RenderNode) -> str:
    return node.title


def _display_class(node: RenderNode) -> str:
    return display_class(node)


def _status_fillcolor(status: str) -> str | None:
    if status == "resolved":
        return "#f5f5f5"
    return None


def _edge_color(edge: RenderEdge) -> str:
    if edge.status in {"rejected", "erroneous"}:
        return "firebrick"
    if edge.status == "superseded":
        return "gray40"
    if edge.status == "resolved":
        return "darkgreen"
    return "#616161"


def _escape_dot_string(value: str) -> str:
    escaped: list[str] = []
    for char in value:
        if char == "\\":
            escaped.append("\\\\")
            continue
        if char == '"':
            escaped.append('\\"')
            continue
        if char == "\n":
            escaped.append("\\n")
            continue
        if char == "\r":
            escaped.append("\\r")
            continue
        if char == "\t":
            escaped.append("\\t")
            continue

        codepoint = ord(char)
        if codepoint < 0x20 or codepoint == 0x7F:
            escaped.append(f"\\x{codepoint:02x}")
            continue
        escaped.append(char)
    return "".join(escaped)
