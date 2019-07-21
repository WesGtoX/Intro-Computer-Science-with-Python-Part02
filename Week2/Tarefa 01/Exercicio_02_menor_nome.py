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


# def test_menor_nome6():
#     assert menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == 'José'
#
#
# def test_menor_nome7():
#     assert menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == 'José'
#
#
# def test_menor_nome8():
#     assert menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == 'José'
