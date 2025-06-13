# src/board.py
import pygame
from src.constants import BRANCO_CASA, VERDE_CASA, TAMANHO_QUADRADO, LINHAS, COLUNAS
from src.piece import Rei, Rainha, Torre, Bispo, Cavalo, Peao

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLUNAS)] for _ in range(LINHAS)]
        self._create_board()

    def _create_board(self):
        # Peças Pretas
        self.board[0][0] = Torre(0, 0, 'preto')
        self.board[0][1] = Cavalo(0, 1, 'preto')
        self.board[0][2] = Bispo(0, 2, 'preto')
        self.board[0][3] = Rainha(0, 3, 'preto')
        self.board[0][4] = Rei(0, 4, 'preto')
        self.board[0][5] = Bispo(0, 5, 'preto')
        self.board[0][6] = Cavalo(0, 6, 'preto')
        self.board[0][7] = Torre(0, 7, 'preto')
        for c in range(COLUNAS):
            self.board[1][c] = Peao(1, c, 'preto')

        # Peças Brancas
        self.board[7][0] = Torre(7, 0, 'branco')
        self.board[7][1] = Cavalo(7, 1, 'branco')
        self.board[7][2] = Bispo(7, 2, 'branco')
        self.board[7][3] = Rainha(7, 3, 'branco')
        self.board[7][4] = Rei(7, 4, 'branco')
        self.board[7][5] = Bispo(7, 5, 'branco')
        self.board[7][6] = Cavalo(7, 6, 'branco')
        self.board[7][7] = Torre(7, 7, 'branco')
        for c in range(COLUNAS):
            self.board[6][c] = Peao(6, c, 'branco')

    def draw(self, win):
        # Desenha o tabuleiro
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                cor = BRANCO_CASA if (linha + coluna) % 2 == 0 else VERDE_CASA
                pygame.draw.rect(win, cor, (coluna * TAMANHO_QUADRADO, linha * TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))

        # Desenha as peças
        fonte = pygame.font.SysFont('segoeuisymbol', int(TAMANHO_QUADRADO * 0.8))
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                peca = self.board[linha][coluna]
                if peca is not None:
                    texto = fonte.render(peca.simbolo, True, pygame.Color('black'))
                    rect = texto.get_rect(center=(coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO / 2, linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO / 2))
                    win.blit(texto, rect)

    def get_piece(self, linha, coluna):
        return self.board[linha][coluna]

    def move_piece(self, peca, nova_linha, nova_coluna):
        self.board[peca.linha][peca.coluna] = None
        self.board[nova_linha][nova_coluna] = peca
        peca.mover(nova_linha, nova_coluna)