import sys

import pygame

from settings import Settings
from ship import Ship
from play_button import Button
import game_functions as gf
from game_stats import GameStats
from pygame.sprite import Group

def run_game():
    """Method to run entire game"""

    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make sprites and groups
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # end flag
    game_done = False
    # Start the main loop for the game
    while not game_done:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        # if gf.get_number_aliens() == 0:
        #     game_done = True

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
