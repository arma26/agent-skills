"""CLI for rendering reasoning-map graphs."""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

from . import SelectionOptions, load_graph, select_graph
from .emit_dot import emit_dot
from .emit_mermaid import emit_mermaid
from .emit_terminal import emit_terminal
from .render_model import RenderGraph, build_render_graph

OUTPUT_FORMATS = ("dot", "mermaid", "terminal")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render reasoning-map graphs.")
    parser.add_argument("graph_path", help="Path to a reasoning-map JSON graph.")
    parser.add_argument(
        "--format",
        choices=OUTPUT_FORMATS,
        required=True,
        help="Output format.",
    )
    parser.add_argument("--output", help="Write rendered output to this path.")
    parser.add_argument("--include-muted", action="store_true", help="Include muted nodes and edges.")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden nodes and edges.")
    parser.add_argument("--all-visibility", action="store_true", help="Include all visibility levels.")
    parser.add_argument("--all-status", action="store_true", help="Include non-active statuses.")
    parser.add_argument("--full-graph", action="store_true", help="Include all statuses and visibility levels.")
    parser.add_argument("--focus", help="Focus on a single node id.")
    parser.add_argument("--depth", type=int, help="Neighborhood depth when --focus is used.")
    parser.add_argument("--strict", action="store_true", help="Fail if dangling edges are present.")
    return parser


def render_graph(
    graph_path: str | Path,
    *,
    output_format: str,
    include_muted: bool = False,
    include_hidden: bool = False,
    all_visibility: bool = False,
    all_status: bool = False,
    full_graph: bool = False,
    focus: str | None = None,
    depth: int | None = None,
) -> str:
    rendered, _ = _render_selection(
        graph_path,
        output_format=output_format,
        include_muted=include_muted,
        include_hidden=include_hidden,
        all_visibility=all_visibility,
        all_status=all_status,
        full_graph=full_graph,
        focus=focus,
        depth=depth,
    )
    return rendered


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    rendered, dangling_edges = _render_selection(
        args.graph_path,
        output_format=args.format,
        include_muted=args.include_muted,
        include_hidden=args.include_hidden,
        all_visibility=args.all_visibility,
        all_status=args.all_status,
        full_graph=args.full_graph,
        focus=args.focus,
        depth=args.depth,
    )

    if dangling_edges:
        message = _dangling_edge_message(dangling_edges, strict=args.strict)
        print(message, file=sys.stderr)
        if args.strict:
            return 1

    if args.output:
        _atomic_write_text(Path(args.output), rendered)
        return 0

    print(rendered, end="")
    return 0


def _render_selection(
    graph_path: str | Path,
    *,
    output_format: str,
    include_muted: bool = False,
    include_hidden: bool = False,
    all_visibility: bool = False,
    all_status: bool = False,
    full_graph: bool = False,
    focus: str | None = None,
    depth: int | None = None,
) -> tuple[str, tuple[dict[str, Any], ...]]:
    graph = load_graph(graph_path)
    selection = select_graph(
        graph,
        SelectionOptions(
            include_muted=include_muted,
            include_hidden=include_hidden,
            all_visibility=all_visibility,
            all_status=all_status,
            full_graph=full_graph,
            focus=focus,
            depth=depth,
        ),
    )
    warnings = ()
    if selection.dangling_edges:
        warnings = (_dangling_edge_message(selection.dangling_edges, strict=False),)
    render_graph_model = build_render_graph(selection.graph, warnings=warnings)
    return _emit(render_graph_model, output_format), selection.dangling_edges


def _emit(graph: RenderGraph, output_format: str) -> str:
    if output_format == "dot":
        return emit_dot(graph)
    if output_format == "mermaid":
        return emit_mermaid(graph)
    if output_format == "terminal":
        return emit_terminal(graph)
    raise ValueError(f"unsupported format: {output_format}")


def _dangling_edge_message(dangling_edges: tuple[dict[str, Any], ...], *, strict: bool) -> str:
    edge_ids = ", ".join(edge["id"] for edge in dangling_edges)
    prefix = "strict mode: " if strict else ""
    noun = "edge" if len(dangling_edges) == 1 else "edges"
    return f"{prefix}dangling {noun} detected: {edge_ids}"


def _atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            handle.write(content)
            handle.flush()
            temp_path = Path(handle.name)
        temp_path.replace(path)
    except Exception:
        if temp_path is not None:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                pass
        raise


if __name__ == "__main__":
    raise SystemExit(main())
