from typing import List, NamedTuple

from complementing_a_strand_of_dna.solution import complement


class RestrictionSite(NamedTuple):
    position: int
    length: int


SHORTEST_MATCH = 4
LONGEST_MATCH = 12


def locate_restriction_sites(dna: str) -> List[RestrictionSite]:
    reversed_complement = complement(dna)[::-1]
    restriction_sites = []

    for start_pos in range(len(dna) - SHORTEST_MATCH + 1):
        for length in range(SHORTEST_MATCH, LONGEST_MATCH + 1):
            end_pos = start_pos + length
            if end_pos > len(dna):
                continue

            if dna[start_pos:end_pos] == reversed_complement[start_pos:end_pos][::-1]:
                restriction_sites.append(RestrictionSite(start_pos + 1, length))

    return restriction_sites
