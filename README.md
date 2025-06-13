# Xadrez em Python com Pygame

Este projeto é uma implementação do clássico jogo de Xadrez, desenvolvido em Python com o auxílio da biblioteca Pygame para a interface gráfica. O foco foi criar uma arquitetura de software robusta e orientada a objetos, que separa claramente a lógica do jogo da sua apresentação visual, permitindo futuras expansões.

## ⚠️ Status do Projeto: Base Funcional

Este projeto constitui uma **base funcional sólida** para um jogo de xadrez. A mecânica principal de movimentação e captura está implementada, mas as regras mais complexas que definem um jogo de xadrez completo ainda são um campo para desenvolvimento futuro.

### Recursos Implementados
- ✔️ **Interface Gráfica:** Tabuleiro e peças desenhados com Pygame.
- ✔️ **Movimentação de Peças:** Lógica de movimento individual para as 6 tipos de peças (Peão, Torre, Cavalo, Bispo, Rainha e Rei).
- ✔️ **Destaque de Movimentos:** Ao clicar em uma peça, seus movimentos válidos são destacados visualmente no tabuleiro.
- ✔️ **Sistema de Turnos:** O jogo alterna corretamente os turnos entre as peças brancas e pretas.
- ✔️ **Captura de Peças:** A mecânica de uma peça capturar a outra ao se mover para sua casa está funcional.
- ✔️ **Arquitetura Orientada a Objetos:** O código é altamente modular, com classes para Peças, Tabuleiro e Jogo.

### Próximos Passos (Roadmap de Desenvolvimento)
- ❌ **Detecção de Xeque e Xeque-mate:** A lógica para identificar quando um rei está em perigo e quando o jogo termina ainda não foi implementada.
- ❌ **Regras Especiais:** Falta implementar o Roque (Castling), a Promoção de Peão e a captura *En Passant*.
- ❌ **Prevenção de Movimentos Ilegais:** Atualmente, é possível fazer um movimento que deixe o próprio rei em xeque.
- ❌ **Condições de Empate:** Regras como afogamento (Stalemate), repetição tripla e a regra dos 50 movimentos não estão presentes.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pygame:** Para toda a renderização gráfica e gerenciamento de eventos (cliques de mouse).

## ⚙️ Estrutura do Projeto

```
xadrez-pygame/
├── main.py        # Ponto de entrada que inicia o loop do Pygame
├── requirements.txt
└── src/
    ├── constants.py   # Cores, dimensões e constantes
    ├── piece.py       # Classes para todas as peças
    ├── board.py       # Classe que gerencia o estado do tabuleiro
    └── game.py        # Classe que orquestra a lógica do jogo
```

## 🚀 Como Executar o Projeto

**Pré-requisitos:** Python 3 e Git instalados.

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Execute o jogo:**
    O comando deve ser executado a partir da pasta raiz do projeto.
    ```bash
    python main.py
    ```

## 🕹️ Como Jogar

- **Selecionar Peça:** Clique com o botão esquerdo do mouse em uma peça da sua cor. Os quadrados para onde ela pode se mover serão destacados.
- **Mover Peça:** Clique em um dos quadrados destacados para mover a peça selecionada para aquele local.
- **Turno:** O turno passará automaticamente para o outro jogador após um movimento válido.