import sys

import pygame

from settings import Settings
from ship import Ship
import game_function as gf

ai_settings = Settings()

from pygame.sprite import Group

def run_game():
	pygame.init()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(screen, ai_settings)
	
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(ai_settings, screen, aliens)

	while True:
		gf.check_events(ship, bullets, ai_settings, screen)
		ship.update()
		gf.update_bullet(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets, aliens)
		
run_game()
