from pathlib import Path

import pytest

from .solution import locate_restriction_sites
from utils import parse_fasta_text


@pytest.fixture
def example():
    root = Path(__file__).parent

    with open(root / "input_1.txt") as f:
        fasta_records = parse_fasta_text(f.read())
    input_dna = fasta_records[0].text

    with open(root / "output_1.txt") as f:
        raw_output = f.read().split("\n")
    output_sites = [tuple(map(int, line.split())) for line in raw_output]

    return input_dna, output_sites


def test_locate_restriction_sites_no_short_runs():
    assert locate_restriction_sites(dna="TA") == []
    assert locate_restriction_sites(dna="TGCA") == [(1, 4)]


def test_locate_restriction_sites():
    assert locate_restriction_sites(dna="TCAATGCATGCGGGTCTATATGCAT") == [
        (4, 6),
        (5, 4),
        (6, 6),
        (7, 4),
        (17, 4),
        (18, 4),
        (20, 6),
        (21, 4),
    ]


def test_example(example):
    input_dna, expected_output = example
    restriction_sites = locate_restriction_sites(input_dna)
    assert restriction_sites == expected_output
