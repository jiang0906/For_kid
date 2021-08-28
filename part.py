import pygame
from settings import *
from name import *


class Part_1:
    def __init__(self):
        self.image = part_1
        self.pos = (10, 10)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                return True
            return False


class Part_2:
    def __init__(self):
        self.image = part_2
        self.pos = (90, 10)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                return True
            return False


class Part_3:
    def __init__(self):
        self.image = part_3
        self.pos = (170, 10)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                return True
            return False
