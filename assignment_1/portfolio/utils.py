import pygame
import os

def create_rect_triangle(screen: pygame.Surface, color: tuple, pos_1: pygame.Vector2, pos_2: pygame.Vector2, size: int) -> None:
    pygame.draw.line(screen, color, pos_1, pos_2, size)
    pygame.draw.line(screen, color, pos_2, (pos_1[0], pos_2[1]), size)
    pygame.draw.line(screen, color, pos_1, (pos_1[0], pos_2[1]), size)


def quit_condition(event: pygame.event.Event) -> bool:
    return event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or pygame.K_q))

def load_messages(file_path: str) -> list:
    messages = []
    with open(os.getcwd() + "/" + file_path, "r") as file:
        for i in file.readlines():
            messages.append(i.strip())
    return messages