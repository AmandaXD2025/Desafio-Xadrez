# src/constants.py
import pygame

# --- Dimensões ---
LARGURA, ALTURA = 800, 800
LINHAS, COLUNAS = 8, 8
TAMANHO_QUADRADO = LARGURA // COLUNAS

# --- Cores (RGB) ---
BRANCO_CASA = (238, 238, 210)
VERDE_CASA = (118, 150, 86)

# <<< NOVAS CORES COM ALTO CONTRASTE >>>
COR_DESTAQUE = (255, 255, 0, 100)      
COR_MOVIMENTO = (30, 144, 255, 125)    

# --- Símbolos das Peças (Unicode) ---
SIMBOLOS = {
    'branco': {'rei': '♔', 'rainha': '♕', 'torre': '♖', 'bispo': '♗', 'cavalo': '♘', 'peao': '♙'},
    'preto': {'rei': '♚', 'rainha': '♛', 'torre': '♜', 'bispo': '♝', 'cavalo': '♞', 'peao': '♟'}
}