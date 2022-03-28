from pathlib import Path

import pytest

from .solution import get_consensus_profile
from utils import parse_fasta_text


@pytest.fixture
def example():
    root = Path(__file__).parent

    with open(root / "input_1.txt") as f:
        fasta_records = parse_fasta_text(f.read())

    with open(root / "output_1.txt") as f:
        raw_output = f.read().split("\n")
    expected_output = [tuple(map(int, line.split())) for line in raw_output]

    return fasta_records, expected_output


def test_consensus_profile(example):
    input_dnas, expected_output = example

    consensus_profile = get_consensus_profile(input_dnas)
    print(consensus_profile)
