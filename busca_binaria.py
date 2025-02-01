def busca(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(meio)
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False
