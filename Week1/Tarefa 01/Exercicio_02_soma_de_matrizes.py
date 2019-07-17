def soma_matrizes(m1, m2):
    lin1, col1 = len(m1), len(m1[0])
    lin2, col2 = len(m2), len(m2[0])

    if lin1 == lin2 and col1 == col2:
        matriz_soma = []
        for i in range(lin1):
            linha = []
            for j in range(col1):
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)
            matriz_soma.append(linha)
        return matriz_soma
    else:
        return False