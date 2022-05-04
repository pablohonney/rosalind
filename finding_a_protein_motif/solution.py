import typing as T
import re

from .fasta_fetcher import FastaDTO

N_GLYCOSYLATION_MOTIF_PATTERN = r"N[^P][ST][^P]"


class ProteinMotifFinder:
    """Find protein motifs from a motif pattern"""

    def __init__(self, fasta: FastaDTO, motif_pattern: str):
        self._fasta = fasta
        self._pattern = "(?=" + motif_pattern + ")"  # allow for overlapping matches

    def find_motifs(self) -> T.List[int]:
        sequence = self._fasta.get_sequence()
        return [match.start() + 1 for match in re.finditer(self._pattern, sequence)]
