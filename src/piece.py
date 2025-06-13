# src/piece.py

class Piece:
    """Classe base para todas as peças."""
    def __init__(self, linha, coluna, cor, simbolo):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
        self.simbolo = simbolo

    def mover(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        return self.simbolo

class Rei(Piece):
    def __init__(self, linha, coluna, cor):
        from src.constants import SIMBOLOS
        super().__init__(linha, coluna, cor, SIMBOLOS[cor]['rei'])

    def get_valid_moves(self, board):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nova_linha, nova_coluna = self.linha + i, self.coluna + j
                if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                    peca = board.get_piece(nova_linha, nova_coluna)
                    if peca is None or peca.cor != self.cor:
                        moves.append((nova_linha, nova_coluna))
        return moves

class Rainha(Piece):
    def __init__(self, linha, coluna, cor):
        from src.constants import SIMBOLOS
        super().__init__(linha, coluna, cor, SIMBOLOS[cor]['rainha'])

    def get_valid_moves(self, board):
        # Combina movimentos da Torre e do Bispo
        torre = Torre(self.linha, self.coluna, self.cor)
        bispo = Bispo(self.linha, self.coluna, self.cor)
        return torre.get_valid_moves(board) + bispo.get_valid_moves(board)

class Torre(Piece):
    def __init__(self, linha, coluna, cor):
        from src.constants import SIMBOLOS
        super().__init__(linha, coluna, cor, SIMBOLOS[cor]['torre'])

    def get_valid_moves(self, board):
        moves = []
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dl, dc in direcoes:
            for i in range(1, 8):
                nova_linha, nova_coluna = self.linha + i * dl, self.coluna + i * dc
                if not (0 <= nova_linha < 8 and 0 <= nova_coluna < 8):
                    break
                peca = board.get_piece(nova_linha, nova_coluna)
                if peca is None:
                    moves.append((nova_linha, nova_coluna))
                elif peca.cor != self.cor:
                    moves.append((nova_linha, nova_coluna))
                    break
                else:
                    break
        return moves

class Bispo(Piece):
    def __init__(self, linha, coluna, cor):
        from src.constants import SIMBOLOS
        super().__init__(linha, coluna, cor, SIMBOLOS[cor]['bispo'])

    def get_valid_moves(self, board):
        moves = []
        direcoes = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dl, dc in direcoes:
            for i in range(1, 8):
                nova_linha, nova_coluna = self.linha + i * dl, self.coluna + i * dc
                if not (0 <= nova_linha < 8 and 0 <= nova_coluna < 8):
                    break
                peca = board.get_piece(nova_linha, nova_coluna)
                if peca is None:
                    moves.append((nova_linha, nova_coluna))
                elif peca.cor != self.cor:
                    moves.append((nova_linha, nova_coluna))
                    break
                else:
                    break
        return moves

class Cavalo(Piece):
    def __init__(self, linha, coluna, cor):
        from src.constants import SIMBOLOS
        super().__init__(linha, coluna, cor, SIMBOLOS[cor]['cavalo'])

    def get_valid_moves(self, board):
        moves = []
        offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dl, dc in offsets:
            nova_linha, nova_coluna = self.linha + dl, self.coluna + dc
            if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                peca = board.get_piece(nova_linha, nova_coluna)
                if peca is None or peca.cor != self.cor:
                    moves.append((nova_linha, nova_coluna))
        return moves

class Peao(Piece):
    def __init__(self, linha, coluna, cor):
        from src.constants import SIMBOLOS
        super().__init__(linha, coluna, cor, SIMBOLOS[cor]['peao'])
        self.primeiro_movimento = True

    def get_valid_moves(self, board):
        moves = []
        direcao = -1 if self.cor == 'branco' else 1
        
        # Movimento para frente
        nova_linha = self.linha + direcao
        if 0 <= nova_linha < 8 and board.get_piece(nova_linha, self.coluna) is None:
            moves.append((nova_linha, self.coluna))
            # Movimento duplo inicial
            if self.primeiro_movimento and board.get_piece(self.linha + 2 * direcao, self.coluna) is None:
                moves.append((self.linha + 2 * direcao, self.coluna))

        # Captura na diagonal
        for dc in [-1, 1]:
            nova_linha, nova_coluna = self.linha + direcao, self.coluna + dc
            if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                peca = board.get_piece(nova_linha, nova_coluna)
                if peca is not None and peca.cor != self.cor:
                    moves.append((nova_linha, nova_coluna))
        return moves

    def mover(self, linha, coluna):
        super().mover(linha, coluna)
        self.primeiro_movimento = False