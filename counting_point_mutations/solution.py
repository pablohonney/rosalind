def hamming_distance(line_1: str, line_2: str) -> int:
    assert len(line_1) == len(line_2)
    return sum(x != y for x, y in zip(line_1, line_2))
