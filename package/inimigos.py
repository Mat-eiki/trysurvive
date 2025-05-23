import os
import pygame

class Inimigo:
    def __init__(self, x, y, vida, dano, velocidade, imagem_path, escala):
        self._vida = vida
        self._dano = dano
        self._velocidade = velocidade

        diretorio_atual = os.path.dirname(__file__)
        caminho_completo = os.path.join(diretorio_atual, '..', 'assets', imagem_path)
        caminho_completo = os.path.abspath(caminho_completo)

        imagem_original = pygame.image.load(caminho_completo).convert_alpha()
        self._image = pygame.transform.rotozoom(imagem_original, 0, escala)
        self._pos = pygame.Vector2(x, y)
        self._rect = self._image.get_rect(center=self._pos)
        self._tempo_ultimo_ataque = 0
        self._tempo_entre_ataques = 1000

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = max(0, valor)

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image

    @property
    def pos(self):
        return self._pos

    @property
    def dano(self):
        return self._dano

    @property
    def vivo(self):
        return self._vida > 0

    # MÉTODOS DE AÇÃO
    def levar_dano(self, dano):
        self._vida = max(0, self._vida - dano)

    def mover_em_direcao(self, alvo):
        direcao = pygame.Vector2(alvo[0] - self._pos.x, alvo[1] - self._pos.y)
        if direcao.length() != 0:
            direcao = direcao.normalize()
        self._pos += direcao * self._velocidade
        self._rect.center = (int(self._pos.x), int(self._pos.y))
        
    def desenhar(self, tela):
        tela.blit(self._image, self._rect)

    def tentar_atacar(self, player):
        tempo_atual = pygame.time.get_ticks()
        if self._rect.colliderect(player.rect):
            if tempo_atual - self._tempo_ultimo_ataque >= self._tempo_entre_ataques:
                player.levar_dano(self._dano)
                self._tempo_ultimo_ataque = tempo_atual

# SUBCLASSES DE ZUMBIS
class ZumbiNormal(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=50, dano=10, velocidade=1.5, imagem_path="zumbi_normal.png", escala=3)

class ZumbiRapido(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=40, dano=5, velocidade=2.5, imagem_path="zumbi_rapido.png", escala=3)

class ZumbiTank(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=160, dano=20, velocidade=1, imagem_path="zumbi_tank.png", escala=3)

class ZumbiBoss1(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=350, dano=33, velocidade=1, imagem_path="zumbi_boss1.png", escala=1)

class ZumbiBoss2(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=800, dano=50, velocidade=1.5, imagem_path="zumbi_boss2.png", escala=1)

class ZumbiBoss3(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=6000, dano=70, velocidade=2, imagem_path="zumbi_boss3.png", escala=1)