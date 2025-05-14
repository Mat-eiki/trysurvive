import pygame
import sys
from player import Player
from inimigos import ZumbiNormal, ZumbiRapido, ZumbiTank, ZumbiBoss1, ZumbiBoss2, ZumbiBoss3

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
barreira = pygame.Rect(585, 350, 235, 200)

# Cria o jogador
jogador = Player(650, 700)

# Cria inimigos
inimigos = [
    ZumbiNormal(200, 100),
    ZumbiRapido(400, 50),
    ZumbiTank(800, 200),
    ZumbiBoss1(1000, 100),
    ZumbiBoss2(1300, 400),
    ZumbiBoss3(300, 800)
]

# Define o relógio
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Entrada do teclado e mouse
    teclas = pygame.key.get_pressed()
    botoes_mouse = pygame.mouse.get_pressed()
    pos_mouse = pygame.mouse.get_pos()

    # Atualiza o movimento do jogador
    jogador.mover(teclas, largura, altura, barreira)

    # Atualiza inimigos
    for inimigo in inimigos:
        inimigo.mover_em_direcao(jogador.rect.center)

    # Atirar
    if botoes_mouse[0]:
        jogador.atirar(pos_mouse)

    # Atualiza projéteis
    for projetil in jogador.projeteis[:]:
        projetil.atualizar()
        if projetil.fora_da_tela(largura, altura):
            jogador.projeteis.remove(projetil)
        else:
            for inimigo in inimigos[:]:
                if projetil.rect.colliderect(inimigo.rect):
                    inimigo.vida -= jogador.arma.dano
                    jogador.projeteis.remove(projetil)
                    if inimigo.vida <= 0:
                        inimigos.remove(inimigo)
                    break

    # Desenho da cena
    tela.blit(background, (0, 0))

    # Desenha jogador
    jogador.desenhar(tela)
    jogador.desenhar_barra_vida(tela)

    # Desenha inimigos
    for inimigo in inimigos:
        inimigo.desenhar(tela)

    # Desenha projéteis
    for projetil in jogador.projeteis:
        projetil.desenhar(tela)

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)