def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        resto = n % (m + 1)
        if resto > 0:
            return resto
        else:
            return m


def usuario_escolhe_jogada(n, m):
    jogadas = 0
    while jogadas < 1 or jogadas > n or jogadas > m:
        jogadas = int(input('Quantas peças?'))
    return jogadas


def partida():
    #n = 0
    #m = 0
    #while n < 1:
    n = int(input('Quantas peças?'))
    #while m < 1 or m > n:
    m = int(input('Limite de peças por jogada?'))

    # testar quem começa
    computer = True
    if n % (m + 1) == 0:
        computer = False
        print('\nVocê começa!\n')
    else:
        print('\nComputador começa!\n')

    while n > 0:
        if computer:
            retirar = computador_escolhe_jogada(n, m)
            computer = False
            print('O computador tirou {} peças.'.format(retirar))
        else:
            retirar = usuario_escolhe_jogada(n, m)
            computer = True
            print('Você tirou {} peças.'.format(retirar))

        # calcular quantas restam
        n = n - retirar
        if n > 0:
            print('Agora restam {} peças no tabuleiro.\n'.format(n))

    if computer:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0


def campeonato():
    usr = 0
    computer = 0

    for i in range(3):
        print('\n**** Rodada {} ****\n'.format(i + 1))
        win = partida()
        if win == 1:
            usr += 1
        else:
            computer += 1

    print(('\n**** Final do campeonato! ****\n\n'
           'Placar final: Você  {} x {}  Computador').format(usr, computer))


op = int(input('''Bem-vindo ao jogo do NIM! Escolha:\n
1 - para jogar uma partida isolada
2 - para jogar um campeonato'''))

if op == 1:
    resul = partida()
elif op == 2:
    campeonato()
