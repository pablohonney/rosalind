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


def parse_raw_input(text: str) -> ParsedInput:
    lines = text.split()
    records = []
    for i in range(0, len(lines) - 1, 2):
        records.append((lines[i], lines[i + 1]))

    return ParsedInput(dna=records[0][1], introns=[r[1] for r in records[1:]])


def solve(dna: str, introns: list, translation_table: dict):
    spliced_dna = splice_dna(dna, introns)
    rna = transcribe(spliced_dna)
    protein = translate(translation_table, rna)
    return protein
