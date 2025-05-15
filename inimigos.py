import pygame

class Inimigo:
    def __init__(self, x, y, vida, dano, velocidade, imagem_path, escala):
        self.vida = vida
        self.dano = dano
        self.velocidade = velocidade
        imagem_original = pygame.image.load(imagem_path).convert_alpha()
        self.image = pygame.transform.rotozoom(imagem_original, 0, escala)
        self.pos = pygame.Vector2(x, y)
        self.rect = self.image.get_rect(center=self.pos)
        self.tempo_ultimo_ataque = 0
        self.tempo_entre_ataques = 1000


    def mover_em_direcao(self, alvo):
        direcao = pygame.Vector2(alvo[0] - self.pos.x, alvo[1] - self.pos.y)
        if direcao.length() != 0:
            direcao = direcao.normalize()
        self.pos += direcao * self.velocidade
        self.rect.center = (int(self.pos.x), int(self.pos.y))
        
    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

    def tentar_atacar(self, player):
        tempo_atual = pygame.time.get_ticks()
        if self.rect.colliderect(player.rect):
            if tempo_atual - self.tempo_ultimo_ataque >= self.tempo_entre_ataques:
                player.levar_dano(self.dano)
                self.tempo_ultimo_ataque = tempo_atual

# Tipos de zumbis com suas respectivas imagens
class ZumbiNormal(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=50, dano=10, velocidade=1.5, imagem_path="zumbi_normal.png", escala=3)

class ZumbiRapido(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=40, dano=5, velocidade=2.5, imagem_path="zumbi_rapido.png", escala=3)

class ZumbiTank(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=150, dano=20, velocidade=1, imagem_path="zumbi_tank.png", escala=3)

class ZumbiBoss1(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=350, dano=33, velocidade=1, imagem_path="zumbi_boss1.png", escala=1)

class ZumbiBoss2(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=800, dano=50, velocidade=1.5, imagem_path="zumbi_boss2.png", escala=1)

class ZumbiBoss3(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, vida=1200, dano=70, velocidade=2, imagem_path="zumbi_boss3.png", escala=1)