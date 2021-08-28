import pygame
import time
from game import *
from settings import *

if __name__ == '__main__':
    # initialization
    pygame.init()
    # set the window
    pygame.display.set_caption("來抽直屬阿")

    game = Game()
    quit_game = False
    while not quit_game:
        quit_game = game.update()
        game.draw()

    pygame.quit()
