def ordena(lista):
    for i in range(len(lista)):
        pos_menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i], lista[pos_menor] = lista[pos_menor], lista[i]
    return lista
