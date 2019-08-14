"""
Parametrização

import pytest
@pytest.mark.parametrize("entrada, esperado", [
    (0, 0),(1, 1),(2, 8),(-2, -8),(10, 1000),
])

def test_cubo(entrada, valor_esperado):
    assert cubo(entrada) == valor_esperado
"""
import pytest

def fatorial(n):
    if n < 0:
        return 0
    i = fat = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat


@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
])

def test_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado