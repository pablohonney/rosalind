from .solution import partial_permutations_count


def test_partial_permutations_count():
    assert partial_permutations_count(21, 7) == 51200


def test_partial_permutations_count_2():
    assert partial_permutations_count(97, 9) == 393600
