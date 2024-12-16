numero = int(input("Digite um número inteiro: "))
anterior = -1
possui_igual = False

while numero > 0:
    atual = numero % 10
    if atual == anterior:
        possui_igual = True
        break
    anterior = atual
    numero //= 10

if possui_igual:
    print("sim")
else:
    print("não")