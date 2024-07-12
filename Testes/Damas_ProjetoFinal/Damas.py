import sys

# função para pular linhas.
def pular(x):
    print("\n" * x)

# função para printar traços seguidos, ex: "---".
def linha(x):
    print('_' * x)

# FUNÇÃO PARA PRINTAR O TABULEIRO
def apresentacao(matriz):
    print()
    for i in range(len(matriz) - 1):

        print('                  ', end='')
        linha(65)
        print('                  |', end='')

        for j in range(len(matriz[i])):
            print(matriz[i][j], end='')
        print()
    print()

def avaliar_dama(cont, linha, coluna, matriz): # função que avalia qual jogada o jogador da vez pode fazer, ou seja, avalia qual o movimento a Dama escolhida pode fazer.
    opcao = []
    opcao_comer = []

    if cont % 2 != 0:  # X ou ♕ =======================================================================================
        if matriz[linha - 1][coluna + 1] == '|     |':
            opcao.append([linha - 1, coluna + 1])

        elif matriz[linha - 1][coluna + 1] == '|  O  |' or matriz[linha - 1][coluna + 1] == '|  ♔  |':
            if matriz[linha - 2][coluna + 2] == '|     |':
                opcao_comer.append([linha - 2, coluna + 2])

        if matriz[linha - 1][coluna - 1] == '|     |':
            opcao.append([linha - 1, coluna - 1])

        elif matriz[linha - 1][coluna - 1] == '|  O  |' or matriz[linha - 1][coluna - 1] == '|  ♔  |':
            if matriz[linha - 2][coluna - 2] == '|     |':
                opcao_comer.append([linha - 2, coluna - 2])

        if matriz[linha + 1][coluna + 1] == '|     |':
            opcao.append([linha + 1, coluna + 1])

        elif matriz[linha + 1][coluna + 1] == '|  O  |' or matriz[linha + 1][coluna + 1] == '|  ♔  |':
            if matriz[linha + 2][coluna + 2] == '|     |':
                opcao_comer.append([linha + 2, coluna + 2])

        if matriz[linha + 1][coluna - 1] == '|     |':
            opcao.append([linha + 1, coluna - 1])

        elif matriz[linha + 1][coluna - 1] == '|  O  |' or matriz[linha + 1][coluna - 1] == '|  ♔  |':
            if matriz[linha + 2][coluna - 2] == '|     |':
                opcao_comer.append([linha + 2, coluna - 2])

    if cont % 2 == 0:  # O ou ♔ =======================================================================================
        if matriz[linha - 1][coluna + 1] == '|     |':
            opcao.append([linha - 1, coluna + 1])

        elif matriz[linha - 1][coluna + 1] == '|  X  |' or matriz[linha - 1][coluna + 1] == '|  ♕  |':
            if matriz[linha - 2][coluna + 2] == '|     |':
                opcao_comer.append([linha - 2, coluna + 2])

        if matriz[linha - 1][coluna - 1] == '|     |':
            opcao.append([linha - 1, coluna - 1])

        elif matriz[linha - 1][coluna - 1] == '|  X  |' or matriz[linha - 1][coluna - 1] == '|  ♕  |':
            if matriz[linha - 2][coluna - 2] == '|     |':
                opcao_comer.append([linha - 2, coluna - 2])

        if matriz[linha + 1][coluna + 1] == '|     |':
            opcao.append([linha + 1, coluna + 1])

        elif matriz[linha + 1][coluna + 1] == '|  X  |' or matriz[linha + 1][coluna + 1] == '|  ♕  |':
            if matriz[linha + 2][coluna + 2] == '|     |':
                opcao_comer.append([linha + 2, coluna + 2])

        if matriz[linha + 1][coluna - 1] == '|     |':
            opcao.append([linha + 1, coluna - 1])

        elif matriz[linha + 1][coluna - 1] == '|  X  |' or matriz[linha + 1][coluna - 1] == '|  ♕  |':
            if matriz[linha + 2][coluna - 2] == '|     |':
                opcao_comer.append([linha + 2, coluna - 2])


    if len(opcao_comer) > 0:
        return opcao_comer
    else:
        return opcao

# função que avalia qual jogada o jogador da vez pode fazer, ou seja, avalia qual o movimento a peça escolhida pode fazer.
def avaliar_jogada(cont, linha, coluna, matriz):
    opcao = []
    opcao_comer = []

    if cont % 2 != 0: # X
        if matriz[linha - 1][coluna + 1] == '|     |':
            opcao.append([linha - 1, coluna + 1])

        elif matriz[linha - 1][coluna + 1] == '|  O  |':
            if matriz[linha - 2][coluna + 2] == '|     |':
                opcao_comer.append([linha - 2, coluna + 2])

        if matriz[linha - 1][coluna - 1] == '|     |':
            opcao.append([linha - 1, coluna - 1])
        elif matriz[linha - 1][coluna - 1] == '|  O  |':
            if matriz[linha - 2][coluna - 2] == '|     |':
                opcao_comer.append([linha - 2, coluna - 2])

    elif cont % 2 == 0: # BOLA
        if matriz[linha + 1][coluna + 1] == '|     |':
            opcao.append([linha + 1, coluna + 1])
        elif matriz[linha + 1][coluna + 1] == '|  X  |':
            if matriz[linha + 2][coluna + 2] == '|     |':
                opcao_comer.append([linha + 2, coluna + 2])

        if matriz[linha + 1][coluna - 1] == '|     |':
            opcao.append([linha + 1, coluna - 1])
        elif matriz[linha + 1][coluna - 1] == '|  X  |':
            if matriz[linha + 2][coluna - 2] == '|     |':
                opcao_comer.append([linha + 2, coluna - 2])

    # Se houver a opção de "comer" alguma peça, é retornada a lista opçao_comer, se não retorna a lista opcao que tem como elementos a movimentação básica da peça.
    if len(opcao_comer) > 0:
        return opcao_comer
    else:
        return opcao

# função que define qual é o jogador da vez de acordo com o número de jogadas
def jogadores(jogadas):
    if jogadas % 2 == 0:  # O é par
        jogador = 'O'
    else:
        jogador = 'X'  # X é ímpar

    return jogador

def posicao():
    while True:
        nova_posicao = input('♦ Escolha uma nova posição para a peça escolhida: ').split()

        try:
            coluna_nova_posicao, linha_nova_posicao = int(nova_posicao[0]), int(
                nova_posicao[1])  # Valores de posição do local de destino escolhido pelo jogador.
            break

        except:
            print(
                '\nPosição inválida. Por favor, informande a linha (horizontal) e a coluna (vertical), respectivamente, separadas por um espaço. Exemplo: "1 2".')
            continue

    return coluna_nova_posicao, linha_nova_posicao

def jogo():


    # FORMAÇÃO INICIAL DO TABULEIRO8 8
    matriz = [['L ↓|C →', '|  1  |', '|  2  |', '|  3  |', '|  4  |', '|  5  |', '|  6  |', '|  7  |', '|  8  |', '|'],
              ['|  1  |', '|  O  |', '|     |', '|  O  |', '|     |', '|  O  |', '|     |', '|  O  |', '|     |', '|'],
              ['|  2  |', '|     |', '|  O  |', '|     |', '|  O  |', '|     |', '|  O  |', '|     |', '|  O  |', '|'],
              ['|  3  |', '|  O  |', '|     |', '|  O  |', '|     |', '|  O  |', '|     |', '|  O  |', '|     |', '|'],
              ['|  4  |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|'],
              ['|  5  |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|'],
              ['|  6  |', '|     |', '|  X  |', '|     |', '|  X  |', '|     |', '|  X  |', '|     |', '|  X  |', '|'],
              ['|  7  |', '|  X  |', '|     |', '|  X  |', '|     |', '|  X  |', '|     |', '|  X  |', '|     |', '|'],
              ['|  8  |', '|     |', '|  X  |', '|     |', '|  X  |', '|     |', '|  X  |', '|     |', '|  X  |', '|'],
              ['       ', '       ', '       ', '       ', '       ', '       ', '       ', '       ', '       ', ' ']]

    print('\n======================================== ▼ VAMOS  COMEÇAR ▼ ========================================')
    apresentacao(matriz)
    linha(100)
    print('Vez de X ou ♕                                                                      Nº de Jogadas = 0\n')
    contador_comidas, comparacao, contagem_jogadas, pecas_x, pecas_o, jogadas, contagem_jogador, verificacao, encerramento = 0, 0, 0, 0, 0, 0, 0, 0, False  # Contadores

    numeros_corretos = [1, 2, 3, 4, 5, 6, 7, 8, '1', '2', '3', '4', '5', '6', '7', '8']

    while True:
        if encerramento == True:
            break

        contagem_jogador += 1
        jogadas += 1

        # ESCOLHENDO A PEÇA
        while True:

            if encerramento == True:
                break

            jogador = jogadores(jogadas)  # Jogador da vez
            peca_dama = 0
            if jogador == 'O':
                peca_dama = '♕'
                peca_invertida = '♔'

            elif jogador == 'X':
                peca_dama = '♔'
                peca_invertida = '♕'

            if verificacao != 0:
                peca_escolhida = verificacao
                print("Você deve comer novamente! Por favor, escolha a nova posição.")
                verificacao = 0
            else:
                peca_escolhida = input('♦ Escolha uma peça para movimentar: ').split()

            try:
                peca_escolhida[0] = peca_escolhida[0].lower()

            except:
                print('\nSem entrada. Escolha novamente.')
                continue

            # Condição de parada
            if peca_escolhida[0] == 'sair':
                print('\nSe desejar continuar:')
                print('\nOpção 1: Jogar novamente\nOpção 2: Ler as Instruções\nOpção 3: Ver os créditos\nOpção 4: Sair do jogo\n')

                encerramento = True
                break

            if peca_escolhida[0] not in numeros_corretos or peca_escolhida[1] not in numeros_corretos:
                print('\nOs números de linha e coluna só vão de 0 até 9. Por favor, informe dois valores neste intervalo.')
                continue

            try:
                linha_peca_escolhida, coluna_peca_escolhida = int(peca_escolhida[0]), int(peca_escolhida[1])  # Valores de posição da peça escolhida

            except:
                print('\nPosição inválida. Por favor, informande a linha (horizontal) e a coluna (vertical), respectivamente, separadas por um espaço. Exemplo: "1 2".')
                continue

            # Condição de se a dama vai se movimentar
            if matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♔  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♕  |':
                # Matriz com posições que o jogador pode se mover. Pode ter tamanho 4, 3, 2, 1 ou 0.
                matriz_movimentacao = avaliar_dama(jogadas, linha_peca_escolhida, coluna_peca_escolhida, matriz)

            # Condição de se o X ou a O vai se movimentar
            elif matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  X  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  O  |':
                # Matriz com posições que o jogador pode se mover. Pode ter tamanho 2, 1 ou 0.
                matriz_movimentacao = avaliar_jogada(jogadas, linha_peca_escolhida, coluna_peca_escolhida, matriz)

            # Condição para quando a peça não puder se mover
            if len(matriz_movimentacao) == 0:
                if jogador == 'X' and matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  X  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] != '|  ♕  |':
                    print('\nA peça escolhida não pode ser movimentada, tente outra vez.')
                    continue

                if jogador == 'O' and matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  O  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♔  |':
                    print('\nA peça escolhida não pode ser movimentada, tente outra vez.')
                    continue

            # Condição para se o jogador escolher alguma parte do tabuleiro onde não há peças.
            if matriz[linha_peca_escolhida][coluna_peca_escolhida] != '|  X  |' and matriz[linha_peca_escolhida][coluna_peca_escolhida] != '|  O  |' and matriz[linha_peca_escolhida][coluna_peca_escolhida] != '|  ♔  |' and matriz[linha_peca_escolhida][coluna_peca_escolhida] != '|  ♕  |':
                print("\nPEÇA INVÁLIDA, TENTE OUTRA VEZ.")
                continue

            # Avaliação se o jogador está escolhendo a sua peça ou a do oponente.
            if jogador == 'O':
                if matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  O  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♔  |':
                    break

                else:
                    print('\nVocê escolheu a peça do seu oponente. Escolha as peças com %s ou %s' % (jogador, peca_invertida))
                    continue

            elif jogador == 'X':
                if matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  X  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♕  |':
                    break

                else:
                    print('\nVocê escolheu a peça do seu oponente. Escolha as peças com %s ou %s' % (jogador, peca_invertida))
                    continue

        print()

        # ESCOLHENDO A NOVA POSIÇÃO DA PEÇA

        movimentacao = False  # verificar se a nova posição é válida

        while movimentacao != True:

            if encerramento == True:
                break

            coluna_nova_posicao, linha_nova_posicao = posicao()

            comer_dnv = [] # lista com posições em que as peças podem comer novamente

            if len(matriz_movimentacao) == 4:
                a = avaliar_dama(jogadas, matriz_movimentacao[0][0], matriz_movimentacao[0][1], matriz)
                b = avaliar_dama(jogadas, matriz_movimentacao[1][0], matriz_movimentacao[1][1], matriz)
                c = avaliar_dama(jogadas, matriz_movimentacao[2][0], matriz_movimentacao[2][1], matriz)
                d = avaliar_dama(jogadas, matriz_movimentacao[3][0], matriz_movimentacao[3][1], matriz)

                comer_dnv.append(a), comer_dnv.append(b), comer_dnv.append(c), comer_dnv.append(d)


            elif len(matriz_movimentacao) == 3:
                a = avaliar_dama(jogadas, matriz_movimentacao[0][0], matriz_movimentacao[0][1], matriz)
                b = avaliar_dama(jogadas, matriz_movimentacao[1][0], matriz_movimentacao[1][1], matriz)
                c = avaliar_dama(jogadas, matriz_movimentacao[2][0], matriz_movimentacao[2][1], matriz)

                comer_dnv.append(a), comer_dnv.append(b), comer_dnv.append(c)


            elif len(matriz_movimentacao) == 2 and (matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  X  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  O  |'):
                a = avaliar_jogada(jogadas, matriz_movimentacao[0][0], matriz_movimentacao[0][1], matriz)
                b = avaliar_jogada(jogadas, matriz_movimentacao[1][0], matriz_movimentacao[1][1], matriz)
                comer_dnv.append(a), comer_dnv.append(b)

            elif len(matriz_movimentacao) == 2 and (matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♕  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♔  |'):
                a = avaliar_dama(jogadas, matriz_movimentacao[0][0], matriz_movimentacao[0][1], matriz)
                b = avaliar_dama(jogadas, matriz_movimentacao[1][0], matriz_movimentacao[1][1], matriz)
                comer_dnv.append(a), comer_dnv.append(b)


            elif len(matriz_movimentacao) == 1 and (matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  X  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  O  |'):
                a = avaliar_jogada(jogadas, matriz_movimentacao[0][0], matriz_movimentacao[0][1], matriz)
                comer_dnv.append(a)

            elif len(matriz_movimentacao) == 1 and (matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♕  |' or matriz[linha_peca_escolhida][coluna_peca_escolhida] == '|  ♔  |'):
                a = avaliar_dama(jogadas, matriz_movimentacao[0][0], matriz_movimentacao[0][1], matriz)
                comer_dnv.append(a)


            comer_dnv = comer_dnv[0]

            contador_comidas = 0

            # AVALIANDO A JOGADA
            if len(matriz_movimentacao) == 4:
                if (linha_nova_posicao == matriz_movimentacao[0][1] or linha_nova_posicao == matriz_movimentacao[1][1] or linha_nova_posicao == matriz_movimentacao[2][1] or linha_nova_posicao == matriz_movimentacao[3][1]) and (coluna_nova_posicao == matriz_movimentacao[0][0] or coluna_nova_posicao == matriz_movimentacao[1][0] or coluna_nova_posicao == matriz_movimentacao[2][0] or coluna_nova_posicao == matriz_movimentacao[3][0]):
                    # Se o local de destino escolhido pelo jogador for um local vazio e que esteja na diagonal direita ou esquerda a frente da peça, a movimentação é PERMITIDA.
                    movimentacao = True

                else:
                    # Se o jogador escolher uma posição que não seja um local vazio ou que não esteja na diagonal direita ou esquerda a frente da peça, a movimentação é NÃO É PERMITIDA.
                    print('\nDe acordo com as regras do jogo, você não pode se mover para esta posição. Por favor, escolha entre a posição:', matriz_movimentacao[0], ',', matriz_movimentacao[1], ',', matriz_movimentacao[2], 'ou', matriz_movimentacao[3])
                    continue

            if len(matriz_movimentacao) == 3:
                if (linha_nova_posicao == matriz_movimentacao[0][1] or linha_nova_posicao == matriz_movimentacao[1][1] or linha_nova_posicao == matriz_movimentacao[2][1]) and (coluna_nova_posicao == matriz_movimentacao[0][0] or coluna_nova_posicao == matriz_movimentacao[1][0] or coluna_nova_posicao == matriz_movimentacao[2][0]):
                    # Se o local de destino escolhido pelo jogador for um local vazio e que esteja na diagonal direita ou esquerda a frente da peça, a movimentação é PERMITIDA.
                    movimentacao = True

                else:
                    # Se o jogador escolher uma posição que não seja um local vazio ou que não esteja na diagonal direita ou esquerda a frente da peça, a movimentação é NÃO É PERMITIDA.
                    print('\nDe acordo com as regras do jogo, você não pode se mover para esta posição. Por favor, escolha entre a posição:', matriz_movimentacao[0], ',', matriz_movimentacao[1], 'ou', matriz_movimentacao[2])
                    continue

            if len(matriz_movimentacao) == 2:  # Se o jogador tiver duas casas vazias como opção de movimento.

                if (linha_nova_posicao == matriz_movimentacao[0][1] or linha_nova_posicao == matriz_movimentacao[1][1]) and (coluna_nova_posicao == matriz_movimentacao[0][0] or coluna_nova_posicao == matriz_movimentacao[1][0]):
                    # Se o local de destino escolhido pelo jogador for um local vazio e que esteja na diagonal direita ou esquerda a frente da peça, a movimentação é PERMITIDA.
                    movimentacao = True

                else:
                    # Se o jogador escolher uma posição que não seja um local vazio ou que não esteja na diagonal direita ou esquerda a frente da peça, a movimentação é NÃO É PERMITIDA.
                    print('\nDe acordo com as regras do jogo, você não pode se mover para esta posição. Por favor, escolha entre a posição:', matriz_movimentacao[0], 'ou', matriz_movimentacao[1])
                    continue

            if len(matriz_movimentacao) == 1:  # Se o jogador tiver apenas uma casa vazia como opção de movimento.

                if linha_nova_posicao == matriz_movimentacao[0][1] and coluna_nova_posicao == matriz_movimentacao[0][0]:
                    # Se o local de destino escolhido pelo jogador for um local vazio e que esteja na diagonal direita ou esquerda a frente da peça, a movimentação é PERMITIDA.
                    movimentacao = True

                else:
                    # Se o jogador escolher uma posição que não seja um local vazio ou que não esteja na diagonal direita ou esquerda a frente da peça, a movimentação é NÃO É PERMITIDA.
                    print(
                        '\nDe acordo com as regras do jogo, você não pode se mover para esta posição. Por favor, escolha a posição',
                        matriz_movimentacao[0])
                    continue
        if encerramento == True:
            break

        # MOVENDO AS PEÇAS

        """
        A lógica utilizada para a movimentação é a remoção do local escolhido para a peça ir, depois é feita uma cópia da peça escolhida para ser inserida no novo local. Após isso é removida a peça inicialmente escolhida e colocado um espaço vazio em seu local.
        """
        matriz[coluna_nova_posicao].pop(linha_nova_posicao)  # remove o local onde a peça irá ficar

        if jogador == 'X' and coluna_nova_posicao == 1:
            matriz[coluna_nova_posicao].insert(linha_nova_posicao, '|  ♕  |')

        elif jogador == 'O' and coluna_nova_posicao == 8:
            matriz[coluna_nova_posicao].insert(linha_nova_posicao, '|  ♔  |')

        else:
            matriz[coluna_nova_posicao].insert(linha_nova_posicao, matriz[linha_peca_escolhida][coluna_peca_escolhida])  # insere uma cópia da peça escolhida na posição escolhida

        matriz[linha_peca_escolhida].pop(coluna_peca_escolhida)  # remove a peça escolhida originalmente

        matriz[linha_peca_escolhida].insert(coluna_peca_escolhida,
                                            '|     |')  # coloca um espaço vazio onde a peça escolhida estava anteriormente

        if (linha_nova_posicao == (coluna_peca_escolhida + 2)) and (coluna_nova_posicao == (linha_peca_escolhida - 2)):  # funciona quando x come pela direita

            matriz[linha_peca_escolhida - 1].pop(coluna_peca_escolhida + 1)  # remove a peça do oponente
            matriz[linha_peca_escolhida - 1].insert((coluna_peca_escolhida + 1), '|     |')

            pecas_o += 1  # soma 1 na variavel de peças_o quando o x "come" uma peça do oponente
            contador_comidas += 1

        elif (linha_nova_posicao == (coluna_peca_escolhida - 2)) and (coluna_nova_posicao == (linha_peca_escolhida - 2)):  # funciona quando x come pela esquerda
            matriz[linha_peca_escolhida - 1].pop(coluna_peca_escolhida - 1)  # remove a peça do oponente
            matriz[linha_peca_escolhida - 1].insert((coluna_peca_escolhida - 1), '|     |')

            pecas_o += 1  # soma 1 na variavel de peças_o quando o x "come" uma peça do oponente
            contador_comidas += 1

        elif (coluna_nova_posicao == (linha_peca_escolhida + 2)) and (linha_nova_posicao == (coluna_peca_escolhida + 2)):  # funciona quando O "come" pela direita
            matriz[linha_peca_escolhida + 1].pop(coluna_peca_escolhida + 1)  # remove a peça do oponente
            matriz[linha_peca_escolhida + 1].insert((coluna_peca_escolhida + 1), '|     |')

            pecas_x += 1  # soma 1 na variavel de peças_x quando O "come" uma peça do oponente
            contador_comidas += 1

        elif (coluna_nova_posicao == (linha_peca_escolhida + 2)) and (linha_nova_posicao == (coluna_peca_escolhida - 2)):  # funciona quando O "come" pela esquerda
            matriz[linha_peca_escolhida + 1].pop(coluna_peca_escolhida - 1)  # remove a peça do oponente
            matriz[linha_peca_escolhida + 1].insert((coluna_peca_escolhida - 1), '|     |')

            pecas_x += 1  # soma 1 na variavel de peças_x quando O "come" uma peça do oponente
            contador_comidas += 1

        if comparacao != contador_comidas:
            if len(comer_dnv) == 4:
                if coluna_nova_posicao == comer_dnv[0][0] + 2 or coluna_nova_posicao == comer_dnv[0][
                    0] - 2 or coluna_nova_posicao == comer_dnv[1][0] - 2 or coluna_nova_posicao == comer_dnv[1][
                    0] + 2 or coluna_nova_posicao == comer_dnv[2][0] + 2 or coluna_nova_posicao == comer_dnv[2][
                    0] - 2 or coluna_nova_posicao == comer_dnv[3][0] + 2 or coluna_nova_posicao == comer_dnv[3][0] - 2:
                    verificacao = [str(coluna_nova_posicao), str(linha_nova_posicao)]
                    jogadas -= 1
                    contagem_jogador -= 1

            elif len(comer_dnv) == 3:
                if coluna_nova_posicao == comer_dnv[0][0] + 2 or coluna_nova_posicao == comer_dnv[0][
                    0] - 2 or coluna_nova_posicao == comer_dnv[1][0] - 2 or coluna_nova_posicao == comer_dnv[1][
                    0] + 2 or coluna_nova_posicao == comer_dnv[2][0] + 2 or coluna_nova_posicao == comer_dnv[2][0] - 2:
                    verificacao = [str(coluna_nova_posicao), str(linha_nova_posicao)]
                    jogadas -= 1
                    contagem_jogador -= 1

            elif len(comer_dnv) == 2:
                if coluna_nova_posicao == comer_dnv[0][0] + 2 or coluna_nova_posicao == comer_dnv[0][
                    0] - 2 or coluna_nova_posicao == comer_dnv[1][0] - 2 or coluna_nova_posicao == comer_dnv[1][0] + 2:
                    verificacao = [str(coluna_nova_posicao), str(linha_nova_posicao)]
                    jogadas -= 1
                    contagem_jogador -= 1

            elif len(comer_dnv) == 1:
                if coluna_nova_posicao == comer_dnv[0][0] + 2 or coluna_nova_posicao == comer_dnv[0][0] - 2:
                    jogadas -= 1
                    contagem_jogador -= 1
                    verificacao = [str(coluna_nova_posicao), str(linha_nova_posicao)]

        vez = jogadores(contagem_jogador - 1)

        # Apresentação da matriz após uma jogada efetuada.
        pular(10)
        apresentacao(matriz)
        pular(3)
        print('\n==================================================================================================')

        contagem_jogadas += 1
        if pecas_o != 12 and pecas_x != 12:
            print(
                'Vez de %s ou %s                                                                   Nº de Jogadas = %d\n' % (
                vez, peca_dama, contagem_jogadas))

        if pecas_o == 12:
            print("ACABOU O JOGO.\n")
            print("♔ ♕ ♚ ♛ PARABÉNS JOGADOR X, VOCÊ GANHOU! ♛ ♚ ♕ ♔")
            print('\nSe desejar continuar:')
            print('Opção 1: Jogar novamente\nOpção 2: Ler as Instruções\nOpção 3: Ver os créditos\nOpção 4: Sair do jogo\n')
            encerramento = True

        if pecas_x == 12:
            print("ACABOU O JOGO.\n")
            print("♔ ♕ ♚ ♛ PARABÉNS JOGADOR O, VOCÊ GANHOU! ♛ ♚ ♕ ♔")
            print('\nSe desejar continuar:\n')
            print('Opção 1: Jogar novamente\nOpção 2: Ler as Instruções\nOpção 3: Ver os créditos\nOpção 4: Sair do jogo\n')
            encerramento = True

def instrucoes():
    # INSTRUÇÕES DO JOGO
    print()
    print('INSTRUÇÕES:\n')
    print('1º - O jogo de damas é praticado entre dois parceiros, com 12 pedras brancas (representadas aqui por "X)" de um lado e com 12 pedras pretas de outro lado (representadas aqui por "O"). O lance inicial cabe sempre a quem estiver com as peças brancas (X).')
    print('2º - O objetivo do jogo é imobilizar ou capturar todas as peças do adversário com suas pedras. As pedras iniciais podem andar e comer apenas em direção a área inimiga e fazendo movimentos em diagonal.')
    print('3º - Ao alcançar a linha mais interna da áera de seu oponente, o jogador transforma a peça em uma Dama. As Damas podem andar e comer peças para cima e para baixo em diagonal andando um quadrado por vez, assim como as iniciais.')
    print('\nCOMO JOGAR:\n')
    print('1º - Faça a seleção de peças e da nova posição informando a linha (horizontal) e a coluna (vertical), respectivamente, separadas por um espaço. Exemplo: "1 2".\n')
    print('2º - Escreva "sair" na opção de escolher uma peça a qualquer momento para acabar com o jogo.')
    linha(100)
    print('\nOpção 1: Jogar Damas\nOpção 3: Ver os créditos\nOpção 4: Sair do jogo\n')

def creditos():

    print('\nCRÉDITOS:')
    print('\nInstituição: IFPB - Campus Campina Grande')
    print('\nProjeto de conclusão da cadeira de algoritmos e programação - Turma 2019.2')
    print('\nDesenvolvedores:\n')
    print(' ♕  Maria Eduarda Cunha Silva Araújo\n')
    print(' ♔  Rafael Victor Cordeiro Muniz')
    print('\nDesenvolvido em Dezembro de 2019 ')
    linha(100)
    print('\nOpção 1: Jogar Damas\nOpção 2: Ler as Instruções\nOpção 4: Sair do jogo\n')


print()
print('                              =========================================')
print('                  =================================================================')
print('         ================================== ♕  D A M A S ♕ =================================')
print('                  =================================================================')
print('                              =========================================')

print('\n                                         BEM VINDO, JOGADOR!\n')

print('Para começarmos escolha alguma opção, por favor:\n')
print('Opção 1: Jogar Damas\nOpção 2: Ler as Instruções\nOpção 3: Ver os créditos\nOpção 4: Sair do jogo\n')


opcoes = list(range(1, 5))

while True:

    try:
        opcao = int(input('Digite a opção desejada: '))
        linha(100)
    except:
        print('\nEntrada inválida. Por favor, tente novamente.')
        continue


    if opcao not in opcoes:
        print('\nEntrada inválida. Por favor, tente novamente.')
        continue

        # 1 = Jogar
        # 2 = Intruções
        # 3 = Créditos
        # 4 = Sair
        # Nome do jogo

    if opcao == 1:
        jogo()

    elif opcao == 2:
        instrucoes()

    elif opcao == 3:
        creditos()

    elif opcao == 4:
        print('\n ♕  ♔  OBRIGADO POR JOGAR, VOLTE SEMPRE. ♔  ♕\n')
        break
