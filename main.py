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

#tela de derrota
def mostrar_tela_derrota(tela):
    fonte_titulo = pygame.font.SysFont(None, 120)
    fonte_opcao = pygame.font.SysFont(None, 60)
    texto = fonte_titulo.render("VOCÊ PERDEU", True, (255, 0, 0))
    rect_texto = texto.get_rect(center=(largura // 2, altura // 3))

    # Botões
    reiniciar_txt = fonte_opcao.render("Reiniciar", True, (255, 255, 255))
    sair_txt = fonte_opcao.render("Sair", True, (255, 255, 255))

    reiniciar_rect = pygame.Rect(largura // 2 - 150, altura // 2, 300, 80)
    sair_rect = pygame.Rect(largura // 2 - 150, altura // 2 + 100, 300, 80)

    while True:
        tela.fill((0, 0, 0))
        tela.blit(texto, rect_texto)

        # Desenha botões
        pygame.draw.rect(tela, (100, 0, 0), reiniciar_rect)
        pygame.draw.rect(tela, (100, 0, 0), sair_rect)
        tela.blit(reiniciar_txt, reiniciar_txt.get_rect(center=reiniciar_rect.center))
        tela.blit(sair_txt, sair_txt.get_rect(center=sair_rect.center))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if reiniciar_rect.collidepoint(pygame.mouse.get_pos()):
                    return "reiniciar"
                elif sair_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

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

    #Vida zerada verificador
    if jogador.vida <= 0:
        acao = mostrar_tela_derrota(tela)
        if acao == "reiniciar":
            # Reinicia o jogo recriando objetos
            jogador = Player(650, 700)
            gerenciador = GerenciadorOndas(largura, altura)
            continue

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