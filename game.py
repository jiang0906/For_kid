import pygame
from name import *
from part import *
from part_group import *
from settings import *


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.part = PartGroup()

    def draw(self):
        """
        Draw everything in this method
        :return: None
        """
        # draw background
        self.win.blit(background, (0, 0))
        # draw names
        self.part.draw(self.win)
        # update screen
        pygame.display.update()

    def update(self):
        game_quit = False
        # event loop
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                game_quit = True
                return game_quit
            # click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.part.got_click(x, y)

        return game_quit
