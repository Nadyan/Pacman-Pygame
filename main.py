import pygame
import config
from Pacman import Pacman

if __name__ == "__main__":

    pygame.init()
    tela = pygame.display.set_mode((config.SCR_WIDTH, config.SCR_HEIGHT), 0)
    pacman = Pacman()

    while True:

        # Calcular as regras
        pacman.calcular_posicionamento()

        # Pintar a tela
        tela.fill(config.PRETO)
        pacman.desenhar(tela)
        pygame.display.update()

        # Captura eventos
        for e in  pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            else:
                pacman.processar_evento(e)
