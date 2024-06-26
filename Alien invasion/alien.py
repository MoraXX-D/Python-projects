import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    '''A class to represent a single alien in the first fleet'''
    def __init__(self,ai_settings,screen):
        '''Inittialize the alien and set its starting position'''
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the alien image and set it to rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien in its current location"""
        self.screen.blit(self.image,self.rect)