from collections import Counter

from translating_rna_into_protein.solution import TRANSLATION_TABLE


def count_amino_acid_codons(table: dict) -> dict:
    return Counter(table.values())


amino_acid_codons_counts = count_amino_acid_codons(TRANSLATION_TABLE)


def infer_mrna_from_protein(protein: str, modulus: int = 10**6) -> int:
    count = amino_acid_codons_counts['Stop']
    for amino_acid in protein:
        count *= amino_acid_codons_counts[amino_acid]

    return count % modulus
