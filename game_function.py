import sys
import pygame

from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullet_allow:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
		ship.rect.centerx += 1
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		ship.rect.centerx -= 1
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygmae.K_q:
		sys.exit()

def check_keyup_events(event, ai_settings, screen, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


"按键处理函数"
def check_events(ship, bullets, ai_settings, screen):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ai_settings, screen, ship)
				
"屏幕刷新函数"		
def update_screen(ai_settings, screen, ship, bullets, aliens):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	pygame.display.flip()
	
def check_mouse_click(ai_settings):
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			ai_settings.screen_spin = True
	
	
def update_bullet(bullets):
	bullets.update()
	#删除消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))
	
	
def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
	
def create_alien(ai_settings, screen, aliens, alien_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	aliens.add(alien)

#创建外星人组
def create_fleet(ai_settings, screen, aliens):
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	
	for alien_number in range(number_aliens_x):
		create_alien(ai_settings, screen, aliens, alien_number)
		
		
