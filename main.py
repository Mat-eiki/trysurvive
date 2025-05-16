import pygame
import sys
from player import Player
from gerenciador_ondas import GerenciadorOndas

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura = 1536
altura = 1024
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Trysurvive")

# Carrega a imagem de fundo
background = pygame.image.load("background.png")

# Define uma barreira (invisível)
barreira = pygame.Rect(585, 350, 235, 200)

# Cria o jogador
jogador = Player(650, 700)

# Cria o gerenciador de ondas
gerenciador = GerenciadorOndas(largura, altura)

# Define o relógio
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Entrada de teclado e mouse
    teclas = pygame.key.get_pressed()
    botoes_mouse = pygame.mouse.get_pressed()
    pos_mouse = pygame.mouse.get_pos()

    # Movimento do jogador
    jogador.mover(teclas, largura, altura, barreira)

    # Atualizações do jogo
    gerenciador.atualizar(jogador)
    gerenciador.mover_inimigos(jogador)
    gerenciador.verificar_colisoes(jogador.projeteis, jogador.arma.dano)

    # Atirar
    if botoes_mouse[0]:
        jogador.atirar(pos_mouse)

    # Atualiza projéteis
    for projetil in jogador.projeteis[:]:
        projetil.atualizar()
        if projetil.fora_da_tela(largura, altura):
            jogador.projeteis.remove(projetil)

    # Desenho da cena em ordem
    tela.blit(background, (0, 0))                      # Fundo
    for projetil in jogador.projeteis:                 # Projéteis
        projetil.desenhar(tela)
    gerenciador.desenhar_inimigos(tela)                # Inimigos
    jogador.desenhar(tela)                             # Jogador
    jogador.desenhar_barra_vida(tela)                  # Barra de vida

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)