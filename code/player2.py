import pygame
from settings import *

class Player_2(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        x_wing = pygame.image.load('Graphics/x-wing.png').convert_alpha()
        x_wing_scaled = pygame.transform.rotozoom(x_wing, 90, 0.01)

        self.image = x_wing_scaled
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH - 100, WINDOW_HEIGHT / 2))

        # Mask
        self.mask = pygame.mask.from_surface(self.image)
    
    def moveUp(self):
        if self.rect.top >= 0:
            self.rect.y -= MOVEMENT_SPEED
    
    def moveDown(self):
        if self.rect.bottom <= WINDOW_HEIGHT:
            self.rect.y += MOVEMENT_SPEED
    
    def moveRight(self):
        if self.rect.right <= WINDOW_WIDTH:
            self.rect.x += MOVEMENT_SPEED

    def moveLeft(self):
        if self.rect.left >= WINDOW_WIDTH / 2 + 5:
            self.rect.x -= MOVEMENT_SPEED
    
    def create_bullet(self):
        return Player2_Bullet(self.rect.centerx, self.rect.centery)

class Player2_Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((40,5))
        self.image.fill('Green')
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
    
    def update(self):
        self.rect.x -= BULLET_SPEED

        if self.rect.x <= -100:
            self.kill()
            print('Kill')