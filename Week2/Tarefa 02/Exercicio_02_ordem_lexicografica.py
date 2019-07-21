def primeiro_lex(lista):
    lexico = ''
    i = 0
    for palavra in lista:
        if lexico == '':
            lexico = palavra
        else:
            if ord(palavra[i]) < ord(lexico[i]):
                lexico = palavra
            elif ord(palavra[i]) == ord(lexico[i]):
                letra_igual(palavra, lexico, i+1)
    return lexico


def letra_igual(palavra, lexico, i):
    if ord(palavra[i]) == ord(primeiro_lex[i]):
        letra_igual(palavra, primeiro_lex, i+1)
    else:
        lexico = palavra
    return lexico


# def test_primeiro_lex0():
#     assert primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A'
#
#
# def test_primeiro_lex1():
#     assert primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA'
#
#
# def test_primeiro_lex2():
#     assert primeiro_lex(['ola', 'rrrrrrr', 'olo' 'qqq', 'zcasa']) == 'ola'
#
#
# def test_primeiro_lex3():
#     assert primeiro_lex(['AAAAAA', 'AAAB' 'b']) == 'AAAAAA'
