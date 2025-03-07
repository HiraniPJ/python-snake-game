import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
