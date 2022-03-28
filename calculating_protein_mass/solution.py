from pathlib import Path


def generate_weights_table(weights: list) -> dict:
    table = {}
    for i in range(0, len(weights) - 1, 2):
        table[weights[i]] = float(weights[i + 1])
    return table


with open(Path(__file__).parent / "weights.txt") as f:
    _weights = f.read()
weights_table = generate_weights_table(_weights.split())


def parse_raw_input(text: str):
    lines = text.split()
    records = []
    for i in range(0, len(lines) - 1, 2):
        records.append((lines[i], lines[i + 1]))
    return records


def weigh_protein(protein: str, table: dict) -> float:
    return round(sum(map(table.__getitem__, protein)), 3)
