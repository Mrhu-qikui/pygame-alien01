import sys
import pygame

from bullet import Bullet

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
def update_screen(ai_settings, screen, ship, bullets):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
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
