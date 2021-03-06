import typing as T
from collections import Counter, defaultdict


class ProfileMatrix:
    """
    Represents nucleotide counts per column in parallel dna text.
    """
    KEYS = "ATGC"

    def __init__(self, dna_sets: T.List[str]):
        self.matrix = defaultdict(list)
        self.length = len(dna_sets[0])

        matrix_cursor = zip(*dna_sets)
        for column in matrix_cursor:
            counter = Counter(column)
            for key in self.KEYS:
                self.matrix[key].append(counter.get(key, 0))

    def print(self):
        for key, counts in self.matrix.items():
            print(f"{key}: " + " ".join(map(str, counts)))

    def calculate_consensus(self) -> str:
        data = list(self.matrix.items())
        consensus = []
        for i in range(self.length):
            data.sort(key=lambda x: x[1][i], reverse=True)
            consensus.append(data[0][0])
        return "".join(consensus)
