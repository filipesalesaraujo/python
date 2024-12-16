numero = int(input("Digite um número inteiro: "))

if numero >= 10 or numero <= -10:
    digito_dezenas = abs(numero) // 10 % 10
else:
    digito_dezenas = 0

print(f"O dígito das dezenas é {digito_dezenas}")