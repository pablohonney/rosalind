from pathlib import Path

import pytest

from .solution import get_max_record
from utils import parse_fasta_text


@pytest.fixture
def example():
    with open(Path(__file__).parent / "example.txt") as f:
        return parse_fasta_text(f.read())


def test_compute_gc_content(example):
    assert get_max_record(example) == ("Rosalind_0808", 60.91954022988506)
