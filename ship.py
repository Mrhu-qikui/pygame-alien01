import pygame



class Ship():
	
	def __init__(self, screen, ai_settings):
		
		self.screen = screen
		
		self.image = pygame.image.load('timg.jpg')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		if ai_settings.screen_spin:
			self.rect.bottom = self.screen_rect.bottom
		else:
			self.rect.midleft = self.screen_rect.midleft
		self.moving_right = False
		self.moving_left = False
		
		self.ai_settings = ai_settings
		self.center = float(self.rect.centerx)
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ai_settings.ship_speed_factor
			
		self.rect.centerx = self.center
		
