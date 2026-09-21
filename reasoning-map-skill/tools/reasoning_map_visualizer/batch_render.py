"""Batch CLI for rendering reasoning-map graphs from a directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .loader import GraphValidationError
from .visualize import OUTPUT_FORMATS, _atomic_write_text, render_graph


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render all reasoning-map JSON files in a directory.")
    parser.add_argument("input_dir", help="Directory containing reasoning-map JSON files.")
    parser.add_argument(
        "--format",
        choices=OUTPUT_FORMATS,
        default="dot",
        help="Output format. Defaults to dot.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write output files. Default behavior is dry-run reporting only.",
    )
    parser.add_argument("--include-muted", action="store_true", help="Include muted nodes and edges.")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden nodes and edges.")
    parser.add_argument("--all-visibility", action="store_true", help="Include all visibility levels.")
    parser.add_argument("--all-status", action="store_true", help="Include non-active statuses.")
    parser.add_argument("--full-graph", action="store_true", help="Include all statuses and visibility levels.")
    parser.add_argument("--focus", help="Focus on a single node id for each graph.")
    parser.add_argument("--depth", type=int, help="Neighborhood depth when --focus is used.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        parser.error(f"input directory does not exist: {input_dir}")
    if not input_dir.is_dir():
        parser.error(f"input path is not a directory: {input_dir}")

    report = render_directory(
        input_dir,
        output_format=args.format,
        write=args.write,
        include_muted=args.include_muted,
        include_hidden=args.include_hidden,
        all_visibility=args.all_visibility,
        all_status=args.all_status,
        full_graph=args.full_graph,
        focus=args.focus,
        depth=args.depth,
    )

    print(json.dumps(report, indent=2, sort_keys=True))

    failures = report["failures"]
    for failure in failures:
        print(f'{failure["input_path"]}: {failure["error"]}', file=sys.stderr)

    return 1 if failures else 0


def render_directory(
    input_dir: str | Path,
    *,
    output_format: str = "dot",
    write: bool = False,
    include_muted: bool = False,
    include_hidden: bool = False,
    all_visibility: bool = False,
    all_status: bool = False,
    full_graph: bool = False,
    focus: str | None = None,
    depth: int | None = None,
) -> dict[str, Any]:
    directory = Path(input_dir)
    if not directory.exists():
        raise FileNotFoundError(f"input directory does not exist: {directory}")
    if not directory.is_dir():
        raise NotADirectoryError(f"input path is not a directory: {directory}")

    successes: list[dict[str, Any]] = []
    failures: list[dict[str, str]] = []
    written_count = 0

    for graph_path in sorted(directory.glob("*.json")):
        output_path = graph_path.with_suffix(_output_suffix(output_format))
        try:
            rendered = render_graph(
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
        except (GraphValidationError, ValueError, OSError, json.JSONDecodeError) as exc:
            failures.append(
                {
                    "input_path": str(graph_path),
                    "output_path": str(output_path),
                    "error": str(exc),
                }
            )
            continue

        if write:
            _atomic_write_text(output_path, rendered)
            written_count += 1

        successes.append(
            {
                "input_path": str(graph_path),
                "output_path": str(output_path),
                "written": write,
            }
        )

    return {
        "input_dir": str(directory),
        "format": output_format,
        "dry_run": not write,
        "success_count": len(successes),
        "failure_count": len(failures),
        "written_count": written_count,
        "successes": successes,
        "failures": failures,
    }


def _output_suffix(output_format: str) -> str:
    if output_format == "dot":
        return ".dot"
    if output_format == "mermaid":
        return ".mermaid"
    if output_format == "terminal":
        return ".terminal"
    raise ValueError(f"unsupported format: {output_format}")


if __name__ == "__main__":
    raise SystemExit(main())
