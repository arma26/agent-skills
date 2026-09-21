"""Load and normalize reasoning-map graph artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL_KEYS = ("graph_id", "title", "nodes", "edges")


class GraphValidationError(ValueError):
    """Raised when a graph artifact is structurally invalid."""


def load_graph(path: str | Path) -> dict[str, Any]:
    """Load a reasoning-map graph and normalize filter-relevant fields."""
    graph_path = Path(path)
    with graph_path.open("r", encoding="utf-8") as handle:
        raw_graph = json.load(handle)

    _validate_graph(raw_graph, graph_path)

    graph = dict(raw_graph)
    graph["nodes"] = [_normalize_node(node) for node in raw_graph["nodes"]]
    graph["edges"] = [_normalize_edge(edge) for edge in raw_graph["edges"]]
    return graph


def _validate_graph(raw_graph: Any, graph_path: Path) -> None:
    if not isinstance(raw_graph, dict):
        raise GraphValidationError(f"{graph_path}: graph must be a JSON object")

    missing_keys = [key for key in REQUIRED_TOP_LEVEL_KEYS if key not in raw_graph]
    if missing_keys:
        joined = ", ".join(sorted(missing_keys))
        raise GraphValidationError(f"{graph_path}: missing top-level keys: {joined}")

    if not isinstance(raw_graph["nodes"], list):
        raise GraphValidationError(f"{graph_path}: nodes must be a list")
    if not isinstance(raw_graph["edges"], list):
        raise GraphValidationError(f"{graph_path}: edges must be a list")

    for index, node in enumerate(raw_graph["nodes"]):
        if not isinstance(node, dict):
            raise GraphValidationError(f"{graph_path}: node {index} must be an object")
        _require_keys(node, ("id", "kind", "title"), f"{graph_path}: node {index}")
    _validate_unique_ids(raw_graph["nodes"], "node", graph_path)

    for index, edge in enumerate(raw_graph["edges"]):
        if not isinstance(edge, dict):
            raise GraphValidationError(f"{graph_path}: edge {index} must be an object")
        _require_keys(edge, ("id", "from", "to", "type"), f"{graph_path}: edge {index}")
    _validate_unique_ids(raw_graph["edges"], "edge", graph_path)


def _require_keys(record: dict[str, Any], keys: tuple[str, ...], context: str) -> None:
    missing_keys = [key for key in keys if key not in record]
    if missing_keys:
        joined = ", ".join(sorted(missing_keys))
        raise GraphValidationError(f"{context} missing keys: {joined}")


def _validate_unique_ids(records: list[dict[str, Any]], record_type: str, graph_path: Path) -> None:
    seen_ids: set[str] = set()
    for index, record in enumerate(records):
        record_id = record["id"]
        if record_id in seen_ids:
            raise GraphValidationError(
                f"{graph_path}: duplicate {record_type} id {record_id!r} at index {index}"
            )
        seen_ids.add(record_id)


def _normalize_node(node: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(node)
    normalized.setdefault("status", "active")
    normalized.setdefault("visibility", "normal")
    deficiencies = normalized.get("deficiencies", [])
    normalized["deficiencies"] = list(deficiencies) if isinstance(deficiencies, list) else [deficiencies]
    normalized.setdefault("relevance", 1.0)
    return normalized


def _normalize_edge(edge: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(edge)
    normalized.setdefault("status", "active")
    normalized.setdefault("visibility", "normal")
    normalized.setdefault("relevance", 1.0)
    return normalized
