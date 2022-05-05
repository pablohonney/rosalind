import typing as T

import pytest

from .fasta_fetcher import get_fasta_from_uniprot_id
from .solution import ProteinMotifFinder
from .solution import N_GLYCOSYLATION_MOTIF_PATTERN


def print_results(motif_start_indices: T.List[int], uniprot_id: str) -> None:
    if motif_start_indices:
        print(uniprot_id)
        print(" ".join(map(str, motif_start_indices)))


def test_protein_motif_finder():
    uniprot_ids_and_motif_start_indices = [
        ("A2Z669", []),
        ("B5ZC00", [85, 118, 142, 306, 395]),
        ("P07204_TRBM_HUMAN", [47, 115, 116, 382, 409]),
        ("P20840_SAG1_YEAST", [79, 109, 135, 248, 306, 348, 364, 402, 485, 501, 614]),
    ]

    for uniprot_id, expected_indices in uniprot_ids_and_motif_start_indices:
        fasta_dto = get_fasta_from_uniprot_id(uniprot_id)
        motif_start_indices = ProteinMotifFinder(
            sequence=fasta_dto.get_sequence(),
            motif_pattern=N_GLYCOSYLATION_MOTIF_PATTERN,
        ).find_motifs()

        assert expected_indices == motif_start_indices


@pytest.mark.skip("used to pass the rosalind level")
def test_exercise():
    uniprot_ids = [
        "P02725_GLP_PIG",
        "P0AAM4",
        "Q58CQ5",
        "P35446_FSPO_RAT",
        "P19827_ITH1_HUMAN",
        "P12630_BAR1_YEAST",
        "P04141_CSF2_HUMAN",
        "Q924A4",
        "P36913_EBA3_FLAME",
        "P01217_GLHA_BOVIN",
        "Q3ATP6",
        "P02760_HC_HUMAN",
    ]

    for uniprot_id in uniprot_ids:
        fasta_dto = get_fasta_from_uniprot_id(uniprot_id)
        motif_start_indices = ProteinMotifFinder(
            sequence=fasta_dto.get_sequence(),
            motif_pattern=N_GLYCOSYLATION_MOTIF_PATTERN,
        ).find_motifs()

        print_results(motif_start_indices, uniprot_id)
