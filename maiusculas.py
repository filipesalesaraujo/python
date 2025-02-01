def maiusculas(frase: str) -> str:
    return "".join([char for char in frase if 'A' <= char <= 'Z'])
