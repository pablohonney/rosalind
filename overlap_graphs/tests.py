from pathlib import Path

import pytest

from .solution import get_overlap_graphs, get_overlap_graphs_naive
from utils import parse_fasta_text


@pytest.fixture
def example():
    with open(Path(__file__).parent / "example.txt") as f:
        return parse_fasta_text(f.read())


def test_get_overlap_graphs_naive(example):
    assert list(get_overlap_graphs_naive(example)) == [
        ("Rosalind_0498", "Rosalind_2391"),
        ("Rosalind_0498", "Rosalind_0442"),
        ("Rosalind_2391", "Rosalind_2323"),
    ]


def test_get_overlap_graphs(example):
    assert get_overlap_graphs(example) == [
        ("Rosalind_0498", "Rosalind_2391"),
        ("Rosalind_0498", "Rosalind_0442"),
        ("Rosalind_2391", "Rosalind_2323"),
    ]
