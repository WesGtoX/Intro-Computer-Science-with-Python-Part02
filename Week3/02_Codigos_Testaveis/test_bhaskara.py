"""
Fixture
• Uma fixture é um valor fixo para um conjunto de testes.

• É usado muitas vezes para guardar um objeto que requer um pouco mais de trabalho para ser criado

• Para definir uma fixture, implementamos uma função que criar o objeto e a marcamos com

@pytest.fixture
"""

import Bhaskara
import pytest

class TestBhaskara:

    # Fixture
    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara()
    # # x² = 0    (1 raiz)
    # def testa_uma_raiz(self, b):
    #     assert b.calcula_raizes(1, 0, 0) == (1, 0)
    #
    # # (x-3)(x-2) = x² = 5x + 6 = 0      (2 raizes)
    # def testa_duas_raiz(self, b):
    #     assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)
    #
    # # 10x² + 10x + 10 = 0       (0 raizes reais)
    # def testa_zero_raiz(self, b):
    #     assert b.calcula_raizes(10, 10, 10) == 0
    #
    # # 10x² + 20x + 10 = 0       (raiz negatica)
    # def testa_raiz_negativa(self, b):
    #     assert b.calcula_raizes(10, 20, 10) == (1, -1)

    # Parametrização
    @pytest.mark.parametrize("entrada, esperado", [
        [(1, 0, 0), (1, 0)],
        [(1, -5, 6), (2, 3, 2)],
        [(10, 10, 10), (0)],
        [(10, 20, 10), (1, -1)],
    ])

    def testa_uma_raiz(self, b, entrada, esperado):
        assert b.calcula_raizes(entrada[0], entrada[1], entrada[2]) == (esperado)
