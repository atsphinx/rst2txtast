import json
from pathlib import Path
from pprint import pprint

import pytest
from deepdiff import DeepDiff
from docutils.core import publish_string

from rst2txtast.writer import ASTWriter

root = Path(__file__).parent


@pytest.mark.parametrize("source", list((root / "data").glob("*.rst")))
def test_it(source: Path):
    expected_path = source.parent / f"{source.stem}.json"
    if not expected_path.exists():
        return
    expected = json.loads(expected_path.read_text())
    actual = json.loads(
        publish_string(
            source=source.read_text(),
            source_path=str(source.name),
            writer=ASTWriter(),
            settings_overrides={
                "file_insertion_enabled": False,
            },
        )
    )
    diff = DeepDiff(
        expected,
        actual,
        ignore_order=True,
        exclude_paths=[
            "root[**]['line']",
            "root[**]['lineno']",
            "root[**]['rawsource']",
            "root[**]['source']",
        ],
    )
    # Show parsed data and diff to check behavior of writer.
    pprint({"ACTUAL": actual, "DIFF": diff})
    assert bool(not diff), "See captured stdout to check diff."
