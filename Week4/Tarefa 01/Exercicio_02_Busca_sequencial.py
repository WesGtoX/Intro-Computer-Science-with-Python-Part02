def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False


# def test_busca_01():
#     assert busca(['a', 'e', 'i'], 'e') == 1
#
#
# def test_busca_02():
#     assert busca([12, 13, 14], 15) == False
#
#
# def test_busca_03():
#     test_lista = [3, 5, 23, 46, 62, 78, 85, 89, 92, 94, 104, 110, 120, 144, 161, 169, 170, 186, 192, 197]
#     assert busca(test_lista, 170) == 16
#
#
# def test_busca_04():
#     test_lista = [3, 29, 34, 48, 52, 63, 68, 92, 109, 128, 135, 163, 167, 178, 184]
#     assert busca(test_lista, 68) == 6
#
#
# def test_busca_05():
#     test_lista = [59, 66, 135, 108, 181, 9, 55, 10, 124, 153, 71, 177, 84, 26, 141]
#     assert busca(test_lista, 1000) == False
#
#
# def test_busca_06():
#     test_lista = [84, 105, 120, 178, 44, 70, 68, 19, 52, 79]
#     assert busca(test_lista, 1) == False
