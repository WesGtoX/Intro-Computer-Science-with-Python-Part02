def ordena(lista):
    tamanho_lista = len(lista)

    for i in range(tamanho_lista - 1):
        menor_visto = i
        for j in range(i + 1, tamanho_lista):
            if lista[j] < lista[menor_visto]:
                menor_visto = j
        lista[i], lista[menor_visto] = lista[menor_visto], lista[i]
    return lista


# def lista_grande(n):
#     import random
#     lista_g = []
#     for i in range(n):
#         lista_g.append(random.randrange(9999))
#     return lista_g
#
#
# def ordenada(lista):
#     for i in range(len(lista)):
#         if i < len(lista) - 1:
#             if lista[i] > lista[i+1]:
#                 return False
#     return True
#
#
# def test_ordena_01():
#     assert ordenada(ordena(lista_grande(15))) == True
#
#
# def test_ordena_03():
#     assert ordenada(ordena(lista_grande(10))) == True
#
#
# def test_ordena_04():
#     assert ordenada(ordena(lista_grande(5))) == True
#
#
# def test_ordena_06():
#     assert ordenada(ordena(lista_grande(20))) == True
