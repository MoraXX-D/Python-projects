import pygame
from pygame.sprite import Group
from settings import settings
from ship import Ship
from alien import Alien
import game_function as gf

def run_game():
    #initilizing the game,settiing and create a screen object
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    #Make a group to store bullet in
    bullets =Group()
    aliens = Group()
    #make an alien
    # alien = Alien(ai_settings,screen)
    gf.create_fleet(ai_settings,screen,aliens)

    #Start the main loop for the game
    while True:
        # Watch the keyboard and mouse event
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()