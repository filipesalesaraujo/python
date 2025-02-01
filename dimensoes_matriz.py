def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    print(f"{linhas}X{colunas}")

# Exemplos de chamada
minha_matriz1 = [[1], [2], [3]]
dimensoes(minha_matriz1)  # Saída esperada: 3X1

minha_matriz2 = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz2)  # Saída esperada: 2X3
