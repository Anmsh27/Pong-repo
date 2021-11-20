import pygame
import math
import random
import time
from player import Paddle
from ball import Ball
from sys import exit
pygame.init()

screen = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Pong")
bg = (0, 0, 0)
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)
gui_state = True
gui_font = pygame.font.Font(None, 200)
gui_font_rendered = gui_font.render("PONG", True, (255, 255, 255))
start_font = pygame.font.Font(None, 100)
start_font_rendered = start_font.render("Press any key to start", True, (255, 255, 255))
player1_score = 0
player2_score = 0
paddle1 = Paddle(10, 200, 1)
paddle2 = Paddle(1280, 200, 2)
client_number = 0
random_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random_choice = random.choice(random_list)
acceptance_list = [1, 2, 4, 7, 9]
list_of_possible_x_vel = [-7.5, -7, -6.5, -6, -5.5, 5.5, 6, 6.5, 7, 7.5]
list_of_possible_y_vel = [-6, -5.5, -5, 5, 5.5, 6]
ball_x_vel = random.choice(list_of_possible_x_vel)
ball_y_vel = random.choice(list_of_possible_y_vel)
ball = Ball(624, 374, ball_x_vel, ball_y_vel)
paddle1_rect = paddle1.rect
paddle2_rect = paddle2.rect
ball_rect = ball.rect

def collision_with_paddle2():
	return True if (
					ball.vel > 0 and ball.y >= paddle2.y - 45 and ball.y <= paddle2.y + 150
					and ball.x + 51 >= paddle2.x
					) else False

def collision_with_paddle1():
	return True if (
					ball.vel < 0 and ball.y >= paddle1.y - 45 and ball.y <= paddle1.y + 150
					and ball.x <= paddle1.x
					) else False

while True:
	screen.fill(bg)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN and gui_state:
			gui_state = False 

	if gui_state:
		screen.blit(gui_font_rendered, (450, 75))
		screen.blit(start_font_rendered, (310, 400))

	if not gui_state:

		screen.blit(paddle1.image, (paddle1.x, paddle1.y))
		screen.blit(paddle2.image, (paddle2.x, paddle2.y))
		screen.blit(ball.image, (ball.x, ball.y))
		score1 = font.render("Player 1's score is " + str(player1_score), True, (255, 255, 255))
		score2 = font.render("Player 2's score is " + str(player2_score), True, (255, 255, 255))
		screen.blit(score1, (460, 0))
		screen.blit(score2, (460, 50))
		paddle1.update()
		paddle2.update()
		ball.update()

		if collision_with_paddle2():
			ball.vel = -ball.vel
			if random_choice in acceptance_list:
				ball.yvel = -ball.yvel
			ball_x_vel = random.choice(list_of_possible_x_vel)
			ball_y_vel = random.choice(list_of_possible_y_vel)
			random_choice = random.choice(random_list)
			ball.update()

		if collision_with_paddle1():
			ball.vel = abs(ball.vel)
			if random_choice in acceptance_list:
				ball.yvel = abs(ball.yvel)
			ball_x_vel = random.choice(list_of_possible_x_vel)
			ball_y_vel = random.choice(list_of_possible_y_vel)
			random_choice = random.choice(random_list)
			ball.update()


		if ball.y < 0 or ball.y + 51 > 800:
			ball.yvel = -ball.yvel

		if paddle1.y < 0:
			paddle1.y = 0

		if paddle1.y + 150 > 800:
			paddle1.y = 650

		if paddle2.y < 0:
			paddle2.y = 0

		if paddle2.y + 150 > 800:
			paddle2.y = 650

		if ball.x > 1300:
			player2_score += 1
			ball_x_vel = random.choice(list_of_possible_x_vel)
			ball_y_vel = random.choice(list_of_possible_y_vel)
			ball.x = 624
			ball.y = 374
			paddle1.y = 200
			paddle2.y = 200
			screen.blit(ball.image, (ball.x, ball.y))
			gui_state = True

		if ball.x < 0:
			player1_score += 1
			ball_x_vel = random.choice(list_of_possible_x_vel)
			ball_y_vel = random.choice(list_of_possible_y_vel)
			ball.x = 624
			ball.y = 374
			paddle1.y = 200
			paddle2.y = 200
			screen.blit(ball.image, (ball.x, ball.y))
			gui_state = True

		ball.update()

	pygame.display.update()
	clock.tick(60)
