#!/usr/bin/env python3
"""Validate tracked skill packages and executable repository tests."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ALLOWED_FRONTMATTER_KEYS = {
    "allowed-tools",
    "author",
    "description",
    "license",
    "metadata",
    "name",
    "platforms",
    "version",
}
EXCLUDED_DIRECTORIES = {".git", ".worktrees", "__pycache__"}
FRONTMATTER_KEY = re.compile(r"^([a-zA-Z][a-zA-Z0-9_-]*):(?:\s*(.*))?$")
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TEST_SUITES = (
    (
        "repository-validator",
        Path("."),
        ("-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"),
    ),
    (
        "reasoning-map-skill",
        Path("reasoning-map-skill"),
        ("-m", "unittest", "tests.reasoning_map_visualizer.test_visualize", "-v"),
    ),
)


@dataclass(frozen=True)
class ValidationResult:
    skill: Path
    errors: tuple[str, ...]


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def discover_skills(root: Path) -> list[Path]:
    skills = []
    for skill_file in root.rglob("SKILL.md"):
        relative_parts = skill_file.relative_to(root).parts
        if EXCLUDED_DIRECTORIES.intersection(relative_parts):
            continue
        skills.append(skill_file.parent)
    return sorted(skills)


def split_frontmatter(content: str) -> tuple[list[str], str] | None:
    lines = content.splitlines()
    if not lines or lines[0] != "---":
        return None

    try:
        end = lines.index("---", 1)
    except ValueError:
        return None

    return lines[1:end], "\n".join(lines[end + 1 :])


def parse_top_level_fields(lines: list[str]) -> tuple[dict[str, str], list[str]]:
    fields: dict[str, str] = {}
    errors: list[str] = []
    active_key: str | None = None

    for line in lines:
        if not line.strip() or line.startswith((" ", "\t")):
            if active_key and line.strip():
                fields[active_key] = f"{fields[active_key]} {line.strip()}".strip()
            continue

        match = FRONTMATTER_KEY.fullmatch(line)
        if not match:
            errors.append(f"invalid top-level frontmatter line: {line!r}")
            active_key = None
            continue

        active_key = match.group(1)
        fields[active_key] = (match.group(2) or "").strip()

    return fields, errors


def local_link_errors(base: Path, body: str) -> list[str]:
    errors = []
    boundary = base.resolve()
    for raw_target in MARKDOWN_LINK.findall(body):
        target = raw_target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith(("#", "mailto:")):
            continue
        target_path = Path(target)
        if target_path.is_absolute():
            errors.append("local link target must be repository-relative")
            continue
        candidate = (base / target_path).resolve()
        if not candidate.is_relative_to(boundary):
            errors.append("local link target escapes its documented boundary")
            continue
        if not candidate.exists():
            errors.append(f"missing linked resource: {target}")
    return errors


def validate_skill(root: Path, skill: Path) -> ValidationResult:
    skill_file = skill / "SKILL.md"
    content = skill_file.read_text(encoding="utf-8")
    errors: list[str] = []
    split = split_frontmatter(content)

    if split is None:
        return ValidationResult(skill, ("missing or unterminated YAML frontmatter",))

    frontmatter_lines, body = split
    fields, parse_errors = parse_top_level_fields(frontmatter_lines)
    errors.extend(parse_errors)

    unexpected = sorted(set(fields) - ALLOWED_FRONTMATTER_KEYS)
    if unexpected:
        errors.append(f"unexpected frontmatter keys: {', '.join(unexpected)}")

    name = fields.get("name", "").strip("\"'")
    if not name:
        errors.append("missing skill name")
    elif len(name) > 64 or not SKILL_NAME.fullmatch(name):
        errors.append(f"invalid skill name: {name!r}")
    elif skill.name != name:
        errors.append(f"skill name {name!r} does not match directory {skill.name!r}")

    description = fields.get("description", "")
    if not description or description in {">", ">-", "|", "|-"}:
        errors.append("missing skill description")
    elif len(description) > 1024:
        errors.append("skill description exceeds 1024 characters")

    if re.search(r"(?m)^\s*\[TODO:[^]]*\]\s*$", body):
        errors.append("skill instructions contain an unfinished TODO placeholder")

    errors.extend(local_link_errors(skill, body))
    return ValidationResult(skill.relative_to(root), tuple(errors))


def readme_errors(root: Path) -> list[str]:
    readme = root / "README.md"
    if not readme.exists():
        return ["root README.md is missing"]
    return local_link_errors(root, readme.read_text(encoding="utf-8"))


def run_test_suite(root: Path, working_directory: Path, arguments: tuple[str, ...]) -> int:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    command = [sys.executable, *arguments]
    return subprocess.run(
        command,
        cwd=root / working_directory,
        env=environment,
        check=False,
    ).returncode


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate repository skill packages and executable tests."
    )
    parser.add_argument(
        "--skills-only",
        action="store_true",
        help="Validate skill packages without running executable tests.",
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    root = repository_root()
    skills = discover_skills(root)
    if not skills:
        print("Validation failed: no skill packages found.", file=sys.stderr)
        return 1

    failures = 0
    for skill in skills:
        result = validate_skill(root, skill)
        if result.errors:
            failures += 1
            print(f"FAIL skill {result.skill}", file=sys.stderr)
            for error in result.errors:
                print(f"  - {error}", file=sys.stderr)
            continue
        print(f"PASS skill {result.skill}")

    documentation_errors = readme_errors(root)
    if documentation_errors:
        failures += 1
        print("FAIL docs README.md", file=sys.stderr)
        for error in documentation_errors:
            print(f"  - {error}", file=sys.stderr)
    else:
        print("PASS docs README.md")

    test_suites = 0
    if not arguments.skills_only:
        test_suites = len(TEST_SUITES)
        for label, working_directory, command_arguments in TEST_SUITES:
            if run_test_suite(root, working_directory, command_arguments) != 0:
                failures += 1
                print(f"FAIL tests {label}", file=sys.stderr)
                continue
            print(f"PASS tests {label}")

    if failures:
        print(f"Validation failed: {failures} check(s) failed.", file=sys.stderr)
        return 1

    suite_word = "suite" if test_suites == 1 else "suites"
    print(f"Validation passed: {len(skills)} skills and {test_suites} test {suite_word}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
