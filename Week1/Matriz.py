def cria_matriz(num_linhas, num_colunas):
    '''
    (int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas
    em que cada elemento é igual ao valor dado.
    '''
    matriz = [] # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        # adiciona linha à matriz
        matriz.append(linha)
    return matriz


def imprimir_matriz(num_linhas, num_colunas):
    matriz = cria_matriz(num_linhas, num_colunas)
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(str(matriz[i][j]), end='\t')
        print('')

def main():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    imprimir_matriz(lin, col)

main()