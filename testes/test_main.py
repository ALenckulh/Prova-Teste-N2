def test_media(fixture_media):
    assert fixture_media == 7


def test_media_ponderada(fixture_media_ponderada):
    assert fixture_media_ponderada == 7.2


def test_mediana(fixture_mediana):
    assert fixture_mediana == 7


def test_unimodal(fixture_unimodal):
    assert fixture_unimodal == 7


def test_multimodal(fixture_multimodal):
    assert fixture_multimodal == "Não é multimodal"
