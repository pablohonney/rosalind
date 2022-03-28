from pathlib import Path

import pytest

from .solution import ProfileMatrix, calculate_consensus
from utils import parse_fasta_text

ROOT = Path(__file__).parent


def _parse_input(input_path: Path):
    with open(input_path) as f:
        fasta_records = parse_fasta_text(f.read())
    dnas = [r.text for r in fasta_records]
    return dnas


def _parse_output(output_path: Path):
    with open(output_path) as f:
        raw_output = f.read().split("\n")

    consensus = raw_output[0]
    profile_matrix = {}
    for line in raw_output[1:]:
        nucleotide, counts = line.split(":")
        profile_matrix[nucleotide] = list(map(int, counts.split()))

    return consensus, profile_matrix


@pytest.fixture
def example_1():
    return _parse_input(ROOT / "input_1.txt"), _parse_output(ROOT / "output_1.txt")


@pytest.fixture
def example_2():
    return _parse_input(ROOT / "input_2.txt"), _parse_output(ROOT / "output_2.txt")


def test_profile_matrix_and_consensus(example_1):
    dnas, (expected_consensus, expected_profile) = example_1

    profile_matrix = ProfileMatrix(dnas)
    assert profile_matrix.matrix == expected_profile

    assert calculate_consensus(profile_matrix) == expected_consensus


def test_profile_matrix_and_consensus_2(example_2):
    dnas, (expected_consensus, expected_profile) = example_2

    profile_matrix = ProfileMatrix(dnas)
    assert profile_matrix.matrix == expected_profile

    assert calculate_consensus(profile_matrix) == expected_consensus
