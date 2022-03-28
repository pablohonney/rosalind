REPLACEMENT_MAP = str.maketrans("ATGC", "TACG")


def complement(dna: str) -> str:
    return dna.translate(REPLACEMENT_MAP)[::-1]
