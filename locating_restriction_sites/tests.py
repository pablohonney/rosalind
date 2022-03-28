from pathlib import Path

import pytest

from .solution import locate_restriction_sites


@pytest.fixture
def example():
    root = Path(__file__).parent

    with open(root / "input_1.txt") as f:
        raw_input = f.read().split()
    input_dna = "".join(raw_input[1:])

    with open(root / "output_1.txt") as f:
        raw_output = f.read().split("\n")
    expected_output = [tuple(map(int, line.split())) for line in raw_output]

    return input_dna, expected_output


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
    input_dna, output_sites = example
    restriction_sites = locate_restriction_sites(input_dna)
    assert restriction_sites == output_sites
