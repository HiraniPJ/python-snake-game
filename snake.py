import pygame
from constants import GREEN, BLOCK_SIZE

class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = pygame.Vector2(0, -1)
        self.grow = False