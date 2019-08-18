class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            # inicialmente, o menor elemento ja visto é o i-esimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # coloca o menor elemento encontrado no inicio da sub-lista
            # para isso, troca de lugar os elemntos nas posicoes i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        return lista
