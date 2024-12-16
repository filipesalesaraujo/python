largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
for i in range(altura):
    if i == 0 or i == altura - 1:
        print("#" * largura)
    else:
        print("#" + " " * (largura - 2) + "#")