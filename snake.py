import pygame
from constants import GREEN, BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = pygame.Vector2(0, -1)
        self.grow = False

    def draw(self, screen):
        for block in self.body:
            pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
    
    def move(self):
        if not self.grow:
            tail = self.body.pop(0)  # Remove the last block unless growing
        head = self.body[-1]
        new_head = (head[0] + self.direction.x * BLOCK_SIZE, head[1] + self.direction.y * BLOCK_SIZE)
        self.body.append(new_head)
        self.grow = False      
          
    def grow_snake(self):
        self.grow = True