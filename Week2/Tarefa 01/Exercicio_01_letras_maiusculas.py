def maiusculas(frase):
    maiuscula = ''
    for caractere in frase.strip():
        if 65 <= ord(caractere) <= 90:
            maiuscula += caractere
    return maiuscula


# def test_maiusculas0():
#     assert maiusculas('Programamos em python 2?') == 'P'
#
#
# def test_maiusculas1():
#     assert maiusculas('Programamos em Python 3.') == 'PP'
#
#
# def test_maiusculas2():
#     assert maiusculas('PrOgRaMaMoS em python!') == 'PORMMS'
