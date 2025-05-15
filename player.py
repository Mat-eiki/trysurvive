import pygame
from armas import Pistola, AK47, Metralhadora
from projetil import Projetil

class Player:
    def __init__(self, x, y):
        # Carrega os sprites
        self.sprites = {
            "front": [pygame.image.load("player_front1.png")],
            "back": [pygame.image.load("player_back1.png")],
            "down": [pygame.image.load("player_down.png"), pygame.image.load("player_down2.png")],
            "up": [pygame.image.load("player_up.png"), pygame.image.load("player_up2.png")],
            "right": [pygame.image.load("player_right.png"), pygame.image.load("player_right2.png")]
        }

        self.direcao = "front"  # Estado inicial
        self.frame_index = 0
        self.frame_count = 0
        self.frame_delay = 10
        self.velocidade = 5
        self.vida = 100

        self.image = self.sprites["front"][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.arma = Metralhadora()
        self.projeteis = []

    def levar_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def mover(self, teclas, largura_tela, altura_tela, barreira):
        movendo = False
        nova_direcao = self.direcao

        movimento_x = 0
        movimento_y = 0

        if teclas[pygame.K_w] and self.rect.top > 0:
            movimento_y = -self.velocidade
            nova_direcao = "up"
            movendo = True
        elif teclas[pygame.K_s] and self.rect.bottom < altura_tela:
            movimento_y = self.velocidade
            nova_direcao = "down"
            movendo = True
        elif teclas[pygame.K_d] and self.rect.right < largura_tela:
            movimento_x = self.velocidade
            nova_direcao = "right"
            movendo = True
        elif teclas[pygame.K_a] and self.rect.left > 0:
            movimento_x = -self.velocidade
            nova_direcao = "left"
            movendo = True

        # Cria cópia do retângulo com movimento aplicado
        novo_rect = self.rect.move(movimento_x, movimento_y)

        # Checa colisão com a barreira
        if not novo_rect.colliderect(barreira):
            self.rect = novo_rect  # Só move se não colidir

        if movendo:
            self.direcao = nova_direcao
            self.frame_count += 1
            if self.frame_count >= self.frame_delay:
                self.frame_index = (self.frame_index + 1) % 2
                self.frame_count = 0
        else:
            self.frame_index = 0  # Parado

        # Atualiza a imagem
        if self.direcao == "left":
            sprite_direita = self.sprites["right"][self.frame_index]
            self.image = pygame.transform.flip(sprite_direita, True, False)
        elif self.direcao == "right":
            self.image = self.sprites["right"][self.frame_index]
        elif self.direcao == "up":
            self.image = self.sprites["up"][self.frame_index]
        elif self.direcao == "down":
            self.image = self.sprites["down"][self.frame_index]
        elif self.direcao == "front":
            self.image = self.sprites["front"][0]
        elif self.direcao == "back":
            self.image = self.sprites["back"][0]

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

    def atirar(self, pos_mouse):
        if self.arma.atirar(pos_mouse):
            centro_x = self.rect.centerx
            centro_y = self.rect.centery
            projetil = Projetil(centro_x, centro_y, pos_mouse[0], pos_mouse[1])
            self.projeteis.append(projetil)

    def desenhar_barra_vida(self, tela):
        # Tamanho e posição da barra
        barra_largura = 50
        barra_altura = 5
        x = self.rect.x - 5
        y = self.rect.y - 15

        # Cor e fundo
        pygame.draw.rect(tela, (255, 0, 0), (x, y, barra_largura, barra_altura))  # Vermelho: fundo da vida
        vida_atual = (self.vida / 100) * barra_largura
        pygame.draw.rect(tela, (0, 255, 0), (x, y, vida_atual, barra_altura))     # Verde: vida atual

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

