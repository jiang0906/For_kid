import pygame
from name import *
from part import *
from part_group import *
from settings import *


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.part = PartGroup()
        '''self.pictures = [Part_A1(), Part_A2(), Part_A3(), Part_A4(), Part_A5(), Part_A6(),
                         Part_B1(), Part_B2(), Part_B3(), Part_B4(), Part_B5(), Part_B6(),
                         Part_C1(), Part_C2(), Part_C3(), Part_C4(), Part_C5(), Part_C6(),
                         Part_D1(), Part_D2(), Part_D3(), Part_D4(), Part_D5(), Part_D6(),
                         Part_E1(), Part_E2(), Part_E3(), Part_E4(), Part_E5(), Part_E6(),
                         Part_F1(), Part_F2(), Part_F3(), Part_F4(), Part_F5(), Part_F6(),
                         Part_G1(), Part_G2(), Part_G3()]'''

    def draw(self):
        """
        Draw everything in this method
        :return: None
        """
        # draw background
        self.win.blit(background, (0, 0))
        '''# draw parts
        for pt in self.pictures:
            self.win.blit(pt.image, pt.pos)'''
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
