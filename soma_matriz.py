def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or any(len(linha1) != len(linha2) for linha1, linha2 in zip(m1, m2)):
        return False

    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

# Exemplos de chamada
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))  # Saída esperada: [[3, 5, 7], [9, 11, 13]]

m1 = [[1], [2], [3]]
m2 = [[2, 3], [4, 5], [6, 7]]
print(soma_matrizes(m1, m2))  # Saída esperada: False
