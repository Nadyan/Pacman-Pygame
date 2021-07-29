import pygame
from pygame.draw import polygon
import config

PAREDE = 2
VAZIO = 0
MOEDA = 1

class Cenario:
    def __init__(self):
        self.tamanho = config.SCR_HEIGHT // config.TAM_CENARIO
        self.matriz = config.CENARIO

    def desenhar_cenario(self, tela):
        for id_linha, linha in enumerate(self.matriz):
            #self.desenhar_linha(id_linha, linha)
            for id_coluna, coluna in enumerate(linha):
                x = id_coluna * self.tamanho
                y = id_linha * self.tamanho

                if coluna == PAREDE:
                    pygame.draw.rect(tela, config.AZUL, (x, y, self.tamanho, self.tamanho), 0)
                elif coluna == VAZIO:
                    pygame.draw.rect(tela, config.PRETO, (x, y, self.tamanho, self.tamanho), 0)
                else:
                    pygame.draw.rect(tela, config.PRETO, (x, y, self.tamanho, self.tamanho), 0)




    def desenhar_linha(self, id_linha, linha):
        for id_coluna, coluna in enumerate(linha):
            x = id_coluna * self.tamanho
            y = id_linha * self.tamanho
