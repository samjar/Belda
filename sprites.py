# Sprite classes
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		# initialize the player's attributes
		self.groups = game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pygame.Surface((TILESIZE, TILESIZE))
		self.image.fill(YELLOW)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.speed_y = 0
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
		self.move_left = self.move_right = self.move_up = self.move_down = False

	def move(self, movex, movey):
		self.speed_x = movex
		self.speed_y = movey

	def collision_with_walls(self):
		hits = pygame.sprite.spritecollide(self.game.player, self.game.walls, False)
		if hits:
			for wall in self.game.walls:
				if self.speed_x > 0:
					print("right")
					self.rect.right = wall.rect.left
				if self.speed_x < 0:
					print("left")
					self.rect.left = wall.rect.right
				if self.speed_y > 0:
					print("down")
					self.rect.bottom = wall.rect.top
				if self.speed_y < 0:
					print("up")
					self.rect.top = wall.rect.bottom


	def update(self):
		# update player movement
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

		self.collision_with_walls()

		self.speed_x = 0
		self.speed_y = 0

class Mountain(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

