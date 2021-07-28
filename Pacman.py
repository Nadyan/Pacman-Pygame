import pygame
from pygame.draw import polygon
import config

class Pacman:
    def __init__(self):
        ## Atributos de posição
        self.coluna = 1
        self.linha = 1

        ## Atributos de formato
        self.centro_x = int(config.SCR_WIDTH / 2)
        self.centro_y = int(config.SCR_HEIGHT / 2)
        self.tamanho = config.TAMANHO_PACMAN
        self.raio = int(self.tamanho / 2)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.cor = config.AMARELO
        self.cor_boca = config.PRETO
        self.cor_olho = config.PRETO

    def calcular_posicionamento(self):

        self.coluna = self.coluna + self.velocidade_x
        self.linha = self.linha + self.velocidade_y
        self.centro_x = int((self.coluna * self.tamanho) + self.raio)
        self.centro_y = int((self.linha * self.tamanho) + self.raio)
        
        if self.centro_x + self.raio >= config.SCR_WIDTH:
            self.velocidade_x = 0
        if self.centro_x <= self.raio:
            self.velocidade_x = 0
        if self.centro_y + self.raio >= config.SCR_HEIGHT:
            self.velocidade_y = 0
        if self.centro_y <= self.raio:
            self.velocidade_y = 0

    def processar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d: ## D
                self.velocidade_x = config.VEL_XY
                self.velocidade_y = 0
            if evento.key == pygame.K_a: ## A
                self.velocidade_x = -config.VEL_XY
                self.velocidade_y = 0
            if evento.key == pygame.K_s: ## S
                self.velocidade_y = config.VEL_XY
                self.velocidade_x = 0
            if evento.key == pygame.K_w: ## W
                self.velocidade_y = -config.VEL_XY
                self.velocidade_x = 0
        """ Para o pacman parar ao soltar a tecla:
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_d:
                self.velocidade_x = 0
        """

    def desenhar(self, tela):
        # Desenha o corpo do pacman
        pygame.draw.circle(tela, self.cor, (self.centro_x, self.centro_y), self.raio, 0)

        # Desenha a boca do pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos_boca = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, self.cor_boca, pontos_boca, 0)

        # Desenha o olho do pacman
        olho_x = int(self.centro_x + self.raio / 6)
        olho_y = int(self.centro_y - self.raio * 0.55)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, self.cor_olho, (olho_x, olho_y), olho_raio, 0)
        