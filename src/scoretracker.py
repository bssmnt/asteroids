import pygame
from constants import *

class ScoreTracker():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 55)
        self.color = WHITE
    
    def score_add(self, amount=1):
        self.score += amount
    
    def draw(self, screen):
        score_tracker = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_tracker, (50, 50))