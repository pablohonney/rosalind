import pytest

from .solution import gene_orders_count, enumerate_gene_orders


def test_gene_orders_count():
    assert gene_orders_count(3) == 6


def test_enumerate_gene_orders():
    assert list(enumerate_gene_orders(3)) == [
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    ]


@pytest.mark.skip
def test_example():
    n = 5
    print(gene_orders_count(n))
    for p in enumerate_gene_orders(n):
        print(" ".join(map(str, p)))
