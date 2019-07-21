def menor_nome(meu_string):
    menor_str = ''
    for string in meu_string:
        string = string.strip().lower()
        if menor_str == '':
            menor_str = string
        else:
            if len(string) < len(menor_str):
                menor_str = string
    return menor_str.capitalize()


# print(menor_nome(['DURZHOZOA', 'SHULFE', 'GIOVI', 'pipe', 'ArvIGi']))
# print(menor_nome(['Mioni', 'Barkorak', 'xundîr', 'voinseivuo', 'fuinob']))
# print(menor_nome(['Zouzo', 'Gasok', 'Pega', 'Elgiga', 'Soerkub']))
# print(menor_nome(['kurak', 'nani', 'urbxatur ', 'ogolido ', 'ramolar']))
# print(menor_nome(['HUZU', 'KEYBI', 'MUXUOR ', 'HANZRE', 'SAROUEK']))
# print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))
# print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
# print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))


def test_menor_nome0():
    assert menor_nome(['DURZHOZOA', 'SHULFE', 'GIOVI', 'pipe', 'ArvIGi']) == 'Pipe'


def test_menor_nome1():
    assert menor_nome(['Mioni', 'Barkorak', 'xundîr', 'voinseivuo', 'fuinob']) == 'Mioni'


def test_menor_nome2():
    assert menor_nome(['Zouzo', 'Gasok', 'Pega', 'Elgiga', 'Soerkub']) == 'Pega'


def test_menor_nome3():
    assert menor_nome(['kurak', 'nani', 'urbxatur ', 'ogolido ', 'ramolar']) == 'Nani'


def test_menor_nome5():
    assert menor_nome(['HUZU', 'KEYBI', 'MUXUOR ', 'HANZRE', 'SAROUEK']) == 'Huzu'


def test_menor_nome6():
    assert menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == 'José'


def test_menor_nome7():
    assert menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == 'José'


def test_menor_nome8():
    assert menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == 'José'
