import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    black_bg = (0, 0, 0)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(black_bg)
        player.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()