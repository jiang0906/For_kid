import pygame
from part import *


class PartGroup:
    def __init__(self):
        self.name = None
        self.parts = []
        self.part_1 = Part_1()
        self.part_2 = Part_2()
        self.part_3 = Part_3()
        self.selected_part = None

    def draw(self, win):
        if self.selected_part == "1":
            self.name = Name_1()
            self.name.draw(win)
        elif self.selected_part == "2":
            self.name = Name_2()
            self.name.draw(win)
        elif self.selected_part == "3":
            self.name = Name_3()
            self.name.draw(win)
        else:
            self.name = None

    def got_click(self, x, y):
        if self.part_1.clicked(x, y):
            self.selected_part = "1"
            return
        elif self.part_2.clicked(x, y):
            self.selected_part = "2"
            return
        elif self.part_3.clicked(x, y):
            self.selected_part = "3"
            return
        else:
            self.selected_part = None
            return
