import pytest
from PROVA_TESTES_2024.testes.stat_funcs import StatsN2

stat = StatsN2()

lista = [6, 7, 8]
lista1 = [7, 5, 7]

@pytest.fixture
def fixture_media():
    return stat.media(lista)


@pytest.fixture
def fixture_media_ponderada():
    pesos = [1, 2, 2]
    return stat.media_ponderada(lista, pesos)


@pytest.fixture
def fixture_mediana():
    return stat.mediana(lista)


@pytest.fixture
def fixture_unimodal():
    return stat.unimodal(lista1)


@pytest.fixture
def fixture_multimodal():
    return stat.multimodal(lista1)
