import typing as T
import re


# use lookahead assertion to avoid overlapping issues
def find_motif(sequence: str, motif: str) -> T.Sequence[int]:
    positions = [m.start() + 1 for m in re.finditer(rf"(?=({motif}))", sequence)]
    return tuple(positions)
