# src/game.py
import pygame
from src.board import Board
from src.constants import TAMANHO_QUADRADO, COR_DESTAQUE, COR_MOVIMENTO

class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.turn = 'branco'
        self.selected_piece = None
        self.valid_moves = []

    def update(self):
        self.board.draw(self.win)
        self._draw_highlights()
        pygame.display.update()

    def _draw_highlights(self):
        # Destaque para a peça selecionada
        if self.selected_piece:
            l, c = self.selected_piece.linha, self.selected_piece.coluna
            s = pygame.Surface((TAMANHO_QUADRADO, TAMANHO_QUADRADO), pygame.SRCALPHA)
            s.fill(COR_DESTAQUE)
            self.win.blit(s, (c * TAMANHO_QUADRADO, l * TAMANHO_QUADRADO))

        # Destaque para movimentos válidos
        for move in self.valid_moves:
            l, c = move
            s = pygame.Surface((TAMANHO_QUADRADO, TAMANHO_QUADRADO), pygame.SRCALPHA)
            s.fill(COR_MOVIMENTO)
            self.win.blit(s, (c * TAMANHO_QUADRADO, l * TAMANHO_QUADRADO))

    def select(self, linha, coluna):
        # Se já tiver uma peça selecionada, tenta mover
        if self.selected_piece:
            move = (linha, coluna)
            if move in self.valid_moves:
                self.board.move_piece(self.selected_piece, linha, coluna)
                self._change_turn()
            # Desseleciona independentemente de ter movido ou não
            self.selected_piece = None
            self.valid_moves = []
            return

        # Se não, tenta selecionar uma nova peça
        peca = self.board.get_piece(linha, coluna)
        if peca is not None and peca.cor == self.turn:
            self.selected_piece = peca
            self.valid_moves = peca.get_valid_moves(self.board)

    def _change_turn(self):
        self.turn = 'preto' if self.turn == 'branco' else 'branco'