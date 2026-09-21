"""Mermaid emission for reasoning-map render models."""

from __future__ import annotations

from .render_model import RenderEdge, RenderGraph, RenderNode


NODE_SHAPES = {
    "problem": '["{label}"]',
    "question": '{{"{label}"}}',
    "goal": '(["{label}"])',
    "decision": '{{{{"{label}"}}}}',
    "option": '["{label}"]',
    "risk": '(["{label}"])',
    "gap": '["{label}"]',
    "claim": '["{label}"]',
    "constraint": '["{label}"]',
}


def emit_mermaid(graph: RenderGraph) -> str:
    """Render a reasoning-map render model as Mermaid flowchart text."""
    lines = ["flowchart TD"]

    for node in graph.nodes:
        lines.append(f"  {_node_id(node)}{_node_shape(node)}")

    for edge in graph.edges:
        lines.append(f"  {_node_ref(edge.from_id)} -->|{_escape_label(edge.relation)}| {_node_ref(edge.to_id)}")

    if graph.warnings:
        lines.append("  %% warnings")
        for warning in graph.warnings:
            lines.append(f"  %% {_escape_comment(warning)}")

    return "\n".join(lines) + "\n"


def _node_id(node: RenderNode) -> str:
    return _node_ref(node.display_id)


def _node_ref(raw_id: str) -> str:
    chars: list[str] = []
    for char in raw_id:
        if char.isalnum():
            chars.append(char)
            continue
        chars.append("_")
    sanitized = "".join(chars).strip("_")
    if not sanitized:
        return "node"
    if sanitized[0].isdigit():
        return f"n_{sanitized}"
    return sanitized


def _node_shape(node: RenderNode) -> str:
    template = NODE_SHAPES.get(node.kind, '["{label}"]')
    return template.format(label=_escape_label(node.title))


def _escape_label(value: str) -> str:
    return value.replace('"', '\\"')


def _escape_comment(value: str) -> str:
    return value.replace("\n", " ").replace("\r", " ")
