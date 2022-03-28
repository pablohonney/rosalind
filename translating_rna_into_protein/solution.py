from pathlib import Path


def get_translation_table(table: str):
    codons = {}
    elements = table.split()
    for i in range(0, len(elements) - 1, 2):
        codons[elements[i]] = elements[i + 1]
    return codons


with open(Path(__file__).parent / "translation_table.txt") as f:
    translation_data = f.read()

TRANSLATION_TABLE = get_translation_table(translation_data)


def translate(translation_table: dict, rna: str) -> str:
    protein = []
    for i in range(0, len(rna) - 2, 3):
        amino_acid = translation_table[rna[i : i + 3]]
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)
    return "".join(protein)
