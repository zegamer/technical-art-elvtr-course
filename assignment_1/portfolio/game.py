import pygame
import random
from vector_distance import two_dimension_euclidean_distance
from constants import *
import utils
from npc import NPC

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont("lucidaconsole", 24)
        self.player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
        self.npc = NPC(pygame.Vector2(WIDTH // 2 - 100, HEIGHT // 2), NPC_SPEED)
        self.distance = two_dimension_euclidean_distance(self.player_pos, self.npc.position)
        self.follow_messages = utils.load_messages(FOLLOW_MESSAGES_FILE_PATH)
        self.conversation_messages = utils.load_messages(CONVERSATION_MESSAGES_FILE_PATH)
        self.conversation_tracker = 0
        self.last_message_time = pygame.time.get_ticks()
        self.npc_message = ""
        self.running = True

    def run(self):
        while self.running:
            self.current_time = pygame.time.get_ticks()
            self.screen.fill(BLACK)
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            pygame.time.delay(30)  # Small delay to control speed

    def handle_events(self):
        for event in pygame.event.get():
            if utils.quit_condition(event):
                self.running = False

    def update(self):
        self.player_pos = pygame.Vector2(pygame.mouse.get_pos())
        self.distance = two_dimension_euclidean_distance(self.player_pos, self.npc.position)

        if self.distance > FOLLOW_DISTANCE:
            self.npc.move_towards(self.player_pos)
            utils.create_rect_triangle(self.screen, TERMINAL_GREEN, self.player_pos, self.npc.position, 2)

            if (random.randint(0, 100) < 2) and (self.current_time - self.last_message_time > MESSAGE_DISPLAY_TIME):
                self.npc_message = random.choice(self.follow_messages)
                self.conversation_tracker = 0
                self.last_message_time = self.current_time

        elif self.distance < FOLLOW_DISTANCE:
            if self.current_time - self.last_message_time > MESSAGE_DISPLAY_TIME:
                self.npc_message = self.conversation_messages[self.conversation_tracker % len(self.conversation_messages)]
                self.conversation_tracker += 1
                self.last_message_time = self.current_time

    def draw(self):
        self.screen.blit(self.font.render(f"Dist: {round(self.distance, 3)}", True, WHITE), (10, 10))
        pygame.draw.circle(self.screen, TERMINAL_GREEN, self.player_pos, 20)  # Player
        pygame.draw.circle(self.screen, RED, self.npc.position, 15)  # NPC
        text_surface = self.font.render(self.npc_message, True, WHITE)
        self.screen.blit(text_surface, (self.npc.position.x + 20, self.npc.position.y - 20))
