import pygame
import random
from inimigos import ZumbiNormal, ZumbiRapido, ZumbiTank, ZumbiBoss1, ZumbiBoss2

class GerenciadorOndas:
    def __init__(self, largura, altura):
        self.inimigos = []
        self.tempo_ultima_onda = pygame.time.get_ticks()
        self.tempo_ultimo_boss = pygame.time.get_ticks()
        self.tempo_inicial = pygame.time.get_ticks()
        self.nivel_atual = 0
        self.boss1_spawnado = False
        self.boss2_spawnado = False
        self.largura = largura
        self.altura = altura

        # Configurações das ondas
        self.config_ondas = [
            {"intervalo": 10000, "normais": 3, "rapidos": 2, "tanks": 1},  # Nível 0
            {"intervalo": 10000, "normais": 6, "rapidos": 4, "tanks": 2}, # Nível 1
            {"intervalo": 10000, "normais": 14, "rapidos": 10, "tanks": 5} # Nível 2
        ]

    def gerar_posicao_entrada(self):
        lado = random.choice(['cima', 'baixo', 'esquerda', 'direita'])

        if lado == 'cima':
            return random.randint(0, self.largura), -50
        elif lado == 'baixo':
            return random.randint(0, self.largura), self.altura + 50
        elif lado == 'esquerda':
            return -50, random.randint(0, self.altura)
        else:
            return self.largura + 50, random.randint(0, self.altura)

    def gerar_onda(self):
        config = self.config_ondas[min(self.nivel_atual, len(self.config_ondas)-1)]

        for _ in range(config["normais"]):
            x, y = self.gerar_posicao_entrada()
            self.inimigos.append(ZumbiNormal(x, y))

        for _ in range(config["rapidos"]):
            x, y = self.gerar_posicao_entrada()
            self.inimigos.append(ZumbiRapido(x, y))

        for _ in range(config["tanks"]):
            x, y = self.gerar_posicao_entrada()
            self.inimigos.append(ZumbiTank(x, y))

    def atualizar(self, jogador):
        tempo_atual = pygame.time.get_ticks()

        # Gera ondas a cada X segundos
        intervalo = self.config_ondas[min(self.nivel_atual, len(self.config_ondas)-1)]["intervalo"]
        if tempo_atual - self.tempo_ultima_onda > intervalo:
            self.gerar_onda()
            self.tempo_ultima_onda = tempo_atual

        # Boss 1 aos 60s
        if not self.boss1_spawnado and tempo_atual - self.tempo_inicial > 60000:
            x, y = self.gerar_posicao_entrada()
            self.inimigos.append(ZumbiBoss1(x, y))
            self.boss1_spawnado = True
            self.nivel_atual = 1

        # Boss 2 aos 120s (apenas se o Boss1 morreu)
        boss1_vivo = any(isinstance(i, ZumbiBoss1) for i in self.inimigos)
        if self.boss1_spawnado and not boss1_vivo and not self.boss2_spawnado and tempo_atual - self.tempo_inicial > 120000:
            x, y = self.gerar_posicao_entrada()
            self.inimigos.append(ZumbiBoss2(x, y))
            self.boss2_spawnado = True
            self.nivel_atual = 2

    def mover_inimigos(self, jogador):
        for inimigo in self.inimigos:
            inimigo.mover_em_direcao(jogador.rect.center)
            inimigo.tentar_atacar(jogador)

    def verificar_colisoes(self, projeteis, dano):
        for projetil in projeteis[:]:
            for inimigo in self.inimigos[:]:
                if projetil.rect.colliderect(inimigo.rect):
                    inimigo.vida -= dano
                    projeteis.remove(projetil)
                    if inimigo.vida <= 0:
                        self.inimigos.remove(inimigo)
                    break

    def desenhar_inimigos(self, tela):
        for inimigo in self.inimigos:
            inimigo.desenhar(tela)