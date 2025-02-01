def conta_letras(frase: str, contar: str = "vogais") -> int:
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    if contar == "vogais":
        return sum(1 for letra in frase if letra in vogais)
    elif contar == "consoantes":
        return sum(1 for letra in frase if letra in consoantes)
    else:
        raise ValueError("O parâmetro 'contar' deve ser 'vogais' ou 'consoantes'.")
