from pathlib import Path

import pytest

from .solution import parse_raw_input, solve, ParsedInput
from translating_rna_into_protein.solution import TRANSLATION_TABLE


@pytest.fixture
def example() -> ParsedInput:
    with open(Path(__file__).parent / "example.txt") as f:
        input_ = f.read()
    return parse_raw_input(input_)


def test_rna_splicing(example: ParsedInput):
    assert (
        solve(example.dna, example.introns, TRANSLATION_TABLE)
        == "MVYIADKQHVASREAYGHMFKVCA"
    )
