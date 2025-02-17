import pygame

class NPC:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

    def move_towards(self, target_pos):
        direction = (target_pos - self.position).normalize()
        self.position += direction * self.speed