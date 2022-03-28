from .solution import RabbitIncubator


def test_mortal_rabbits():
    assert RabbitIncubator(months=6, age=3).breed() == 4
