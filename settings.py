import os
import pygame

# win
WIN_WIDTH = 1024
WIN_HEIGHT = 600

# background
background = pygame.transform.scale(pygame.image.load(os.path.join("images/ENV.png")), (WIN_WIDTH, WIN_HEIGHT))

# images name
name_1 = pygame.transform.scale(pygame.image.load(os.path.join("images/name/1.jpg")), (500, 450))
name_2 = pygame.transform.scale(pygame.image.load(os.path.join("images/name/2.jpg")), (500, 450))
name_3 = pygame.transform.scale(pygame.image.load(os.path.join("images/name/3.jpg")), (500, 450))

# image part
part_1 = pygame.transform.scale(pygame.image.load(os.path.join("images/part/1.jpg")), (70, 70))
part_2 = pygame.transform.scale(pygame.image.load(os.path.join("images/part/2.jpg")), (70, 70))
part_3 = pygame.transform.scale(pygame.image.load(os.path.join("images/part/3.jpg")), (70, 70))

