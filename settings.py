import os
import pygame

# win
WIN_WIDTH = 1024
WIN_HEIGHT = 600

# path
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "images")
NAME_PATH = os.path.join(os.path.dirname(__file__), "images/name")
PART_PATH = os.path.join(os.path.dirname(__file__), "images/part")

# background
background = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "ENV.png")), (WIN_WIDTH, WIN_HEIGHT))

# images name
name_1 = pygame.transform.scale(pygame.image.load(os.path.join(NAME_PATH, "1.jpg")), (500, 450))
name_2 = pygame.transform.scale(pygame.image.load(os.path.join(NAME_PATH, "2.jpg")), (500, 450))
name_3 = pygame.transform.scale(pygame.image.load(os.path.join(NAME_PATH, "3.jpg")), (500, 450))

# image part
part_1 = pygame.transform.scale(pygame.image.load(os.path.join(PART_PATH, "1.jpg")), (70, 70))
part_2 = pygame.transform.scale(pygame.image.load(os.path.join(PART_PATH, "2.jpg")), (70, 70))
part_3 = pygame.transform.scale(pygame.image.load(os.path.join(PART_PATH, "3.jpg")), (70, 70))

