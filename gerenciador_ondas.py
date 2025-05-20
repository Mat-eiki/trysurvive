import pygame
import random
from inimigos import ZumbiNormal, ZumbiRapido, ZumbiTank, ZumbiBoss1, ZumbiBoss2, ZumbiBoss3
from armas import Pistola, AK47, Metralhadora

class GerenciadorOndas:
    def __init__(self, largura, altura):
        self.inimigos = []
        self.tempo_ultima_onda = pygame.time.get_ticks()
        self.tempo_ultimo_boss = pygame.time.get_ticks()
        self.tempo_inicial = pygame.time.get_ticks()
        self.nivel_atual = 0
        self.boss1_spawnado = False
        self.boss2_spawnado = False
        self.boss3_spawnado = False
        self.largura = largura
        self.altura = altura

        # Configurações das ondas
        self.config_ondas = [
            {"intervalo": 20000, "normais": 3, "rapidos": 2, "tanks": 1},  # Nível 0
            {"intervalo": 20000, "normais": 6, "rapidos": 4, "tanks": 2}, # Nível 1
            {"intervalo": 15000, "normais": 14, "rapidos": 10, "tanks": 5} # Nível 2
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

        # Atualiza intervalo da onda atual
        intervalo = self.config_ondas[min(self.nivel_atual, len(self.config_ondas)-1)]["intervalo"]
        if tempo_atual - self.tempo_ultima_onda > intervalo:
            self.gerar_onda()
            self.tempo_ultima_onda = tempo_atual

        # Boss 1 aos 60s (mas só uma vez)
        if not self.boss1_spawnado and tempo_atual - self.tempo_inicial > 60000:
            x, y = self.gerar_posicao_entrada()
            self.inimigos.append(ZumbiBoss1(x, y))
            self.boss1_spawnado = True

        # Subir para nível 1 após derrotar Boss 1
        if self.boss1_spawnado and not any(isinstance(i, ZumbiBoss1) for i in self.inimigos):
            if self.nivel_atual < 1:
                self.nivel_atual = 1
                jogador.arma = AK47()

# Boss 2 aos 120s (somente se Boss 1 já foi derrotado)
        if self.nivel_atual >= 1 and not self.boss2_spawnado and tempo_atual - self.tempo_inicial > 120000:
            x, y = self.gerar_posicao_entrada()
            self.inimigos.append(ZumbiBoss2(x, y))
            self.boss2_spawnado = True

# Subir para nível 2 após derrotar Boss 2
        if self.boss2_spawnado and not any(isinstance(i, ZumbiBoss2) for i in self.inimigos):
            if self.nivel_atual < 2:
                self.nivel_atual = 2
                jogador.arma = Metralhadora()
        
        # Boss3 aos 180 segundos (3 minutos)
        if self.nivel_atual >= 2 and not self.boss3_spawnado and tempo_atual - self.tempo_inicial > 180000:
            x, y = self.gerar_posicao_entrada()
            self.inimigos.append(ZumbiBoss3(x, y))
            self.boss3_spawnado = True

        # Detectar vitória (quando boss3 for spawnado e derrotado)
        if self.boss3_spawnado and not any(isinstance(i, ZumbiBoss3) for i in self.inimigos):
            return "vitoria"

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