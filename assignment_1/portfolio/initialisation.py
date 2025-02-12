import pygame
from constants import WIDTH, HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Font
font = pygame.font.SysFont("lucidaconsole", 24)
npc_message = ""
