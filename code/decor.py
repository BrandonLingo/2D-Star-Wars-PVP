import pygame
from settings import *


"""
Not actually implented in the game, it was a concept for background animations.
Do not actually blit this to the screen, x_decor.png is no longer in the graphics
folder.
"""

class X_Decor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        xwing_decor = pygame.image.load('Graphics/x_decor.png')
        self.image = pygame.transform.scale(xwing_decor, (100,50))
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH , 0))
        self.timer = pygame.time.get_ticks() 

    def update(self):
        
        if self.timer >= 1000:
            self.rect.x -= 6
            self.rect.y += 6