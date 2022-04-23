from .solution import RabbitIncubator


def test_mortal_rabbits():
    assert RabbitIncubator(months=6, age=3).breed() == 4


def test_exercise():
    assert RabbitIncubator(months=100, age=18).breed() == 351932180421200619432
