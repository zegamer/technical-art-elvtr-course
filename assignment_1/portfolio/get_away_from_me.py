import random
import pygame
from vector_distance import two_dimension_euclidean_distance
import utils

pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TERMINAL_GREEN = (74, 246, 38)

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Grid settings
CELL_SIZE = 50  # Distance between lines
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# Initialize player and NPC positions
player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
npc_pos = pygame.Vector2(WIDTH // 2 - 100, HEIGHT // 2)
NPC_SPEED = 4
FOLLOW_DISTANCE = 50  # NPC follows if beyond this distance

FOLLOW_MESSAGES = utils.load_messages("assignment_1/portfolio/annoying_messages.txt")
CONVERSATION_MESSAGES = utils.load_messages("assignment_1/portfolio/conversation.txt")

CONVERSATION_TRACKER = 0
MESSAGE_DISPLAY_TIME = 2000  # Time to display each message in milliseconds
last_message_time = pygame.time.get_ticks()

# Font
font = pygame.font.SysFont("lucidaconsole", 24)
npc_message = ""

# Game loop
running = True
while running:
    current_time = pygame.time.get_ticks()
    screen.fill(BLACK)

    for event in pygame.event.get():
        if utils.quit_condition(event):
            running = False

    player_pos = pygame.Vector2(pygame.mouse.get_pos())

    # Calculate distance between player and NPC and display it
    distance = two_dimension_euclidean_distance(player_pos, npc_pos)
    screen.blit(font.render(f"Dist: {round(distance, 3)}", True, WHITE), (10, 10))

    if distance > FOLLOW_DISTANCE:
        npc_pos = npc_pos.move_towards(player_pos, NPC_SPEED)

        # Draw lines connecting player and NPC
        utils.create_rect_triangle(screen, TERMINAL_GREEN, player_pos, npc_pos, 2)

        if (random.randint(0, 100) < 2) and (current_time - last_message_time > MESSAGE_DISPLAY_TIME):
            npc_message = random.choice(FOLLOW_MESSAGES)
            CONVERSATION_TRACKER = 0
            last_message_time = current_time

    elif distance < FOLLOW_DISTANCE:
        if current_time - last_message_time > MESSAGE_DISPLAY_TIME:
            npc_message = CONVERSATION_MESSAGES[CONVERSATION_TRACKER % len(CONVERSATION_MESSAGES)]
            CONVERSATION_TRACKER += 1
            last_message_time = current_time

    # Draw player and NPC
    pygame.draw.circle(screen, TERMINAL_GREEN, player_pos, 20)  # Player
    pygame.draw.circle(screen, RED, npc_pos, 15)  # NPC

    # Display NPC's message
    text_surface = font.render(npc_message, True, WHITE)
    screen.blit(text_surface, (npc_pos.x + 20, npc_pos.y - 20))

    # Update display
    pygame.display.flip()
    pygame.time.delay(30)  # Small delay to control speed

pygame.quit()
