import pygame
import os
import sys
import time
from settings import *

class MenuItem(pygame.font.Font):
	def __init__(self, text, font=None, font_size=50, font_color=WHITE, (pos_x, pos_y)=(0, 0)):

		pygame.font.Font.__init__(self, font, font_size)
		self.text = text
		self.font_size = font_size
		self.font_color = font_color
		self.label = self.render(self.text, 1, self.font_color)
		self.width = self.label.get_rect().width
		self.height = self.label.get_rect().height
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.position = pos_x, pos_y

	def is_mouse_selection(self, (posx, posy)):
		if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
			(posy >= self.pos_y and posy <= self.pos_y + self.height):
				return True
		return False

	def set_position(self, x, y):
		self.position = (x, y)
		self.pos_x = x
		self.pos_y = y

	def set_font_color(self, color):
		self.font_color = color
		self.label = self.render(self.text, 1, self.font_color)


class MainMenu():
	def __init__(self, screen, items, funcs, bg_color=BLACK, font=None, font_size=50,
				 font_color=WHITE):
		self.screen = screen
		self.screen_width = self.screen.get_rect().width
		self.screen_height = self.screen.get_rect().height

		self.bg_color = bg_color
		self.clock = pygame.time.Clock()

		self.funcs = funcs
		self.items = []
		for index, item in enumerate(items):
			menu_item = MenuItem(item, font, font_size, font_color)

			t_h = len(items) * menu_item.height
			pos_x = (self.screen_width / 2) - (menu_item.width / 2)
			pos_y = (self.screen_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)

			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)

		self.mouse_is_visible = True
		self.cur_item = None

	def set_mouse_visibility(self):
		if self.mouse_is_visible == True:
			pygame.mouse.set_visible(True)
		else:
			pygame.mouse.set_visible(False)

	def set_keyboard_selection(self, key):
		for item in self.items:
			item.set_italic(False)
			item.set_font_color(WHITE)

		if self.cur_item is None:
			self.cur_item = 0
		else:
			# Find the chosen item
			if key == pygame.K_UP and \
					self.cur_item > 0:
				self.cur_item -= 1
			elif key == pygame.K_UP and \
					self.cur_item == 0:
				self.cur_item = len(self.items) - 1
			elif key == pygame.K_DOWN and \
					self.cur_item < len(self.items) - 1:
				self.cur_item += 1
			elif key == pygame.K_DOWN and \
					self.cur_item == len(self.items) - 1:
				self.cur_item = 0

		self.items[self.cur_item].set_italic(True)
		self.items[self.cur_item].set_font_color(RED)

		if key == pygame.K_SPACE or key == pygame.K_RETURN:
			text = self.items[self.cur_item].text
			self.funcs[text]()

	def set_mouse_selection(self, item, mpos):
		if item.is_mouse_selection(mpos):
			item.set_italic(True)
			item.set_font_color(RED)
		else:
			item.set_italic(False)
			item.set_font_color(WHITE)

	def create_frame(self):
		pygame.draw.line(self.screen, WHITE, (200, 200), (815, 200))

	def menu_run(self):
		running = True
		while running:
			self.clock.tick(30)
			mpos = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					sys.exit()
				if event.type == pygame.KEYDOWN:
					self.mouse_is_visible = False
					self.set_keyboard_selection(event.key)
				if event.type == pygame.MOUSEBUTTONDOWN:
					for item in self.items:
						if item.is_mouse_selection(mpos):
							self.funcs[item.text]()

			if pygame.mouse.get_rel() != (0, 0):
				self.mouse_is_visible = True
				self.cur_item = None

			self.set_mouse_visibility()

			self.screen.fill(self.bg_color)
			self.create_frame()

			for item in self.items:
				if self.mouse_is_visible:
					self.set_mouse_selection(item, mpos)
				self.screen.blit(item.label, item.position)

			pygame.display.flip()

if (__name__ == "__main__"):

	def new():
		pass

	def load_game():
		pass

	def testing():
		pass

	def quit():
		sys.exit()

	os.environ['SDL_VIDEO_CENTERED'] = '1'
		
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption(TITLE)

	funcs = {'New Game': new,
			 'Load Game': load_game,
			 'Quit': quit}
	mm = MainMenu(screen, funcs.keys(), funcs)
	mm.menu_run() 
