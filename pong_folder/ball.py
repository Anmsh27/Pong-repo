import pygame

class Ball():
	def __init__(self, x, y, vel, yvel):
		self.x = x
		self.y = y
		self.vel = vel
		self.yvel = yvel
		self.image = pygame.image.load('resources/ball.png').convert_alpha()
		self.rect = self.image.get_rect(topleft=(self.x, self.y), left=self.x, bottomleft=(self.x, self.y + 51),
										midbottom=(self.x + 26, self.y + 51), bottomright=(self.x + 51, self.y + 51),
										right=self.x + 51, topright=(self.x + 51, self.y), top=self.y, bottom=self.y + 51)

	def update(self):
		self.x += self.vel
		self.y += self.yvel