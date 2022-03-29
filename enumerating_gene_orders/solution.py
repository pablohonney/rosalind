from math import factorial
from itertools import permutations
import typing as T


def enumerate_gene_orders(n: int) -> T.Generator[T.List[int], None, None]:
    values = list(range(1, n + 1))
    yield from permutations(values)


def gene_orders_count(n: int) -> int:
    return factorial(n)
