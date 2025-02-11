import random
import pygame
from vector_distance import two_dimension_euclidean_distance
import utils

# pygame.init()

# # Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# TERMINAL_GREEN = (74, 246, 38)

# WIDTH, HEIGHT = 1280, 720
# screen = display.set_mode((WIDTH, HEIGHT))

# # Grid settings
# CELL_SIZE = 50  # Distance between lines
# CENTER_X = WIDTH // 2
# CENTER_Y = HEIGHT // 2

# clock = time.Clock()
# running = True


# while running:
#     for event in general_events.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(BLACK)

#     # for x in range(0, WIDTH, CELL_SIZE):  # Vertical lines
#     #     pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT), 1)
#     # for y in range(0, HEIGHT, CELL_SIZE):  # Horizontal lines
#     #     pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y), 1)

#     # Draw x-axis and y-axis
#     pygame.draw.line(screen, GRAY, (CENTER_X, 0), (CENTER_X, HEIGHT), 2)  # Y-axis
#     pygame.draw.line(screen, GRAY, (0, CENTER_Y), (WIDTH, CENTER_Y), 2)  # X-axis
    
#     pygame.draw.line(screen, TERMINAL_GREEN, (CENTER_X, CENTER_Y), mouse_events.get_pos(), 2)

#     # Draw origin point
#     draw.circle(screen, TERMINAL_GREEN, mouse_events.get_pos(), 10)

#     display.flip()

# quit()



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

FOLLOW_MESSAGES = utils.load_messages("assignment_1\portfolio\conversation.txt")

# Read from conversation.txt
CONVERSATION_MESSAGES = utils.load_messages("assignment_1/portfolio/conversation.txt")

CONVERSATION_TRACKER = 0

# Font
font = pygame.font.SysFont("lucidaconsole", 24)
npc_message = ""

# Game loop
clock = pygame.time.Clock()
running = True
while running:
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

        # TODO: 
        # Finish conversation.txt
        # 1. NPC has a conversation with player when they are close
        # 2. NPC says a message from the conversation.txt file
        # 3. NPC says a message from the FOLLOW_MESSAGES list when they are far

        # Draw lines connecting player and NPC
        utils.create_rect_triangle(screen, TERMINAL_GREEN, player_pos, npc_pos, 2)
                
        if random.randint(0, 100) < 2:
            npc_message = random.choice(FOLLOW_MESSAGES)
            CONVERSATION_TRACKER = 0
        else:
            if random.randint(0, 100) < 5: 
                npc_message = CONVERSATION_MESSAGES[
                    CONVERSATION_TRACKER % len(CONVERSATION_MESSAGES)]
                CONVERSATION_TRACKER += 1

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
