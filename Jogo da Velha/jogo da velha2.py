

# Jogo da velha criado por https://github.com/vctrmacedo 

jogo = True
jogadas = ''
matriz = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

def display():
    for linha in range(3):
        for coluna in range(3):
                print(f'[{matriz[linha][coluna]}]', end=' ')
        print()

def tela():
    display()           
    player = 0
    while jogo:
        if player == 0:
            jogadas = input("Escolha a posição o jogador 1: ")
            if (jogadas[0] == '2' or  jogadas[0] == '0' or jogadas[0] == '1') and (jogadas[1] == '2' or  jogadas[1] == '0' or jogadas[1] == '1'):
                if  matriz[int(jogadas[0])][int(jogadas[1])] == ' ':
                    matriz[int(jogadas[0])][int(jogadas[1])] = 'X'
                    player = 1 
                    display()
                    vitoriaOuVelha()
                else:
                    print("Já houve uma jogada nesse local, tente novamente.")
            else: 
                print('Valor inválido para a jogada.')
        else:
            jogadas = input("Escolha a posição o jogador 2: ")
            if (jogadas[0] == '2' or  jogadas[0] == '0' or jogadas[0] == '1') and (jogadas[1] == '2' or  jogadas[1] == '0' or jogadas[1] == '1'):
                if  matriz[int(jogadas[0])][int(jogadas[1])] == ' ':
                    matriz[int(jogadas[0])][int(jogadas[1])] = 'O'
                    player = 0
                    display()
                    vitoriaOuVelha()
                else:
                    print("Já houve uma jogada nesse local, tente novamente.")
            else: 
                print('Valor inválido para a jogada.')


def menu():
    opcao = 1
    opcao = int(input("1 - Iniciar o jogo \n" + "2 - Sair do jogo \n" + "Escolha uma opção: " ))
    if opcao == 1:
        global matriz
        matriz = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
        tela()
    else:
        print("Saindo do jogo...")
        exit()

def vitoriaOuVelha():
    if      matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X' or \
            matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X' or \
            matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X' or \
            matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X' or \
            matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X' or \
            matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X' or \
            matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X' or \
            matriz[0][2] == 'X' and matriz[1][1] == 'X' and matriz[2][0] == 'X':
                print("Vitória do jogador 1!! Parabéns!!")
                menu()

    elif    matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O' or \
            matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O' or \
            matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O' or \
            matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O' or \
            matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O' or \
            matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O' or \
            matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O' or \
            matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O':
                print("Vitória do jogador 2!! Parabéns!!")
                menu()

    elif    matriz[0][0] != ' ' and matriz[0][1] != ' ' and matriz[0][2] != ' ' and \
            matriz[1][0] != ' ' and matriz[1][1] != ' ' and matriz[1][2] != ' ' and \
            matriz[2][0] != ' ' and matriz[2][1] != ' ' and matriz[2][2] != ' ' and \
            matriz[0][0] != ' ' and matriz[1][0] != ' ' and matriz[2][0] != ' ' and \
            matriz[0][1] != ' ' and matriz[1][1] != ' ' and matriz[2][1] != ' ' and \
            matriz[0][2] != ' ' and matriz[1][2] != ' ' and matriz[2][2] != ' ' and \
            matriz[0][0] != ' ' and matriz[1][1] != ' ' and matriz[2][2] != ' ' and \
            matriz[0][2] != ' ' and matriz[1][1] != ' ' and matriz[2][0] != ' ':
                print("############## Deu velha!! ##############") 
                menu()           
menu() 