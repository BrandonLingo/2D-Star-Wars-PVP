import pygame, sys
from settings import *
from debug import debug 
from player1 import Player_1, Player1_Bullet
from player2 import Player_2
from decor import X_Decor

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Star Wars')
        self.clock = pygame.time.Clock()

        # Game Things
        self.game_actice = True
        self.player_1_health = PLAYERS_HEALTH
        self.player_2_health = PLAYERS_HEALTH

        background = pygame.image.load('Graphics/background.jpg')

        # Scale Factor
        bg_height = pygame.image.load('Graphics/background.jpg').get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height
        background_height = background.get_height() * self.scale_factor
        background_width = background.get_width() * self.scale_factor
        self.full_background = pygame.transform.scale(background, (background_width, background_height))

        # Sprite Groups
        self.collision_sprite = pygame.sprite.Group()
        self.bullet_group1 = pygame.sprite.Group()
        self.missle_group1 = pygame.sprite.Group()
        self.bullet_group2 = pygame.sprite.Group()
        self.decor_sprite = pygame.sprite.Group()

        # Sprites
        self.player_1 = Player_1(self.collision_sprite)
        self.player_2 = Player_2(self.collision_sprite)
        self.x_decor = X_Decor(self.decor_sprite)

        # Player 1 Firing Recharge
        self.fire_ready = True
        self.laser_timer = None
        self.current_time = None
        
        # Player 1 Missle Rechare
        self.missle_ready = True
        self.missle_timer_1 = None
        self.missle_current_time = None


        #Player 2 Firing Recharge
        self.fire_ready_2 = True
        self.laser_timer_2 = None

        # Font
        self.font = pygame.font.Font(None, 35)

        # Music
        self.bg_music = pygame.mixer.Sound('audio/theme.wav')
        self.bg_music.set_volume(0.2)
        self.bg_music.play()

        # Audio
        self.tie_shoot_sound = pygame.mixer.Sound('audio/Tie_shoot_sound.wav')
        self.x_wing_shoot = pygame.mixer.Sound('audio/X_wing_shoot.wav')
        self.death1_sound = pygame.mixer.Sound('audio/darth_death.wav')
        self.death1_sound.set_volume(0.2)

        # Images 
        self.rebel_logo = pygame.image.load('Graphics/rebel_logo.png')
        self.rebel_logo_rect = self.rebel_logo.get_rect(center=(WINDOW_WIDTH /2 , WINDOW_HEIGHT / 2 - 100 ))
        self.empire_logo = pygame.image.load('Graphics/empire_logo.png')
        self.empire_logo = pygame.transform.scale(self.empire_logo, (300,300))
        self.empire_logo_rect = self.empire_logo.get_rect(center=(WINDOW_WIDTH /2 , WINDOW_HEIGHT / 2 - 100 ))


    def collisions(self):
        if pygame.sprite.spritecollide(self.player_2, self.bullet_group1, True, pygame.sprite.collide_mask):
            debug('Collision')
            self.player_2_health -= 1
            print('Player 2 health: ', self.player_2_health)    
        
        if pygame.sprite.spritecollide(self.player_1, self.bullet_group2, True, pygame.sprite.collide_mask):
            self.player_1_health -= 1
            print('Player 1 Health: ', self.player_1_health)
    
    def end_game(self):
 
        if self.player_1_health == 0 or self.player_2_health == 0:
            self.game_actice = False
            
    def show_font(self):

        # Health Font
        self.player_1_font = self.font.render(f'Health: {self.player_1_health}', False, 'Red')
        self.player_2_font = self.font.render(f'Health: {self.player_2_health}', False, 'Yellow')

        # Blit to Screen
        self.screen.blit(self.player_1_font, (0,0))
        self.screen.blit(self.player_2_font, (WINDOW_WIDTH - 120, 0))
        #self.screen.blit(self.missle1_ready_font, (WINDOW_WIDTH / 2 - 300, 0))

    def rand_audio(self):

        # Player 1 death sound
        if self.player_1_health == 0:
            self.death1_sound.play()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Player 1 Shooting
                if self.game_actice:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if self.fire_ready:
                                self.bullet_group1.add(self.player_1.create_bullet())
                                self.fire_ready = False
                                self.laser_timer = pygame.time.get_ticks() / 1000
                                self.tie_shoot_sound.play()
                            if not self.fire_ready:
                                self.current_time = pygame.time.get_ticks() / 1000
                                if self.current_time - self.laser_timer >= BULLET_TIME:
                                    self.fire_ready = True

                        # Player 1 Missle Shooting
                        if event.key == pygame.K_e:
                            if self.missle_ready:
                                self.missle_group1.add(self.player_1.create_missle())
                                self.missle_ready = False
                                self.missle_timer_1 = pygame.time.get_ticks()// 1000
                            if not self.missle_ready:
                                self.missle_current_time = pygame.time.get_ticks() // 1000
                                if self.missle_current_time - self.missle_timer_1 >= MISSLE_TIME:
                                    self.missle_ready = True



                        #Player 2 Shooting
                        if event.key == pygame.K_RCTRL:
                            if self.fire_ready_2:
                                self.bullet_group2.add(self.player_2.create_bullet())
                                self.fire_ready_2 = False
                                self.laser_timer_2 = pygame.time.get_ticks() / 1000
                                self.x_wing_shoot.play()
                            if not self.fire_ready_2:
                                current_timer_2 = pygame.time.get_ticks() / 1000
                                if current_timer_2 - self.laser_timer_2 >= BULLET_TIME:
                                    self.fire_ready_2 = True
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.game_actice = True
                            self.player_1 = Player_1(self.collision_sprite)
                            self.player_2 = Player_2(self.collision_sprite)
                            self.player_1_health = PLAYERS_HEALTH
                            self.player_2_health = PLAYERS_HEALTH
                            

            if self.game_actice:
                keys = pygame.key.get_pressed()

                # Player 1 Movement
                if keys[pygame.K_w]:
                    self.player_1.moveUp()
                if keys[pygame.K_s]:
                    self.player_1.moveDown()
                if keys[pygame.K_a]:
                    self.player_1.moveLeft()
                if keys[pygame.K_d]:
                    self.player_1.moveRight()

                # Player 2 Movement
                if keys[pygame.K_UP]:
                    self.player_2.moveUp()
                if keys[pygame.K_DOWN]:
                    self.player_2.moveDown()
                if keys[pygame.K_RIGHT]:
                    self.player_2.moveRight()
                if keys[pygame.K_LEFT]:
                    self.player_2.moveLeft()

                # Objects on Screen
                self.screen.blit(self.full_background, (0,0))
                #self.decor_sprite.draw(self.screen)
                #c zxself.decor_sprite.update()

                pygame.draw.line(self.screen, 'white', (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 2)
                self.collision_sprite.draw(self.screen)
                self.show_font()

                # Drawing and upadting Bullets
                self.bullet_group1.draw(self.screen)
                self.bullet_group1.update()
                self.bullet_group2.draw(self.screen)
                self.bullet_group2.update()
                self.missle_group1.draw(self.screen)
                self.missle_group1.update()
                
                self.collisions()

                self.end_game()
                self.rand_audio()
            else:
                self.restart_text = self.font.render('Click Space To Restart', False, 'White')
                self.screen.blit(self.restart_text, (WINDOW_WIDTH / 2 - 140, WINDOW_HEIGHT / 2 + 150))
                self.player_1.kill()
                self.player_2.kill()

                # Display winners logo
                if self.player_1_health == 0:
                    self.screen.blit(self.rebel_logo, self.rebel_logo_rect)
                elif self.player_2_health == 0:
                    self.screen.blit(self.empire_logo, self.empire_logo_rect)

            pygame.display.update()
            self.clock.tick(FRAME_RATE)
            
if __name__ == '__main__':
    game = Game()
    game.run()