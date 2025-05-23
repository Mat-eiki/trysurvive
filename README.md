# Trysurvive

## Definição do Problema

Jogos de sobrevivência oferecem uma experiência desafiadora onde o jogador precisa enfrentar ondas crescentes de inimigos enquanto gerencia recursos limitados, saúde e habilidades. O problema principal abordado pelo Trysurvive é criar uma experiência fluida e dinâmica de sobrevivência, que combine:

- Inimigos variados com diferentes características (velocidade, dano, vida).
- Progressão em ondas de dificuldade crescente.
- Controle simples e intuitivo do personagem.
- Feedback visual e sonoro para manter o jogador engajado.
- Sistema de recordes para incentivar o aprimoramento e replay.

O objetivo do jogo é testar as habilidades de sobrevivência do jogador, colocando-o em uma arena onde ele deve resistir o máximo de tempo possível contra hordas de zumbis até atingir a vitória ou ser derrotado.

## Casos de Uso

- **Jogador inicia o jogo:** O jogador abre o jogo e é apresentado à tela principal com a arena de jogo carregada.
- **Jogador controla o personagem:** O jogador usa teclado e mouse para movimentar e atirar.
- **Inimigos aparecem em ondas:** O sistema gera ondas de zumbis que atacam o jogador, aumentando a dificuldade progressivamente.
- **Jogador sobrevive o maior tempo possível:** O jogador tenta sobreviver o máximo possível, controlando seus movimentos e ataques.
- **Sistema de vida e dano:** O jogador perde vida ao ser atacado e pode eliminar inimigos para sobreviver.
- **Sistema de pontuação e recorde:** O tempo sobrevivido é salvo como recorde local, incentivando o jogador a melhorar.
- **Pausa e reinício:** O jogador pode pausar o jogo a qualquer momento e, em caso de derrota, reiniciar para tentar novamente.
- **Tela de vitória:** Caso o jogador alcance o objetivo final, uma tela de vitória é exibida com o tempo total.

## Instalação

1. Certifique-se de ter o Python 3 instalado na sua máquina.  
   [Baixe aqui](https://www.python.org/downloads/)

2. Instale a biblioteca Pygame:  
   ```bash
   pip install pygame
   
3. Clone este repositório ou faça o download dos arquivos do jogo.

4. Execute o jogo:
   ```bash
   python main.py

## Como Jogar

- Use as teclas **W, A, S, D** para movimentar o personagem.
- Use o mouse para mirar.
- Clique com o botão esquerdo do mouse para atirar.
- Pressione **ESC** para pausar ou despausar o jogo.
- Sobreviva o máximo que puder contra as ondas de zumbis.
- Quando perder, uma tela com seu tempo de sobrevivência e recorde será exibida, permitindo reiniciar ou sair do jogo.

## Tecnologias Utilizadas

- **Python 3** — Linguagem de programação usada para desenvolver o jogo.
- **Pygame** — Biblioteca para desenvolvimento de jogos 2D.
- **JSON** — Para armazenamento local do recorde do jogador.
- **Pillow (opcional)** — Para edição e criação de assets gráficos (não obrigatório para rodar o jogo).
