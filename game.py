import pygame
from name import *
from part import *
from part_group import *
from settings import *


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.part = PartGroup()
        self.part_1 = Part_1()
        self.part_2 = Part_2()
        self.part_3 = Part_3()

    def draw(self):
        """
        Draw everything in this method
        :return: None
        """
        # draw background
        self.win.blit(background, (0, 0))
        # draw parts
        self.part_1.draw(self.win)
        self.part_2.draw(self.win)
        self.part_3.draw(self.win)
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
