#!/usr/bin/env python3
"""Validate every skill in skills/<name>/SKILL.md.

Checks the YAML frontmatter that Claude needs to load a skill:
- the file starts with a frontmatter block delimited by '---'
- `name` is present, kebab-case, at most 64 characters and matches the folder name
- `name` follows the repo convention `<domain>-savings-coach`
- `description` is present and at most 1024 characters
- the body below the frontmatter is not empty
- every symlink inside the skill folder (e.g. into context/) resolves

Uses only the standard library so it runs without installing anything.
Exit code 0 means all skills are valid.
"""

import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_SUFFIX = "-savings-coach"
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024


def parse_frontmatter(text):
    """Return (fields, body) or raise ValueError when the frontmatter is malformed."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("file must start with a '---' frontmatter block")
    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        raise ValueError("frontmatter block is not closed with '---'")

    fields = {}
    for line in lines[1:end]:
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"cannot parse frontmatter line: {line!r}")
        fields[key.strip()] = value.strip().strip("\"'")
    body = "\n".join(lines[end + 1:])
    return fields, body


def validate_skill(skill_file):
    """Return a list of error messages for one SKILL.md file."""
    try:
        fields, body = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    except ValueError as error:
        return [str(error)]

    errors = []
    folder = skill_file.parent.name
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append("missing 'name'")
    else:
        if not NAME_PATTERN.match(name):
            errors.append(f"name {name!r} must be kebab-case (a-z, 0-9, '-')")
        if len(name) > MAX_NAME_LENGTH:
            errors.append(f"name is longer than {MAX_NAME_LENGTH} characters")
        if not name.endswith(NAME_SUFFIX) or name == NAME_SUFFIX[1:]:
            errors.append(f"name {name!r} must follow '<domain>{NAME_SUFFIX}'")
        if name != folder:
            errors.append(f"name {name!r} does not match folder {folder!r}")

    if not description:
        errors.append("missing 'description'")
    elif len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"description is longer than {MAX_DESCRIPTION_LENGTH} characters")

    if not body.strip():
        errors.append("skill body is empty")

    for path in sorted(skill_file.parent.rglob("*")):
        if path.is_symlink() and not path.exists():
            errors.append(f"broken link {path.relative_to(skill_file.parent)}")
    return errors


def main():
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        print(f"No skills found in {SKILLS_DIR}")
        return 1

    failed = False
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        errors = ["SKILL.md not found"] if not skill_file.is_file() else validate_skill(skill_file)
        if errors:
            failed = True
            for error in errors:
                print(f"FAIL {skill_dir.name}: {error}")
        else:
            print(f"ok   {skill_dir.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
