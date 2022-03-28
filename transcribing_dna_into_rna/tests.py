from .solution import transcribe


def test_transcribe():
    assert transcribe(dna="GATGGAACTTGACTACGTAAATT") == "GAUGGAACUUGACUACGUAAAUU"
