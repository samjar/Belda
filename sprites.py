# Sprite classes
import pygame
import random
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		# initialize the player's attributes
		self.groups = game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pygame.Surface((64, 64), pygame.SRCALPHA)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.speed_y = 0
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
		self.nextRoom = False

	def move(self, movex, movey):
		self.speed_x = movex
		self.speed_y = movey
		print(self.speed_x, self.speed_y)
		print(self.game.current_room)

	def collision_with_walls(self):
		for wall in self.game.walls:
			if pygame.sprite.collide_rect(self.game.player, wall):
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

		if self.rect.x < 0:
			#switchroom on levellist x axis (-1)
			#self.game.draw_map()
			self.game.current_room -= 1
			self.nextRoom = True
			self.rect.x = WIDTH - TILESIZE
		elif self.rect.x > WIDTH - TILESIZE:
			#switchroom on levellist x axis (+1)
			#self.game.draw_map()
			self.game.current_room += 1
			self.nextRoom = True
			self.rect.x = 0
		elif self.rect.y < 0:
			#switchroom on levellist y axis (-1)
			#self.game.draw_map()
			self.game.current_room -= XMAPLENGTH
			self.nextRoom = True
			self.rect.y = HEIGHT - TILESIZE
		elif self.rect.y > HEIGHT - TILESIZE:
			#switchroom on levellist y axis (+1)
			#self.game.draw_map()
			self.game.current_room += XMAPLENGTH
			self.nextRoom = True

		if self.nextRoom == True:
			self.game.all_sprites.empty()
			self.game.background_sprites.empty()
			self.game.walls.empty()
			self.game.draw_map()
			self.nextRoom = False

		self.speed_x = 0
		self.speed_y = 0

class Mountain(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.walls
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		#once I get different mountains, change the random thingie to 1, #
		self.mountain_var = random.randint(1, 1)
		if self.mountain_var == 1:
			self.image = MOUNTAIN1

		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE

class Grass(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.background_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.grass_var = random.randint(1, 10)
		if self.grass_var == 1:
			self.image = GRASS1
		elif self.grass_var == 2:
			self.image = GRASS2
		elif self.grass_var >= 3:
			self.image = GRASS3
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
