import pygame
import time
from projetil import Projetil

class Arma:
    def __init__(self, nome, cadencia, dano):
        self.nome = nome
        self.cadencia = cadencia
        self.dano = dano
        self.ultimo_tiro = 0

    def atirar(self, pos_mouse):
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_tiro >= self.cadencia:
            self.ultimo_tiro = tempo_atual
            return True
        return False
    
    def pode_atirar(self):
        tempo_atual = time.time()
        return tempo_atual - self.ultimo_tiro >= self.cadencia
    
# Instâncias das armas
class Pistola(Arma):
    def __init__(self):
        super().__init__(nome="Pistola", cadencia=500, dano=10)

class AK47(Arma):
    def __init__(self):
        super().__init__(nome="AK47", cadencia=300, dano=20)

class Metralhadora(Arma):
    def __init__(self):
        super().__init__(nome="Metralhadora", cadencia=100, dano=30)