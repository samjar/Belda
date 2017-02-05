import logging
import os
import sys

import pygame
import pytmx
from pygame import mixer, display

from mainmenu import MainMenu
from player import Player
from settings import (WIDTH, HEIGHT, TITLE, HEROSPRITEDOWN, FPS, WALKRATE,
                      BLACK)
from map import BeldaMap

log = logging.getLogger(__name__)

os.environ['SDL_VIDEO_CENTERED'] = '1'


class Game:
    def __init__(self):
        # initialize the program - not the game
        pygame.init()
        mixer.pre_init(44100, -16, 1, 512)
        mixer.music.load("sound/Come_and_Find_Me.ogg")
        mixer.music.set_volume(0.5)
        mixer.music.play(1)
        self.screen = display.set_mode((WIDTH, HEIGHT))
        display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 150)
        self.walls = None
        self.player_group = None
        self.running = False
        self.player = None
        self.current_room = (0, 0)
        self.map = None

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()

    def load_game(self):
        pass

    def new(self):
        # Initialize the Game
        pygame.key.set_repeat(1, 10)
        pygame.mixer.music.stop()
        self.player_group = pygame.sprite.Group()
        self.map = BeldaMap("map/belda.tmx")
        self.run()

    def advance_room_horizontally(self, left):
        if left:
            self.current_room = (self.current_room[0] - 1, self.current_room[1])
        else:
            self.current_room = (self.current_room[0] + 1, self.current_room[1])

    def advance_room_vertically(self, up):
        if up:
            self.current_room = (self.current_room[0], self.current_room[1] - 1)
        else:
            self.current_room = (self.current_room[0], self.current_room[1] + 1)

    def init_map(self):
        world_pos = self.map.get_player_position()
        room_pos = self.map.get_player_room_position()
        self.player = Player(self, room_pos[0], room_pos[1])
        self.player_group.add(self.player)
        self.current_room = self.map.get_room(*world_pos)
        pass

    def run(self):
        # Game Loop
        self.running = True
        self.init_map()
        while self.running:
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
                    # self.running = False
                    # while testing, since it exits faster
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.speed_x = -WALKRATE
                if event.key == pygame.K_RIGHT:
                    self.player.speed_x = WALKRATE
                if event.key == pygame.K_UP:
                    self.player.speed_y = -WALKRATE
                if event.key == pygame.K_DOWN:
                    self.player.speed_y = WALKRATE
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.speed_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player.speed_y = 0

    def update(self):
        # Game Loop - Update
        self.player_group.update()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        # TODO draw map
        self.map.draw(self.screen, self.current_room)
        self.player_group.draw(self.screen)

        pygame.display.update()

    def start_screen(self):
        funcs = {'New Game': self.new,
                 'Load': self.load_game,
                 'Options': self.options,
                 'Quit': self.quit}
        mm = MainMenu(self.screen, funcs.keys(), funcs)
        mm.menu_run()

    def game_over_screen(self):
        pass

    def options(self):
        pass
