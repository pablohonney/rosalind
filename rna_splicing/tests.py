from pathlib import Path

import pytest

from .solution import solve, ParsedInput
from translating_rna_into_protein.solution import TRANSLATION_TABLE
from utils import parse_fasta_text


@pytest.fixture
def example() -> ParsedInput:
    with open(Path(__file__).parent / "example.txt") as f:
        faste_records = parse_fasta_text(f.read())
    return ParsedInput(faste_records[0].text, [r.text for r in faste_records[1:]])


def test_rna_splicing(example: ParsedInput):
    assert (
        solve(example.dna, example.introns, TRANSLATION_TABLE)
        == "MVYIADKQHVASREAYGHMFKVCA"
    )
