import pygame
from constants import GREEN, BLOCK_SIZE

class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = pygame.Vector2(0, -1)
        self.grow = False
        
    def draw(self, screen):
        for block in self.body:
            pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))