import ordenador
import conta_tempos
import pytest

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = conta_tempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = conta_tempos.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenado(self, l):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True

    def test_bolha_curta_aleat(self, o, l_aleat):
        o.bolha_curta(l_aleat)
        assert self.esta_ordenado(l_aleat) == True

    def test_selecao_direta_aleat(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.esta_ordenado(l_aleat) == True

    def test_bolha_curta_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenado(l_quase) == True

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenado(l_quase) == True
