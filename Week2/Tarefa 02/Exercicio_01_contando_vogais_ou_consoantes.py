def conta_letras(frase, contar="vogais"):
    contar_vogais = 0
    contar_consoantes = 0
    vogais = 'aeiou'

    frase = frase.strip().lower()
    for letra in frase:
        if 97 <= ord(letra) <= 122:
            if letra in vogais:
                contar_vogais += 1
            else:
                contar_consoantes += 1
    return contar_vogais if contar == 'vogais' else contar_consoantes


# def test_contar_letras0():
#     assert conta_letras('programamos em python') == 6
#
#
# def test_contar_letras1():
#     assert conta_letras('programamos em python', 'vogais') == 6
#
#
# def test_contar_letras2():
#     assert conta_letras('programamos em python', 'consoantes') == 13
