import pygame
from settings import *
from player2 import Player_2

class Player_1(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        tie_fighter = pygame.image.load('Graphics/tie.png').convert_alpha()
        tie_fighter_scale = pygame.transform.rotozoom(tie_fighter, 90, 0.15)

        self.image = tie_fighter_scale
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 15, WINDOW_HEIGHT / 2))

    def moveUp(self):

        if self.rect.top >= 0:
            self.rect.y -= MOVEMENT_SPEED
    
    def moveDown(self):
        if self.rect.bottom <= WINDOW_HEIGHT:
            self.rect.y += MOVEMENT_SPEED
    
    def moveRight(self):
        if self.rect.right <= WINDOW_WIDTH / 2 - 2:
            self.rect.x += MOVEMENT_SPEED
    
    def moveLeft(self):
        if self.rect.left >= 0:
            self.rect.x -= MOVEMENT_SPEED

    def create_bullet(self):
        return Player1_Bullet(self.rect.centerx, self.rect.centery)
    
    def create_missle(self):
        return Player1_Missle(self.rect.centerx, self.rect.centery)

class Player1_Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((40,5))
        self.image.fill('Red')
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
    
    def update(self):
        self.rect.x += BULLET_SPEED

        if self.rect.x >= WINDOW_WIDTH + 200:
            self.kill()

class Player1_Missle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((40, 10))
        self.image.fill('Yellow')
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.group = pygame.sprite.Group()

    def update(self):
        self.rect.x += MISSLE_SPEED
