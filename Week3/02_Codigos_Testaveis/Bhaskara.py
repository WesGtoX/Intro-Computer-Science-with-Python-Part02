import math


class Bhaskara:

    def delta(self, a, b, c):
        return (b ** 2) - (4 * a * c)

    def main(self):
        a_dig = float(input("Digite o valor de a: "))
        b_dig = float(input("Digite o valor de b: "))
        c_dig = float(input("Digite o valor de c: "))
        print(self.calcula_raizes(a_dig, b_dig, c_dig))

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            x = (- b + math.sqrt(d)) / (2 * a)
            # print("A única raiz é: ", x)
            return 1, x
        else:
            if d < 0:
                # print("Esta equação nao possui raizes reais")
                return 0
            else:
                x1 = (- b + math.sqrt(d)) / (2 * a)
                x2 = (- b - math.sqrt(d)) / (2 * a)
                return 2, x1, x2
                # print("A primeira raiz é: ", x1)
                # print("A segunda raiz é: ", x2)
