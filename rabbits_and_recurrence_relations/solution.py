def breed_rabbits(month: int, birth_rate: int) -> int:
    old, young = 0, 1
    for _ in range(month - 1):
        old, young = old + young, old * birth_rate
    total = old + young
    return total
