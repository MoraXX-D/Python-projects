import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_event(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right =True
    elif event.key == pygame.K_LEFT:
        #move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a new bullet and add it to bullet group
        new_bullet =Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,screen,ship,bullets):
    '''respond to keypress and mouse event'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:  #register keypress
            check_keydown_event( event, ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
                
                     

def update_screen(ai_settings,screen,ship,alien,bullets):
    '''Update image on the screen and fkip to a new screen'''
    #redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    # Make the most recently drawn screen visible
    pygame.display.flip()

def create_fleet(ai_settings,screen,aliens):
    '''create a full fleet of alien'''
    #create an alien and find the number of alien in a row
    #spacing between each alien is equal to one alien of width
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    #create the first row of alien
    for alien in range(number_aliens_x):
        #create an alien and place it in the row
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width * number_aliens_x
        aliens.add(alien)