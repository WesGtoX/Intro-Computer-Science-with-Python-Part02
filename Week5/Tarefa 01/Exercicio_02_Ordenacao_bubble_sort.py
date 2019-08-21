def bubble_sort(lista):
    fim = len(lista)

    for i in range(fim-1, 0, -1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
                trocou = True
        if not trocou:
            return lista
    return lista


# print(bubble_sort([5, 1, 4, 2]))
# [1, 5, 4, 2]
# [1, 4, 5, 2]
# [1, 4, 2, 5]
# [1, 2, 4, 5]
# [1, 2, 4, 5] deve devolver
