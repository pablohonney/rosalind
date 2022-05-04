import dataclasses
import io

import requests
import Bio.SeqIO
import Bio.SeqIO.FastaIO


@dataclasses.dataclass
class FastaDTO:
    """
    A data transfer object (DTO) representing a Fasta file fetched from uniprot database.
    """

    uniprot_id: str
    text: str
    format: str = "fasta"

    def _parse(self) -> Bio.SeqIO.FastaIO.FastaIterator:
        return Bio.SeqIO.parse(io.StringIO(self.text), self.format)

    def get_sequence(self) -> str:
        head_entry = next(self._parse())
        return str(head_entry.seq)


def get_fasta_from_uniprot_id(uniprot_id: str) -> FastaDTO:
    """Fetch fasta data from uniprot database"""
    response = requests.get(f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta")
    assert response.status_code == requests.codes.OK
    return FastaDTO(uniprot_id, response.text)
