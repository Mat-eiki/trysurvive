import pygame
import sys
import json
from player import Player
from gerenciador_ondas import GerenciadorOndas
from armas import Pistola, AK47, Metralhadora

#inicializa o Pygame
pygame.init()

#fonte para o cronometro
fonte = pygame.font.SysFont("arial", 36)

#define as dimensões da tela
info_tela = pygame.display.Info()
largura = 1440
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Trysurvive")

#carrega a imagem de fundo
background = pygame.image.load("background.png")

#define uma barreira (invisível)
barreira = pygame.Rect(585, 350, 235, 200)

#cria o jogador
jogador = Player(650, 700)

#cria o gerenciador de ondas
gerenciador = GerenciadorOndas(largura, altura)
gerenciador.gerar_onda()

#define o relógio
clock = pygame.time.Clock()

def inicializar_jogo():
    jogador = Player(650, 700)
    gerenciador = GerenciadorOndas(largura, altura)
    gerenciador.gerar_onda()  # Garante a primeira onda
    return jogador, gerenciador

jogador, gerenciador = inicializar_jogo()

def mostrar_tela_derrota(tela, recorde_str, tempo_atual_str):
    fonte_titulo = pygame.font.SysFont(None, 120)
    fonte_opcao = pygame.font.SysFont(None, 60)
    fonte_menor = pygame.font.SysFont(None, 40)

    texto = fonte_titulo.render("VOCÊ PERDEU", True, (255, 0, 0))
    recorde_txt = fonte_menor.render(f"Recorde: {recorde_str}", True, (255, 255, 255))
    atual_txt = fonte_menor.render(f"Sobreviveu: {tempo_atual_str}", True, (255, 255, 255))

    rect_texto = texto.get_rect(center=(largura // 2, altura // 3))
    rect_recorde = recorde_txt.get_rect(center=(largura // 2, altura // 3 + 70))
    rect_atual = atual_txt.get_rect(center=(largura // 2, altura // 3 + 110))

    reiniciar_txt = fonte_opcao.render("Reiniciar", True, (255, 255, 255))
    sair_txt = fonte_opcao.render("Sair", True, (255, 255, 255))

    reiniciar_rect = pygame.Rect(largura // 2 - 150, altura // 2, 300, 80)
    sair_rect = pygame.Rect(largura // 2 - 150, altura // 2 + 100, 300, 80)

    while True:
        tela.fill((0, 0, 0))
        tela.blit(texto, rect_texto)
        tela.blit(recorde_txt, rect_recorde)
        tela.blit(atual_txt, rect_atual)

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

def mostrar_tela_vitoria(tela, tempo_total_seg):
    fonte_titulo = pygame.font.SysFont(None, 100)
    fonte_texto = pygame.font.SysFont(None, 60)
    texto = fonte_titulo.render("VOCÊ VENCEU!", True, (0, 255, 0))
    rect_texto = texto.get_rect(center=(largura // 2, altura // 3))

    tempo_str = f"Tempo: {tempo_total_seg // 60:02}:{tempo_total_seg % 60:02}"
    tempo_txt = fonte_texto.render(tempo_str, True, (255, 255, 255))
    rect_tempo = tempo_txt.get_rect(center=(largura // 2, altura // 3 + 100))

    reiniciar_txt = fonte_texto.render("Reiniciar", True, (255, 255, 255))
    sair_txt = fonte_texto.render("Sair", True, (255, 255, 255))

    reiniciar_rect = pygame.Rect(largura // 2 - 150, altura // 2, 300, 80)
    sair_rect = pygame.Rect(largura // 2 - 150, altura // 2 + 100, 300, 80)

    while True:
        tela.fill((0, 0, 0))
        tela.blit(texto, rect_texto)
        tela.blit(tempo_txt, rect_tempo)

        pygame.draw.rect(tela, (0, 100, 0), reiniciar_rect)
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

    # Botões
    reiniciar_txt = fonte_opcao.render("Reiniciar", True, (255, 255, 255))
    sair_txt = fonte_opcao.render("Sair", True, (255, 255, 255))

    reiniciar_rect = pygame.Rect(largura // 2 - 150, altura // 2, 300, 80)
    sair_rect = pygame.Rect(largura // 2 - 150, altura // 2 + 100, 300, 80)

    while True:
        tela.fill((0, 0, 0))
        tela.blit(texto, rect_texto)
        tela.blit(recorde_txt, rect_recorde)
        tela.blit(atual_txt, rect_atual)

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

#loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #entrada de teclado e mouse
    teclas = pygame.key.get_pressed()
    botoes_mouse = pygame.mouse.get_pressed()
    pos_mouse = pygame.mouse.get_pos()

    #movimento do jogador
    jogador.mover(teclas, largura, altura, barreira)

    #atualizações do jogo
    resultado = gerenciador.atualizar(jogador)
    if resultado == "vitoria":
        tempo_final = pygame.time.get_ticks()
        tempo_total_seg = (tempo_final - gerenciador.tempo_inicial) // 1000
        acao = mostrar_tela_vitoria(tela, tempo_total_seg)
        if acao == "reiniciar":
            jogador, gerenciador = inicializar_jogo()
            continue
    gerenciador.mover_inimigos(jogador)
    gerenciador.verificar_colisoes(jogador.projeteis, jogador.arma.dano)

    #verificador de vida zerada
    if jogador.vida <= 0:
        # Calcula o tempo sobrevivido
        tempo_final = pygame.time.get_ticks()
        tempo_total_ms = tempo_final - gerenciador.tempo_inicial
        tempo_total_seg = tempo_total_ms // 1000
        minutos = tempo_total_seg // 60
        segundos = tempo_total_seg % 60

        # Verifica o recorde salvo
        recorde_anterior = 0
        try:
            with open("recorde.json", "r") as f:
                dados_salvos = json.load(f)
                recorde_anterior = dados_salvos.get("tempo_total_segundos", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            recorde_anterior = 0

        # Salva novo recorde se for maior
        if tempo_total_seg > recorde_anterior:
            dados = {
                "minutos": minutos,
                "segundos": segundos,
                "tempo_total_segundos": tempo_total_seg
            }
            with open("recorde.json", "w") as f:
                json.dump(dados, f, indent=4)
            recorde_str = f"{minutos:02}:{segundos:02}"
        else:
            recorde_min = recorde_anterior // 60
            recorde_seg = recorde_anterior % 60
            recorde_str = f"{recorde_min:02}:{recorde_seg:02}"

        # Chama tela de derrota com o recorde
        tempo_atual_str = f"{minutos:02}:{segundos:02}"
        acao = mostrar_tela_derrota(tela, recorde_str, tempo_atual_str)
        if acao == "reiniciar":
            jogador, gerenciador = inicializar_jogo()
            continue
        else:
            pygame.quit()
            sys.exit()


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

    # Calcula o tempo sobrevivido
    tempo_atual = pygame.time.get_ticks()
    segundos = (tempo_atual - gerenciador.tempo_inicial) // 1000
    minutos = segundos // 60
    segundos = segundos % 60
    texto_tempo = f"{minutos:02}:{segundos:02}"
    imagem_tempo = fonte.render(texto_tempo, True, (255, 255, 255))

    # Posição no canto superior direito (com margem)
    pos_x = largura - imagem_tempo.get_width() - 20
    pos_y = 20  # margem superior fixa
    tela.blit(imagem_tempo, (pos_x, pos_y))

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)