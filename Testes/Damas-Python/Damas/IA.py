from copy import deepcopy
from Variaveis import branco, preto

class IA:
    def minimax(self,posicao, profundidade, max_jogador, jogo):
        if profundidade == 0 or posicao.ganhador() is not None:
            return posicao.avaliar(), posicao
        if max_jogador:
            maxAvaliada = float('-inf')
            melhor_movimento = None
            for mov in IA().pegar_todos_mov(posicao, branco, jogo):
                avaliado = IA().minimax(mov, profundidade - 1, False, jogo)[0]
                maxAvaliada = max(maxAvaliada, avaliado)
                if maxAvaliada == avaliado:
                    melhor_movimento = mov
            return maxAvaliada, melhor_movimento
        else:
            minAvaliada = float('inf')
            melhor_movimento = None
            for mov in IA().pegar_todos_mov(posicao, preto, jogo):
                avaliado = IA().minimax(mov, profundidade - 1, True, jogo)[0]
                minAvaliada = min(minAvaliada, avaliado)
                if minAvaliada == avaliado:
                    melhor_movimento = mov
            return minAvaliada, melhor_movimento

    def simular_mov(self,peca, mov, tabuleiro, jogo, passar):
        tabuleiro.mov(peca, mov[0], mov[1])
        if passar:
            tabuleiro.remover(passar)
        return tabuleiro

    def pegar_todos_mov(self,tabuleiro, cor, jogo):
        movs = []
        for peca in tabuleiro.contar_pecas(cor):
            valido_movim = tabuleiro.pegar_movimento_validos(peca)
            for mov, passar in valido_movim.items():
                tabul_tempor = deepcopy(tabuleiro)
                peca_tempor = tabul_tempor.pegar_peca(peca.linha, peca.coluna)
                novo_tabuleiro = IA().simular_mov(peca_tempor, mov, tabul_tempor, jogo, passar)
                movs.append(novo_tabuleiro)
        return movs


