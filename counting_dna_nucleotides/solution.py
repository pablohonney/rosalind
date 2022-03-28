from collections import Counter


def count_dna_nucleotides(dna: str) -> dict:
    return Counter(dna)


def present_result(counter: dict) -> str:
    nucleotides_count = [counter[nucleotide] for nucleotide in "ACGT"]
    return " ".join(map(str, nucleotides_count))


def solve(dna: str) -> str:
    count_ = count_dna_nucleotides(dna)
    return present_result(count_)
