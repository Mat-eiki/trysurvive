import pygame

class Inimigo:
    def __init__(self, x, y, vida, dano, velocidade, imagem_path):
        self.vida = vida
        self.dano = dano
        self.velocidade = velocidade
        self.image = pygame.image.load(imagem_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def mover_em_direcao(self, alvo):
        dx = alvo[0] - self.rect.centerx
        dy = alvo[1] - self.rect.centery
        distancia = max((dx ** 2 + dy ** 2) ** 0.5, 1)
        self.rect.x += self.velocidade * dx / distancia
        self.rect.y += self.velocidade * dy / distancia

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

# Tipos de zumbis com suas respectivas imagens
class ZumbiNormal(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=50, dano=10, velocidade=1, imagem_path="zumbi_normal.png")

class ZumbiRapido(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=40, dano=5, velocidade=2.5, imagem_path="zumbi_rapido.png")

class ZumbiTank(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=150, dano=20, velocidade=0.5, imagem_path="zumbi_tank.png")

class ZumbiBoss1(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=350, dano=33, velocidade=1, imagem_path="zumbi_boss1.png")

class ZumbiBoss2(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=800, dano=50, velocidade=1.5, imagem_path="zumbi_boss2.png")

class ZumbiBoss3(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=1200, dano=70, velocidade=2, imagem_path="zumbi_boss3.png")