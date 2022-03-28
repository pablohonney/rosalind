from .solution import complement


def test_complement():
    assert complement(dna="AAAACCCGGT") == "ACCGGGTTTT"
