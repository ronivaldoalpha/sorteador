import pytest

from src.main import Sorteados


def test_limite_preserva_intervalo_apos_reinicio():
    sorteio = Sorteados(inicio=5, maximo=12)
    sorteio.sorteados.append(8)

    sorteio.resetar()

    assert sorteio.cesta == list(range(5, 13))
    assert sorteio.maximo == 12
    assert sorteio.sorteados == []


def test_editar_limite_reconstroi_cesta_e_reinicia_sorteio():
    sorteio = Sorteados()
    sorteio.sorteados.append(3)
    sorteio.set_limite(20)

    assert sorteio.cesta == list(range(1, 21))
    assert sorteio.maximo == 20
    assert sorteio.sorteados == []
    assert sorteio.ultimo_valor is None


def test_limite_abaixo_do_inicio_e_rejeitado():
    sorteio = Sorteados(inicio=5, maximo=12)

    with pytest.raises(ValueError):
        sorteio.set_limite(4)
