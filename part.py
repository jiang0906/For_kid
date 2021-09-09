import pygame
from settings import *
from name import *


class Part_A1:
    def __init__(self):
        self.image = part_A1
        self.pos = (270, 160)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_A2:
    def __init__(self):
        self.image = part_A2
        self.pos = (270, 290)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_A3:
    def __init__(self):
        self.image = part_A3
        self.pos = (270, 430)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_A4:
    def __init__(self):
        self.image = part_A4
        self.pos = (270, 570)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_A5:
    def __init__(self):
        self.image = part_A5
        self.pos = (270, 690)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_A6:
    def __init__(self):
        self.image = part_A6
        self.pos = (270, 820)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_B1:
    def __init__(self):
        self.image = part_B1
        self.pos = (410, 170)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_B2:
    def __init__(self):
        self.image = part_B2
        self.pos = (410, 300)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_B3:
    def __init__(self):
        self.image = part_B3
        self.pos = (410, 430)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_B4:
    def __init__(self):
        self.image = part_B4
        self.pos = (410, 560)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_B5:
    def __init__(self):
        self.image = part_B5
        self.pos = (410, 660)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_B6:
    def __init__(self):
        self.image = part_B6
        self.pos = (410, 810)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_C1:
    def __init__(self):
        self.image = part_C1
        self.pos = (540, 170)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_C2:
    def __init__(self):
        self.image = part_C2
        self.pos = (540, 300)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_C3:
    def __init__(self):
        self.image = part_C3
        self.pos = (540, 430)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_C4:
    def __init__(self):
        self.image = part_C4
        self.pos = (540, 540)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_C5:
    def __init__(self):
        self.image = part_C5
        self.pos = (540, 680)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_C6:
    def __init__(self):
        self.image = part_C6
        self.pos = (540, 810)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_D1:
    def __init__(self):
        self.image = part_D1
        self.pos = (670, 170)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_D2:
    def __init__(self):
        self.image = part_D2
        self.pos = (670, 300)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_D3:
    def __init__(self):
        self.image = part_D3
        self.pos = (670, 420)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_D4:
    def __init__(self):
        self.image = part_D4
        self.pos = (670, 570)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_D5:
    def __init__(self):
        self.image = part_D5
        self.pos = (670, 680)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_D6:
    def __init__(self):
        self.image = part_D6
        self.pos = (670, 800)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_E1:
    def __init__(self):
        self.image = part_E1
        self.pos = (790, 140)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_E2:
    def __init__(self):
        self.image = part_E2
        self.pos = (790, 300)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_E3:
    def __init__(self):
        self.image = part_E3
        self.pos = (790, 420)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_E4:
    def __init__(self):
        self.image = part_E4
        self.pos = (790, 570)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_E5:
    def __init__(self):
        self.image = part_E5
        self.pos = (790, 690)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_E6:
    def __init__(self):
        self.image = part_E6
        self.pos = (790, 800)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_F1:
    def __init__(self):
        self.image = part_F1
        self.pos = (920, 160)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_F2:
    def __init__(self):
        self.image = part_F2
        self.pos = (920, 290)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_F3:
    def __init__(self):
        self.image = part_F3
        self.pos = (920, 400)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_F4:
    def __init__(self):
        self.image = part_F4
        self.pos = (920, 570)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_F5:
    def __init__(self):
        self.image = part_F5
        self.pos = (920, 690)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_F6:
    def __init__(self):
        self.image = part_F6
        self.pos = (920, 810)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_G1:
    def __init__(self):
        self.image = part_G1
        self.pos = (1050, 160)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_G2:
    def __init__(self):
        self.image = part_G2
        self.pos = (1050, 290)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_G3:
    def __init__(self):
        self.image = part_G3
        self.pos = (1050, 420)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_G4:
    def __init__(self):
        self.image = part_G4
        self.pos = (1050, 560)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_G5:
    def __init__(self):
        self.image = part_G5
        self.pos = (1050, 680)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_G6:
    def __init__(self):
        self.image = part_G6
        self.pos = (1050, 800)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_H1:
    def __init__(self):
        self.image = part_H1
        self.pos = (1180, 170)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_H2:
    def __init__(self):
        self.image = part_H2
        self.pos = (1180, 300)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_H3:
    def __init__(self):
        self.image = part_H3
        self.pos = (1180, 420)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_H4:
    def __init__(self):
        self.image = part_H4
        self.pos = (1180, 550)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_H5:
    def __init__(self):
        self.image = part_H5
        self.pos = (1180, 680)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_H6:
    def __init__(self):
        self.image = part_H6
        self.pos = (1180, 810)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_I1:
    def __init__(self):
        self.image = part_I1
        self.pos = (1300, 170)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_I2:
    def __init__(self):
        self.image = part_I2
        self.pos = (1300, 300)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_I3:
    def __init__(self):
        self.image = part_I3
        self.pos = (1300, 420)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_I4:
    def __init__(self):
        self.image = part_I4
        self.pos = (1300, 550)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_I5:
    def __init__(self):
        self.image = part_I5
        self.pos = (1300, 680)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False


class Part_I6:
    def __init__(self):
        self.image = part_I6
        self.pos = (1300, 810)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, win):
        win.blit(self.image, self.pos)

    def clicked(self, x, y) -> bool:
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False
