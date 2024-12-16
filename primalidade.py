numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print("não primo")
else:
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print("primo")
    else:
        print("não primo")