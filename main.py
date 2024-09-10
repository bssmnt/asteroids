import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    black_bg = (0, 0, 0)
    timer = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers = (player_shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(black_bg)

        for i in updatable:
            i.update(dt)

            timer -= dt

        for a in asteroids:
            if player.collides_with(a) == True:
                print("Game over!")
                sys.exit()
            for shot in player_shots:
                if shot.collides_with(a):
                    a.split()
                    shot.kill()
                

        

        for i in drawable:
            i.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()