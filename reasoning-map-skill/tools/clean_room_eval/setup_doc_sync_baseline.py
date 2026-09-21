#!/usr/bin/env python3
"""Prepare a local clean-room benchmark clone of doc-sync."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DEST = REPO_ROOT / ".worktrees" / "doc-sync-roomid-baseline"
DEFAULT_COMMIT = "2ef3467"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare a local doc-sync clone at a fixed baseline commit.",
    )
    parser.add_argument(
        "--source",
        type=Path,
        required=True,
        help="Path to the source doc-sync repository.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEFAULT_DEST,
        help="Destination directory for the local benchmark clone.",
    )
    parser.add_argument(
        "--commit",
        default=DEFAULT_COMMIT,
        help="Commit to check out in the benchmark clone.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply the clone and checkout actions. Without this flag the script is dry-run.",
    )
    return parser.parse_args()


def run_command(args: list[str], cwd: Path | None = None, apply: bool = False) -> None:
    location = f" (cwd={cwd})" if cwd is not None else ""
    print("$", " ".join(args) + location)
    if not apply:
        return

    subprocess.run(args, cwd=str(cwd) if cwd is not None else None, check=True)


def validate_source(source: Path) -> None:
    if not source.exists():
        raise SystemExit(f"Source repository does not exist: {source}")
    if not (source / ".git").exists():
        raise SystemExit(f"Source path is not a git repository: {source}")


def prepare_destination(dest: Path, apply: bool) -> None:
    if dest.exists():
        if not apply:
            print(f"Destination already exists and will not be modified during dry run: {dest}")
            return
        if any(dest.iterdir()):
            raise SystemExit(
                f"Destination already exists and is not empty: {dest}\n"
                "Choose a different destination or remove it manually."
            )
        if apply:
            shutil.rmtree(dest)
    if apply:
        dest.parent.mkdir(parents=True, exist_ok=True)


def main() -> int:
    args = parse_args()
    validate_source(args.source)
    prepare_destination(args.dest, args.apply)

    print("Dry run." if not args.apply else "Applying clone setup.")
    run_command(
        ["git", "clone", "--no-hardlinks", str(args.source), str(args.dest)],
        apply=args.apply,
    )
    run_command(["git", "checkout", args.commit], cwd=args.dest, apply=args.apply)
    run_command(["git", "status", "--short", "--branch"], cwd=args.dest, apply=args.apply)
    return 0


if __name__ == "__main__":
    sys.exit(main())
