from pathlib import Path

import pytest

from .solution import solve


@pytest.fixture
def example():
    with open(Path(__file__).parent / "example.txt") as f:
        return f.read()


def test_compute_gc_content(example):
    assert solve(example) == ("Rosalind_0808", 60.91954022988506)
