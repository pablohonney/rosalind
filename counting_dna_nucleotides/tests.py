from .solution import solve


def test_compute_gc_content():
    assert (
        solve(
            dna="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        )
        == "20 12 17 21"
    )
