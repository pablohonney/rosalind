from .solution import breed_rabbits


def test_breed_rabbits():
    assert breed_rabbits(5, 3) == 19
