from Variaveis import *


class Jogo:
    # Classe para tomar conta do status do jogo
    def __init__(self):
        self.status = 'Jogando'
        self.turno = 1
        self.jogadores = ('x', 'o')
        self.cedula_selecionada = None
        self.pulando = False
        self.matriz_jogadores = [['x','-','x','-','x','-','x','-'],
                                ['-','x','-','x','-','x','-','x'],
                                ['x','-','x','-','x','-','x','-'],
                                ['-','-','-','-','-','-','-','-'],
                                ['-','-','-','-','-','-','-','-'],
                                ['-','o','-','o','-','o','-','o'],
                                ['o','-','o','-','o','-','o','-'],
                                ['-','o','-','o','-','o','-','o']]
        
    
    def avalia_clique(self, pos):
        turno = self.turno % 2
        if self.status == "Jogando":
            linha, coluna = linha_clicada(pos), coluna_clicada(pos)
            if self.cedula_selecionada:
                movimento = self.is_movimento_valido(self.jogadores[turno], self.cedula_selecionada, linha, coluna)
                if movimento[0]:
                    self.jogar(self.jogadores[turno], self.cedula_selecionada, linha, coluna, movimento[1])
                elif linha == self.cedula_selecionada[0] and coluna == self.cedula_selecionada[1]:
                    movs = self.movimento_obrigatorio(self.cedula_selecionada)
                    if movs[0] == []:
                        if self.pulando:
                            self.pulando = False
                            self.proximo_turno()
                    self.cedula_selecionada = None
            else:
                if self.matriz_jogadores[linha][coluna].lower() == self.jogadores[turno]:
                    self.cedula_selecionada = [linha, coluna]
    
    # VERIFICANDO SE UM MOVIMENTO REALIZADO PELO JOGADOR É VÁLIDO
    def is_movimento_valido(self, jogador, localizacao_cedula, linha_destino, coluna_destino):

        linha_originaria = localizacao_cedula[0]
        coluna_originaria = localizacao_cedula[1]

        obrigatorios = self.todos_obrigatorios()

        if obrigatorios != {}:
            if (linha_originaria, coluna_originaria) not in obrigatorios:
                return False, None
            elif [linha_destino, coluna_destino] not in obrigatorios[(linha_originaria, coluna_originaria)]:
                return False, None

        movimento, pulo = self.movimentos_possiveis(localizacao_cedula)

        if [linha_destino, coluna_destino] in movimento:
            if pulo:
                if len(pulo) == 1:
                    return True, pulo[0]
                else:
                    for i in range(len(pulo)):
                        if abs(pulo[i][0] - linha_destino) == 1 and abs(pulo[i][1] - coluna_destino) == 1:
                            return True, pulo[i]

            if self.pulando:
                return False, None

            return True, None

        return False, None
    

    # RETORNA TODOS OS MOVIMENTOS OBRIGATÓRIOS DE UM TURNO
    def todos_obrigatorios(self):
            todos = {}

            for r in range(len(self.matriz_jogadores)):
                for c in range(len(self.matriz_jogadores[r])):
                    ob, pulos = self.movimento_obrigatorio((r, c))
                    if  ob != []:
                        todos[(r, c)] = ob

            return todos
            
        # RETORNA SE EXISTE UM MOVIMENTO POSSIVEL A SE FAZER COM A PEÇA
    def existe_possivel(self):
            for l in range(len(self.matriz_jogadores)):
                for c in range(len(self.matriz_jogadores[l])):
                    if self.movimentos_possiveis((l, c))[0]:
                        return True
            return False

def coluna_clicada(pos):
	x = pos[0]
	for i in range(1, 8):
		if x < i * ALTURA / 8:
			return i - 1
	return 7

def linha_clicada(pos):
	y = pos[1]
	for i in range(1, 8):
		if y < i * ALTURA / 8:
			return i - 1
	return 7