import pygame
import sys
from player import Player

# Importa o player passando a poss
jogador = Player(650, 700)

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura = 1536
altura = 1024
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Trysurvive")

# Carrega a imagem de fundo
background = pygame.image.load("background.png")

# Define uma barreira
barreira = pygame.Rect(585, 350, 235, 200)  # x, y, largura, altura

# Define o relógio para controlar o FPS (frames por segundo)
clock = pygame.time.Clock()


# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    botoes_mouse = pygame.mouse.get_pressed()
    pos_mouse = pygame.mouse.get_pos()

    # Atualiza movimento do jogador
    jogador.mover(teclas, largura, altura, barreira)

    # Atirar
    if botoes_mouse[0]:
        jogador.atirar(pos_mouse)

    # Atualiza projéteis
    for projetil in jogador.projeteis[:]:
        projetil.atualizar()
        if projetil.fora_da_tela(largura, altura):
            jogador.projeteis.remove(projetil)

    # Desenho na tela (uma vez por frame)
    tela.blit(background, (0, 0))

    # Desenha jogador e vida
    jogador.desenhar(tela)
    jogador.desenhar_barra_vida(tela)

    # Desenha projéteis
    for projetil in jogador.projeteis:
        projetil.desenhar(tela)

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)
