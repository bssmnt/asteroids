import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from scoretracker import ScoreTracker

def main():
    pygame.init()
    
    timer = 0
    dt = 0
    clock = pygame.time.Clock()
    score_tracker = ScoreTracker()
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
    
    score_threshold = 1
    speed_multiplier = 1.0
    speed_increase_factor = 0.05
  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        timer -= dt
        
        screen.fill(BLACK)

        for i in updatable:
            i.update(dt)

        for a in asteroids:
            if player.collides_with(a) == True:
                print("Game over!")
                sys.exit()
            for shot in player_shots:
                if shot.collides_with(a):
                    a.split()
                    shot.kill()
                    score_tracker.score_add()

                    if score_tracker.score % score_threshold == 0:
                        speed_multiplier += speed_increase_factor
                        for a in asteroids:
                            a.increase_speed(speed_multiplier)
        
        score_tracker.draw(screen)
                
        for i in drawable:
            i.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()