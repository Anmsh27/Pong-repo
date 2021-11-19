import pygame

class Paddle():
	def __init__(self, x, y, player_num):
		self.player_num = player_num
		self.x = x
		self.y = y
		self.image = pygame.image.load('resources/Paddle.png').convert_alpha()
		self.rect = self.image.get_rect(topleft=(self.x, self.y), left=self.x, bottomleft=(self.x, self.y + 150),
										midbottom=(self.x + 5, self.y + 150), bottomright=(self.x + 10, self.y + 150),
										right=self.x + 10, topright=(self.x + 10, self.y), top=self.y, bottom=self.y + 150)
		self.bottom = self.y + 150
		self.top = self.y

	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_s] and self.player_num == 1:
			self.y += 13
		elif keys[pygame.K_w] and self.player_num == 1:
			self.y -= 13
		elif keys[pygame.K_DOWN] and self.player_num == 2:
			self.y += 13
		elif keys[pygame.K_UP] and self.player_num == 2:
			self.y -= 13
		self.rect = self.image.get_rect(topleft=(self.x, self.y), left=self.x, bottomleft=(self.x, self.y + 150),
										midbottom=(self.x + 5, self.y + 150), bottomright=(self.x + 10, self.y + 150),
										right=self.x + 10, topright=(self.x + 10, self.y), top=self.y, bottom=self.y + 150)