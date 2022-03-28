from .solution import weigh_protein, weights_table


def test_weigh_protein():
    protein = "SKADYEK"
    assert weigh_protein(protein, weights_table) == 821.392
