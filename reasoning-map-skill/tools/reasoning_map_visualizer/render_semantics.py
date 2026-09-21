"""Shared semantic grouping helpers for reasoning-map renderers."""

from __future__ import annotations

from .render_model import RenderNode


LAYER_ORDER = {
    "question": 0,
    "problem": 0,
    "goal": 0,
    "claim": 1,
    "constraint": 1,
    "risk": 1,
    "option": 2,
    "decision": 3,
    "gap": 3,
}

DISPLAY_CLASS_COLORS = {
    "problem": "#7c4dff",
    "cause": "#ba68c8",
    "benefit": "#8bc34a",
    "effect": "#f4d03f",
    "detriment": "#f48fb1",
    "component": "#a5d6a7",
    "solution": "#66bb6a",
    "mitigation": "#81d4fa",
    "obstacle": "#ef9a9a",
    "gap": "#90a4ae",
    "neutral": "#90a4ae",
}


def node_layer(node: RenderNode) -> int:
    return LAYER_ORDER.get(node.kind, 2)


def display_class(node: RenderNode) -> str:
    if node.kind in {"problem", "question", "goal"}:
        return "problem"
    if node.kind in {"option", "decision"}:
        return "solution"
    if node.kind == "gap":
        return "gap"
    if node.kind == "constraint":
        return "obstacle"
    if node.kind == "risk":
        return "detriment"
    if node.kind == "claim":
        role = str(node.source.get("role", ""))
        if role == "cause":
            return "cause"
        if role in {"mitigation", "support"}:
            return "benefit"
        if role in {"counterpoint", "detriment"}:
            return "detriment"
        if role in {"component", "dependency"}:
            return "component"
        return "benefit"
    return "neutral"
