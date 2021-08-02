import pygame
import config
from Pacman import Pacman
from Cenario import Cenario

if __name__ == "__main__":

    pygame.init()

    clock = pygame.time.Clock()

    tela = pygame.display.set_mode((config.SCR_WIDTH, config.SCR_HEIGHT), 0)

    pacman = Pacman()
    cenario = Cenario(pacman)

    while True:

        clock.tick(16)

        # Calcular as regras
        pacman.calcular_posicionamento()
        cenario.calcular_posicionamento()

        # Pintar a tela
        tela.fill(config.PRETO)
        cenario.desenhar(tela)
        pacman.desenhar(tela)
        pygame.display.update()

        # Captura eventos
        for e in  pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                pacman.processar_evento(e)
