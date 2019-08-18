import random


def lista_grande(n):
    lista_g = []
    for i in range(n):
        lista_g.append(random.randrange(9999))
    return lista_g
