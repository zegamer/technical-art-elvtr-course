import pygame
from constants import WIDTH, HEIGHT

# Initialize player and NPC positions
player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
npc_pos = pygame.Vector2(WIDTH // 2 - 100, HEIGHT // 2)

# NPC settings
NPC_SPEED = 4
FOLLOW_DISTANCE = 50  # NPC follows if beyond this distance