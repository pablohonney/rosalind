from .solution import hamming_distance


def test_hamming_distance():
    a, b = "GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"
    assert hamming_distance(a, b) == 7
