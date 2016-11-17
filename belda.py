import pygame
import random
import time
import sys
import os

from os import path
from sprites import *
from settings import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Game:
	def __init__(self):
		# initialize the program - not the game
		pygame.init()
		pygame.mixer.pre_init(44100, -16, 1, 512)
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.load_data()
		pygame.key.set_repeat(1, 10)

	def load_data(self):
		game_folder = path.dirname(__file__)
		self.map_data = []
		with open(path.join(game_folder, 'map.txt'), 'rt') as f:
			for line in f:
				self.map_data.append(line)

	def quit(self):
		pygame.quit()
		sys.exit()

	def new(self):
		# Initialize the Game
		self.all_sprites = pygame.sprite.Group()
		self.walls = pygame.sprite.Group()
		self.draw_map()
		self.run()

	def draw_map(self):
		# draw the map from map.txt
		for row, tiles in enumerate(self.map_data):
			for col, tile in enumerate(tiles):
				if tile == '1':
					Mountain(self, col, row)
				if tile == 'S':
					self.player = Player(self, col, row)

	def run(self):
		# Game Loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def events(self):
		# Game Loop - Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.quit()
				if event.key == pygame.K_LEFT:
					self.player.move(-WALKRATE, 0)
				elif event.key == pygame.K_RIGHT:
					self.player.move(WALKRATE, 0)
				elif event.key == pygame.K_UP:
					self.player.move(0, -WALKRATE)
				elif event.key == pygame.K_DOWN:
					self.player.move(0, WALKRATE)
				

	def update(self):
		# Game Loop - Update
		self.all_sprites.update()
		
	def draw(self):
		# Game Loop - Draw
		self.screen.fill(BLACK)
		#self.draw_grid()
		self.all_sprites.draw(self.screen)

		pygame.display.update()

	def draw_grid(self):
		# Grid for tile testing purposes (just temporary)
		for x in range(0, WIDTH, TILESIZE):
			pygame.draw.line(self.screen, GREY, (x, 0), (x, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(self.screen, GREY, (0, y), (WIDTH, y))

	def start_screen(self):
		pass

	def game_over_screen(self):
		pass


g = Game()

# start/menu screen for whenever we make one
g.start_screen()

# after start screen, goes into the while loop
while g.running:
	# starts a new game
	g.new()
	# goes to Game Over screen if playing = False
	g.game_over_screen()
	# after Game Over screen, it goes back to new (unless running = False)
