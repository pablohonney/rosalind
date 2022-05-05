import typing as T
import re

N_GLYCOSYLATION_MOTIF_PATTERN = r"N[^P][ST][^P]"


class ProteinMotifFinder:
    """Find protein motifs from a motif pattern"""

    def __init__(self, sequence: str, motif_pattern: str):
        self._sequence = sequence
        self._pattern = "(?=" + motif_pattern + ")"  # allow for overlapping matches

    def find_motifs(self) -> T.List[int]:
        return [
            match.start() + 1 for match in re.finditer(self._pattern, self._sequence)
        ]
