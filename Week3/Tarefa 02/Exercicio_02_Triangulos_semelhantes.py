class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        lado1 = sorted([self.a, self.b, self.c])
        lado2 = sorted([triangulo.a, triangulo.b, triangulo.c])

        if lado1[0] > lado2[0]:
            l_maior, l_menor = lado1, lado2
        else:
            l_maior, l_menor = lado2, lado1

        if l_maior[0] % l_menor[0] == l_maior[1] % l_menor[1] == l_maior[2] % l_menor[2]:
            return True
        else:
            return False
