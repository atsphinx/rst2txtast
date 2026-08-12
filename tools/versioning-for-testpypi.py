"""Edit ``pyproject.toml`` to upload TestPyPI."""

import time
from pathlib import Path

import tomli

SECTION = "project"
KEYNAME = "version"


def main():
    pyproject_toml_path = Path.cwd() / "pyproject.toml"
    current_version = tomli.loads(pyproject_toml_path.read_text())[SECTION][KEYNAME]
    upload_version = f"{current_version}.post{int(time.time())}"

    print(f"Current version:\t{current_version}")
    print(f"Upload version: \t{upload_version}")
    replace_metadata(pyproject_toml_path, SECTION, KEYNAME, upload_version)


def replace_metadata(filepath: Path, section: str, keyname: str, value: str):
    found_section = False
    found_keyname = False
    lines = []
    for line in filepath.read_text().splitlines():
        if found_keyname:
            lines.append(line)
            continue
        if found_section and line.startswith(f"{keyname} = "):
            found_keyname = True
            lines.append(f'{keyname} = "{value}"')
            continue
        if line == f"[{section}]":
            found_section = True
        lines.append(line)
    filepath.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
