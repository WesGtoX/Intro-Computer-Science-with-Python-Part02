def ordenada(lista):
    for i in range(len(lista)):
        if i < len(lista) - 1:
            if lista[i] > lista[i+1]:
                return False
    return True


# def test_ordenada_01():
#     test_lista = [3, 5, 23, 46, 62, 78, 85, 89, 92, 94, 104, 110, 120, 144, 161, 169, 170, 186, 192, 197]
#     assert ordenada(test_lista) == True
#
#
# def test_ordenada_02():
#     test_lista = [3, 29, 34, 48, 52, 63, 68, 92, 109, 128, 135, 163, 167, 178, 184]
#     assert ordenada(test_lista) == True
#
#
# def test_ordenada_03():
#     test_lista = [59, 66, 135, 108, 181, 9, 55, 10, 124, 153, 71, 177, 84, 26, 141]
#     assert ordenada(test_lista) == False
#
#
# def test_ordenada_04():
#     test_lista = [84, 105, 120, 178, 44, 70, 68, 19, 52, 79]
#     assert ordenada(test_lista) == False
#
#
# def test_ordenada_05():
#     test_lista = [10, 13, 21, 27, 45, 50, 51, 52, 54, 67, 70, 72, 73, 78, 80, 83, 85,]
#     assert ordenada(test_lista) == True
#
#
# def test_ordenada_06():
#     test_lista = [42, 164, 155, 70, 144, 183, 27, 31, 157, 68, 114, 197, 163, 73, 119, 192]
#     assert ordenada(test_lista) == False
