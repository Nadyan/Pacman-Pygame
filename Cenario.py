import pygame
from pygame.draw import polygon
import config

PAREDE = 2
VAZIO = 0
MOEDA = 1

class Cenario:
    def __init__(self, pacman):
        self.pacman = pacman
        self.tamanho_celula = config.SCR_HEIGHT // config.TAM_CENARIO
        self.matriz = config.CENARIO
        self.tamanho_moeda = self.tamanho_celula // 10
        self.pontuacao = 0
        self.score = pygame.font.SysFont('arial', 16, True, False)

    def desenhar(self, tela):
        for id_linha, linha in enumerate(self.matriz):
            for id_coluna, coluna in enumerate(linha):
                x = id_coluna * self.tamanho_celula
                y = id_linha * self.tamanho_celula

                if coluna == PAREDE:
                    pygame.draw.rect(tela, config.AZUL, (x, y, self.tamanho_celula, self.tamanho_celula), 0)
                elif coluna == VAZIO:
                    pygame.draw.rect(tela, config.PRETO, (x, y, self.tamanho_celula, self.tamanho_celula), 0)
                elif coluna == MOEDA:
                    meio_celula = (x+self.tamanho_celula/2, y+self.tamanho_celula/2)
                    pygame.draw.circle(tela, config.AMARELO, meio_celula, self.tamanho_moeda, 0)

        self.desenhar_pontuacao(tela)

    def desenhar_pontuacao(self, tela):
        img_pontuacao = self.score.render("Score: {}".format(self.pontuacao), True, config.AMARELO)
        tela.blit(img_pontuacao, (5, 3))

    def calcular_posicionamento(self):
        # Testa se a movimentação é permitida
        coluna_intencao = self.pacman.coluna_intencao
        linha_intencao = self.pacman.linha_intencao

        proxima_celula = self.matriz[linha_intencao][coluna_intencao]
        if proxima_celula != PAREDE:
            self.pacman.efetuar_movimento()
            if proxima_celula == MOEDA:
                self.matriz[linha_intencao][coluna_intencao] = VAZIO
                self.pontuacao += 1
            
        
