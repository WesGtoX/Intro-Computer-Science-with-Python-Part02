def mais_curto(lista_de_nomes):
    curto = 0
    nome_curto = ''
    for nome in lista_de_nomes:
        nome = nome.strip().lower()
        if curto == 0:
            curto = len(nome)
            nome_curto = nome.capitalize()
        else:
            if len(nome) < curto:
                curto = len(nome)
                nome_curto = nome.capitalize()
    return nome_curto


def test_lista_nomes0():
    assert mais_curto(['  DURZHOZOA  ', 'SHULFE', 'GIOVI', ' pipe  ', 'ArvIGi']) == "Pipe"


def test_lista_nomes1():
    assert mais_curto(['Mioni', '  Barkorak', 'xundîr', '  voinseivuo', 'fuinob']) == "Mioni"


def test_lista_nomes2():
    assert mais_curto(['Zouzo', 'Gasok  ', '  Pega', 'Elgiga  ', 'Soerkub']) == "Pega"


def test_lista_nomes3():
    assert mais_curto(['kurak  ', 'nani  ', '        urbxatur ', 'ogolido ', 'ramolar']) == "Nani"


def test_lista_nomes5():
    assert mais_curto([' HUZU', ' KEYBI ', '  MUXUOR ', ' HANZRE', 'SAROUEK  ']) == "Huzu"
