def imprime_matriz(minha_matriz):
    for i in range(len(minha_matriz)):
        for j in range(len(minha_matriz[0])):
            if j == len(minha_matriz[0]) - 1:
                print(str(minha_matriz[i][j]))
            else:
                print(str(minha_matriz[i][j]), end=' ')
