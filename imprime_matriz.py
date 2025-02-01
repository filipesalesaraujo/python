def imprime_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(elemento) for elemento in linha))

# Exemplos de chamada
minha_matriz1 = [[1], [2], [3]]
imprime_matriz(minha_matriz1)  # Saída esperada:
# 1
# 2
# 3

minha_matriz2 = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz2)  # Saída esperada:
# 1 2 3
# 4 5 6
