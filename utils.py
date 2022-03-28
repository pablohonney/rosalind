from typing import NamedTuple, List


NEW_RECORD_STARTER = ">Rosalind"


class FastaRecord(NamedTuple):
    name: str
    text: str


def parse_fasta_text(text: str) -> List[FastaRecord]:
    lines = text.split()

    fasta_records = []
    name = ""
    recs = []
    for line in lines:
        if line.startswith(NEW_RECORD_STARTER):
            if name:
                fasta_records.append(FastaRecord(name=name, text="".join(recs)))

            name = line.lstrip(">")
            recs.clear()
        else:
            recs.append(line)

    fasta_records.append(FastaRecord(name=name, text="".join(recs)))

    return fasta_records


def parse_fasta_text_2(text: str) -> List[FastaRecord]:
    lines = text.split(">")

    records = []
    for line in lines:
        if not line:
            continue
        name, _line = line.strip().split("\n", 1)
        cleaned_line = _line.replace("\n", "")
        records.append(FastaRecord(name, cleaned_line))
    return records
