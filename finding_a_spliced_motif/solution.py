import typing as T

Subsequence = T.List[int]


def find_spliced_motif_naive(text: str, motif: str) -> Subsequence:
    subsequence = []
    motif_i = 0
    for text_i, text_char in enumerate(text):
        if motif[motif_i] == text_char:
            subsequence.append(text_i + 1)
            motif_i += 1
            if motif_i == len(motif):
                break

    return subsequence


class SplicedMotifFinder:
    def __init__(self, text: str, motif: str):
        self._motif = motif
        self._motif_occurrences = self._get_motif_occurrences(text, motif)

    def find_spliced_motif(self) -> T.Generator[Subsequence, None, None]:
        yield from self._find_spliced_motif(motif_index=0, previous_index=-1)

    @staticmethod
    def _get_motif_occurrences(text: str, motif: str) -> dict:
        motif_occurrences = {}
        for motif_char in motif:
            motif_occurrences[motif_char] = []

        for text_i, text_char in enumerate(text):
            if text_char in motif_occurrences:
                motif_occurrences[text_char].append(text_i)

        return motif_occurrences

    # recursively yield values
    def _find_spliced_motif(
        self, motif_index: int, previous_index: int
    ) -> T.Generator[Subsequence, None, None]:
        motif_char = self._motif[motif_index]
        motif_char_occurrences = self._motif_occurrences[motif_char]

        # get the valid/greater indices
        for text_i in motif_char_occurrences:
            if text_i <= previous_index:
                continue

            if motif_index + 1 == len(self._motif):
                yield [text_i + 1]
            else:
                for i in self._find_spliced_motif(
                    motif_index + 1, previous_index=text_i
                ):
                    yield [text_i + 1] + i
