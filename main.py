# main.py
import pygame
from src.constants import LARGURA, ALTURA, TAMANHO_QUADRADO
from src.game import Game

WIN = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Xadrez")
pygame.font.init()

def get_row_col_from_mouse(pos):
    x, y = pos
    linha = y // TAMANHO_QUADRADO
    coluna = x // TAMANHO_QUADRADO
    return linha, coluna

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                linha, coluna = get_row_col_from_mouse(pos)
                game.select(linha, coluna)

        game.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()