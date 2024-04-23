import pygame

class Ship():
    def __init__(self,ai_setting,screen):
        '''initialize the ship and set its starting position'''
        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect =  screen.get_rect()

        #Start new ship at the bottom of center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #store the decimal value for ship center
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position based on the movement op flag"""
        #update the ship center value not the rect  
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at current location"""
        self.screen.blit(self.image,self.rect)
