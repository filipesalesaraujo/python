def menor_nome(nomes: list) -> str:
    nome_min = min([nome.strip() for nome in nomes], key=len)
    return nome_min.capitalize()
