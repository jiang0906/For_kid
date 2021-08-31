import pygame
from part import *
from name import *
from settings import *


class PartGroup:
    def __init__(self):
        self.name = None
        self.part_A1 = Part_A1()
        self.part_A2 = Part_A2()
        self.part_A3 = Part_A3()
        self.part_A4 = Part_A4()
        self.part_A5 = Part_A5()
        self.part_A6 = Part_A6()
        self.part_B1 = Part_B1()
        self.part_B2 = Part_B2()
        self.part_B3 = Part_B3()
        self.part_B4 = Part_B4()
        self.part_B5 = Part_B5()
        self.part_B6 = Part_B6()
        self.part_C1 = Part_C1()
        self.part_C2 = Part_C2()
        self.part_C3 = Part_C3()
        self.part_C4 = Part_C4()
        self.part_C5 = Part_C5()
        self.part_C6 = Part_C6()
        self.part_D1 = Part_D1()
        self.part_D2 = Part_D2()
        self.part_D3 = Part_D3()
        self.part_D4 = Part_D4()
        self.part_D5 = Part_D5()
        self.part_D6 = Part_D6()
        self.part_E1 = Part_E1()
        self.part_E2 = Part_E2()
        self.part_E3 = Part_E3()
        self.part_E4 = Part_E4()
        self.part_E5 = Part_E5()
        self.part_E6 = Part_E6()
        self.part_F1 = Part_F1()
        self.part_F2 = Part_F2()
        self.part_F3 = Part_F3()
        self.part_F4 = Part_F4()
        self.part_F5 = Part_F5()
        self.part_F6 = Part_F6()
        self.part_G1 = Part_G1()
        self.part_G2 = Part_G2()
        self.part_G3 = Part_G3()
        self.pictures = [self.part_A1, self.part_A2, self.part_A3, self.part_A4, self.part_A5, self.part_A6,
                         self.part_B1, self.part_B2, self.part_B3, self.part_B4, self.part_B5, self.part_B6,
                         self.part_C1, self.part_C2, self.part_C3, self.part_C4, self.part_C5, self.part_C6,
                         self.part_D1, self.part_D2, self.part_D3, self.part_D4, self.part_D5, self.part_D6,
                         self.part_E1, self.part_E2, self.part_E3, self.part_E4, self.part_E5, self.part_E6,
                         self.part_F1, self.part_F2, self.part_F3, self.part_F4, self.part_F5, self.part_F6,
                         self.part_G1, self.part_G2, self.part_G3]
        self.selected_part = None

    def draw(self, win):
        for pt in self.pictures:
            win.blit(pt.image, pt.pos)
            if self.selected_part == "A1":
                self.name = Name_A1()
                self.name.draw(win)
            elif self.selected_part == "A2":
                self.name = Name_A2()
                self.name.draw(win)
            elif self.selected_part == "A3":
                self.name = Name_A3()
                self.name.draw(win)
            elif self.selected_part == "A4":
                self.name = Name_A4()
                self.name.draw(win)
            elif self.selected_part == "A5":
                self.name = Name_A5()
                self.name.draw(win)
            elif self.selected_part == "A6":
                self.name = Name_A6()
                self.name.draw(win)
            elif self.selected_part == "B1":
                self.name = Name_B1()
                self.name.draw(win)
            elif self.selected_part == "B2":
                self.name = Name_B2()
                self.name.draw(win)
            elif self.selected_part == "B3":
                self.name = Name_B3()
                self.name.draw(win)
            elif self.selected_part == "B4":
                self.name = Name_B4()
                self.name.draw(win)
            elif self.selected_part == "B5":
                self.name = Name_B5()
                self.name.draw(win)
            elif self.selected_part == "B6":
                self.name = Name_B6()
                self.name.draw(win)
            elif self.selected_part == "C1":
                self.name = Name_C1()
                self.name.draw(win)
            elif self.selected_part == "C2":
                self.name = Name_C2()
                self.name.draw(win)
            elif self.selected_part == "C3":
                self.name = Name_C3()
                self.name.draw(win)
            elif self.selected_part == "C4":
                self.name = Name_C4()
                self.name.draw(win)
            elif self.selected_part == "C5":
                self.name = Name_C5()
                self.name.draw(win)
            elif self.selected_part == "C6":
                self.name = Name_C6()
                self.name.draw(win)
            elif self.selected_part == "D1":
                self.name = Name_D1()
                self.name.draw(win)
            elif self.selected_part == "D2":
                self.name = Name_D2()
                self.name.draw(win)
            elif self.selected_part == "D3":
                self.name = Name_D3()
                self.name.draw(win)
            elif self.selected_part == "D4":
                self.name = Name_D4()
                self.name.draw(win)
            elif self.selected_part == "D5":
                self.name = Name_D5()
                self.name.draw(win)
            elif self.selected_part == "D6":
                self.name = Name_D6()
                self.name.draw(win)
            elif self.selected_part == "E1":
                self.name = Name_E1()
                self.name.draw(win)
            elif self.selected_part == "E2":
                self.name = Name_E2()
                self.name.draw(win)
            elif self.selected_part == "E3":
                self.name = Name_E3()
                self.name.draw(win)
            elif self.selected_part == "E4":
                self.name = Name_E4()
                self.name.draw(win)
            elif self.selected_part == "E5":
                self.name = Name_E5()
                self.name.draw(win)
            elif self.selected_part == "E6":
                self.name = Name_E6()
                self.name.draw(win)
            elif self.selected_part == "F1":
                self.name = Name_F1()
                self.name.draw(win)
            elif self.selected_part == "F2":
                self.name = Name_F2()
                self.name.draw(win)
            elif self.selected_part == "F3":
                self.name = Name_F3()
                self.name.draw(win)
            elif self.selected_part == "F4":
                self.name = Name_F4()
                self.name.draw(win)
            elif self.selected_part == "F5":
                self.name = Name_F5()
                self.name.draw(win)
            elif self.selected_part == "F6":
                self.name = Name_F6()
                self.name.draw(win)
            elif self.selected_part == "G1":
                self.name = Name_G1()
                self.name.draw(win)
            elif self.selected_part == "G2":
                self.name = Name_G2()
                self.name.draw(win)
            elif self.selected_part == "G3":
                self.name = Name_G3()
                self.name.draw(win)
            else:
                self.name = None

    def got_click(self, x, y):
        if self.part_A1.clicked(x, y):
            self.selected_part = "A1"
            self.pictures.remove(self.part_A1)
            return
        elif self.part_A2.clicked(x, y):
            self.selected_part = "A2"
            self.pictures.remove(self.part_A2)
            return
        elif self.part_A3.clicked(x, y):
            self.selected_part = "A3"
            self.pictures.remove(self.part_A3)
            return
        elif self.part_A4.clicked(x, y):
            self.selected_part = "A4"
            self.pictures.remove(self.part_A4)
            return
        elif self.part_A5.clicked(x, y):
            self.selected_part = "A5"
            self.pictures.remove(self.part_A5)
            return
        elif self.part_A6.clicked(x, y):
            self.selected_part = "A6"
            self.pictures.remove(self.part_A6)
            return
        elif self.part_B1.clicked(x, y):
            self.selected_part = "B1"
            self.pictures.remove(self.part_B1)
            return
        elif self.part_B2.clicked(x, y):
            self.selected_part = "B2"
            self.pictures.remove(self.part_B2)
            return
        elif self.part_B3.clicked(x, y):
            self.selected_part = "B3"
            self.pictures.remove(self.part_B3)
            return
        elif self.part_B4.clicked(x, y):
            self.selected_part = "B4"
            self.pictures.remove(self.part_B4)
            return
        elif self.part_B5.clicked(x, y):
            self.selected_part = "B5"
            self.pictures.remove(self.part_B5)
            return
        elif self.part_B6.clicked(x, y):
            self.selected_part = "B6"
            self.pictures.remove(self.part_B6)
            return
        elif self.part_C1.clicked(x, y):
            self.selected_part = "C1"
            self.pictures.remove(self.part_C1)
            return
        elif self.part_C2.clicked(x, y):
            self.selected_part = "C2"
            self.pictures.remove(self.part_C2)
            return
        elif self.part_C3.clicked(x, y):
            self.selected_part = "C3"
            self.pictures.remove(self.part_C3)
            return
        elif self.part_C4.clicked(x, y):
            self.selected_part = "C4"
            self.pictures.remove(self.part_C4)
            return
        elif self.part_C5.clicked(x, y):
            self.selected_part = "C5"
            self.pictures.remove(self.part_C5)
            return
        elif self.part_C6.clicked(x, y):
            self.selected_part = "C6"
            self.pictures.remove(self.part_C6)
            return
        elif self.part_D1.clicked(x, y):
            self.selected_part = "D1"
            self.pictures.remove(self.part_D1)
            return
        elif self.part_D2.clicked(x, y):
            self.selected_part = "D2"
            self.pictures.remove(self.part_D2)
            return
        elif self.part_D3.clicked(x, y):
            self.selected_part = "D3"
            self.pictures.remove(self.part_D3)
            return
        elif self.part_D4.clicked(x, y):
            self.selected_part = "D4"
            self.pictures.remove(self.part_D4)
            return
        elif self.part_D5.clicked(x, y):
            self.selected_part = "D5"
            self.pictures.remove(self.part_D5)
            return
        elif self.part_D6.clicked(x, y):
            self.selected_part = "D6"
            self.pictures.remove(self.part_D6)
            return
        elif self.part_E1.clicked(x, y):
            self.selected_part = "E1"
            self.pictures.remove(self.part_E1)
            return
        elif self.part_E2.clicked(x, y):
            self.selected_part = "E2"
            self.pictures.remove(self.part_E2)
            return
        elif self.part_E3.clicked(x, y):
            self.selected_part = "E3"
            self.pictures.remove(self.part_E3)
            return
        elif self.part_E4.clicked(x, y):
            self.selected_part = "E4"
            self.pictures.remove(self.part_E4)
            return
        elif self.part_E5.clicked(x, y):
            self.selected_part = "E5"
            self.pictures.remove(self.part_E5)
            return
        elif self.part_E6.clicked(x, y):
            self.selected_part = "E6"
            self.pictures.remove(self.part_E6)
            return
        elif self.part_F1.clicked(x, y):
            self.selected_part = "F1"
            self.pictures.remove(self.part_F1)
            return
        elif self.part_F2.clicked(x, y):
            self.selected_part = "F2"
            self.pictures.remove(self.part_F2)
            return
        elif self.part_F3.clicked(x, y):
            self.selected_part = "F3"
            self.pictures.remove(self.part_F3)
            return
        elif self.part_F4.clicked(x, y):
            self.selected_part = "F4"
            self.pictures.remove(self.part_F4)
            return
        elif self.part_F5.clicked(x, y):
            self.selected_part = "F5"
            self.pictures.remove(self.part_F5)
            return
        elif self.part_F6.clicked(x, y):
            self.selected_part = "F6"
            self.pictures.remove(self.part_F6)
            return
        elif self.part_G1.clicked(x, y):
            self.selected_part = "G1"
            self.pictures.remove(self.part_G1)
            return
        elif self.part_G2.clicked(x, y):
            self.selected_part = "G2"
            self.pictures.remove(self.part_G2)
            return
        elif self.part_G3.clicked(x, y):
            self.selected_part = "G3"
            self.pictures.remove(self.part_G3)
            return
        else:
            self.selected_part = None
            return
