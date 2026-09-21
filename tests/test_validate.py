from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate import discover_skills, readme_errors, validate_skill


VALID_SKILL = """\
---
name: example-skill
description: Validate an example skill.
---

# Example skill

Read [the reference](references/example.md).
"""


class SkillValidationTests(unittest.TestCase):
    def test_discovers_skills_without_entering_worktrees(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            active = root / "example-skill"
            ignored = root / ".worktrees" / "copy" / "duplicate-skill"
            active.mkdir()
            ignored.mkdir(parents=True)
            (active / "SKILL.md").write_text(VALID_SKILL, encoding="utf-8")
            (ignored / "SKILL.md").write_text(VALID_SKILL, encoding="utf-8")

            self.assertEqual(discover_skills(root), [active])

    def test_accepts_matching_name_and_existing_relative_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "example-skill"
            references = skill / "references"
            references.mkdir(parents=True)
            (skill / "SKILL.md").write_text(VALID_SKILL, encoding="utf-8")
            (references / "example.md").write_text("# Example\n", encoding="utf-8")

            result = validate_skill(root, skill)

            self.assertEqual(result.errors, ())

    def test_reports_missing_link_and_directory_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "wrong-directory"
            skill.mkdir()
            (skill / "SKILL.md").write_text(VALID_SKILL, encoding="utf-8")

            result = validate_skill(root, skill)

            self.assertIn(
                "skill name 'example-skill' does not match directory 'wrong-directory'",
                result.errors,
            )
            self.assertIn("missing linked resource: references/example.md", result.errors)

    def test_reports_missing_readme_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "Read [the missing guide](docs/missing.md).\n",
                encoding="utf-8",
            )

            self.assertEqual(
                readme_errors(root),
                ["missing linked resource: docs/missing.md"],
            )

    def test_rejects_links_outside_the_documented_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "example-skill"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                VALID_SKILL.replace(
                    "references/example.md",
                    "../outside.md",
                ),
                encoding="utf-8",
            )

            result = validate_skill(root, skill)

            self.assertIn(
                "local link target escapes its documented boundary",
                result.errors,
            )

    def test_rejects_absolute_links_without_echoing_the_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "example-skill"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                VALID_SKILL.replace(
                    "references/example.md",
                    "/private/example.md",
                ),
                encoding="utf-8",
            )

            result = validate_skill(root, skill)

            self.assertIn(
                "local link target must be repository-relative",
                result.errors,
            )
            self.assertNotIn("/private/example.md", "\n".join(result.errors))


if __name__ == "__main__":
    unittest.main()
