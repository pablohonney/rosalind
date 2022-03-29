from .solution import translate, TRANSLATION_TABLE


def test_translate():
    rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    assert translate(rna=rna) == "MAMAPRTEINSTRING"
