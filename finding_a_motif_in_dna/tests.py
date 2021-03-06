from .solution import find_motif


def test_find_motif():
    assert find_motif(sequence="GATATATGCATATACTT", motif="ATAT") == (2, 4, 10)


def test_find_motif_exercise():
    dna = "CGCACGTTATCGTCAACCGACAGTCAACCGTAAGTCAACCGTCAACCATAACGTCAACCTACTGTCAACCTCCGTCAACCGGTCAACCAAGTCAACCTGTCAACCGGGTCAACCTCGTCAACCGTCAACCTAGGTCAACCGTCAACCGGTCAACCATGAGTCAACCTAGCCCAGCGTCAACCAGTCAACCGGTCAACCTTGTCAACCTGTCAACCGAGTCAACCCCTTCTCCGGTCAACCGTCAACCGTCAACCTGTCAACCCGTCAACCTGTCAACCGCGTCAACCGTCAACCGGTCAACCGGAAAACGTCAACCTGTCAACCAGTCAACCTCGTAGTCAACCGTGGTCAACCGTCAACCGTCGTCAACCGTCAACCGTCAACCCTAAAGTCAACCAAGTCAACCGTCAACCGCAGTCAACCGTCGTCAACCTGTAGCGTCAACCAAGTCAACCAAGTCAACCTCGAGATGTCAACCGTGCTGGTCGTCAACCGTCAACCGTGTCAACCCCAGTCAACCGGTCAACCCTTGTGTCAACCTGTCAACCGTCAACCTCCGGGTGACCTGGGTCAACCGTCAACCGTCAACCCTGTCAACCTTCCTTGCGTCAACCTAGTTTCCCGTCAACCGATCCCGTCAACCCACAGCAAACGTCAACCTAAAGTCAACCTGTCAACCGCTGGCACGGTCAACCGGGGTCAACCCCCGTACGTCAACCGGTCAACCCTCGTCAACCGTCATTGTCAACCCGCCGGTCAACCGAGTCAACCTCTGGCGTCAACCCTGTCAACCGTTCCGTCAACCGAGTCAACCCGAGTCAACCGCTGGTCAACCGTCAACCCATACGGTCAACCCGTAGTCAACCTGTCAACC"
    expected_positions = (23, 34, 117, 134, 234, 241, 281, 338, 348, 355, 365, 372, 400, 417, 472, 488, 495, 542, 570, 577, 731, 787, 829)  # fmt: skip
    assert find_motif(sequence=dna, motif="GTCAACCGT") == expected_positions
