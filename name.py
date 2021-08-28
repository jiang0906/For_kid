import pygame
from settings import *


class Name_1:
    def __init__(self):
        self.image = name_1
        self.pos = (256, 100)

    def draw(self, win):
        win.blit(self.image, self.pos)


class Name_2:
    def __init__(self):
        self.image = name_2
        self.pos = (256, 100)

    def draw(self, win):
        win.blit(self.image, self.pos)


class Name_3:
    def __init__(self):
        self.image = name_3
        self.pos = (256, 100)

    def draw(self, win):
        win.blit(self.image, self.pos)
