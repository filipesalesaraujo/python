def computador_escolhe_jogada(n, m):
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    return m

def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        print("Oops! Jogada inválida! Tente de novo.")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("Você começa!")
        vez = "usuario"
    else:
        print("Computador começa!")
        vez = "computador"

    while n > 0:
        if vez == "computador":
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça(s).")
            vez = "usuario"
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça(s).")
            vez = "computador"
        
        n -= jogada
        if n > 0:
            print(f"Agora restam {n} peça(s) no tabuleiro.")
        else:
            print("Fim do jogo!", "O computador ganhou!" if vez == "usuario" else "Você ganhou!")

def campeonato():
    print("\nVoce escolheu um campeonato!")
    placar_computador = 0
    placar_usuario = 0
    
    for rodada in range(1, 4):
        print(f"\n**** Rodada {rodada} ****")
        partida()
        if input("Quem ganhou essa rodada? (computador/usuario): ").strip().lower() == "computador":
            placar_computador += 1
        else:
            placar_usuario += 1
    
    print("\n**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
opcao = int(input())

if opcao == 1:
    print("\nVoce escolheu uma partida isolada!")
    partida()
else:
    campeonato()
