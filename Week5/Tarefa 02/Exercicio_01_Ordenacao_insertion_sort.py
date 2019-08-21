def insertion_sort(lista):
    for i in range(len(lista)):
        while i != len(lista)-1 and lista[i] > lista[i+1]:
            lista[i+1], lista[i] = lista[i], lista[i+1]
            if i != 0:
                i -= 1
    return lista
