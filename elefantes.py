def incomodam(n):
    if n <= 0:
        return ""
    return "incomodam " + incomodam(n - 1)

def elefantes(n):
    if n <= 1:
        return ""
    if n == 2:
        return "Um elefante incomoda muita gente\n2 elefantes " + incomodam(2) + "muito mais"

    parte_anterior = elefantes(n - 1)
    linha_1 = f"\n{n-1} elefantes incomodam muita gente"
    linha_2 = f"\n{n} elefantes " + incomodam(n) + "muito mais"

    return parte_anterior + linha_1 + linha_2
