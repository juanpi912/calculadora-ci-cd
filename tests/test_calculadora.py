import pytest
from app.calculadora import sumar, dividir, multiplicar


def test_sumar_dos_numeros_positivos():
    assert sumar(5, 3) == 8


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_multiplicar_por_cero():
    assert multiplicar(8, 0) == 0