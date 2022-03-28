import re
from dataclasses import dataclass
from typing import List

from transcribing_dna_into_rna.solution import transcribe
from translating_rna_into_protein.solution import translate


def splice_dna(dna: str, introns: list) -> str:
    return re.sub("|".join(introns), "", dna)


@dataclass
class ParsedInput:
    dna: str
    introns: List[str]


def solve(dna: str, introns: list, translation_table: dict) -> str:
    spliced_dna = splice_dna(dna, introns)
    rna = transcribe(spliced_dna)
    protein = translate(translation_table, rna)
    return protein
