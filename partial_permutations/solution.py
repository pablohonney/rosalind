from math import factorial


def partial_permutations_count(n: int, k: int, modulus: int = 10**6) -> int:
    return factorial(n) // factorial(n - k) % modulus
