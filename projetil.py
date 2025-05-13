import pygame
import math

class Projetil:
    def __init__(self, x, y, alvo_x, alvo_y, velocidade=10):
        self.pos = pygame.Vector2(x, y)
        direcao = pygame.Vector2(alvo_x - x, alvo_y - y)
        if direcao.length() != 0:
            self.direcao = direcao.normalize()
        else:
            self.direcao = pygame.Vector2(0, 0)
        self.velocidade = velocidade
        self.raio = 3
        self.cor = (255, 255, 0)
        self.rect = pygame.Rect(x, y, self.raio * 2, self.raio * 2)

    def atualizar(self):
        self.pos += self.direcao * self.velocidade
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (int(self.pos.x), int(self.pos.y)), self.raio)

    def fora_da_tela(self, largura, altura):
        return (
            self.pos.x < 0 or self.pos.x > largura or
            self.pos.y < 0 or self.pos.y > altura
        )