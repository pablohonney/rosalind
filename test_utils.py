from utils import parse_fasta_text

fasta_raw_input = """>Rosalind_1
ATCCAGCT
ZZZZZZZZ
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""


def test_read_fasta():
    records = parse_fasta_text(fasta_raw_input)
    assert records == [
        ("Rosalind_1", "ATCCAGCTZZZZZZZZ"),
        ("Rosalind_2", "GGGCAACT"),
        ("Rosalind_3", "ATGGATCT"),
        ("Rosalind_4", "AAGCAACC"),
        ("Rosalind_5", "TTGGAACT"),
        ("Rosalind_6", "ATGCCATT"),
        ("Rosalind_7", "ATGGCACT"),
    ]
