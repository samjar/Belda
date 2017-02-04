import logging
import os
import sys

import pygame
from pygame import mixer, display

from beldarooms import room_list
from mainmenu import MainMenu
from player import Player
from room import Room
from settings import (WIDTH, HEIGHT, TITLE, HEROSPRITEDOWN, FPS, WALKRATE,
                      BLACK)

log = logging.Logger(__name__)

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
        self.running = True
        pygame.key.set_repeat(1, 150)
        self.walls = None
        self.background_sprites = None
        self.player_sprite = None
        self.room = None
        self.running = False
        self.player = None
        self.current_room = None
        self.current_room_index = 0
        self.current_room_initialized = False
        self.rooms = {}

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
        self.player_sprite = pygame.sprite.Group()
        self.run()

    def set_room(self, room_index):
        # this access with raise IndexError if the room doesn't exist
        room_list[room_index]
        self.current_room_index = room_index
        self.current_room_initialized = False

    def init_map(self):
        if self.current_room_initialized:
            # the current room is already initialized
            return

        if self.current_room_index in self.rooms:
            # room was loaded previously, reuse it
            self.current_room = self.rooms[self.current_room_index]
            return

        # load the room
        self.current_room = Room(room_list[self.current_room_index])
        pp = self.current_room.get_player_position()
        if pp is not None and self.player is None:
            self.player = Player(self, pp[0], pp[1])
            self.player_sprite.add(self.player)

        self.rooms[self.current_room_index] = self.current_room
        self.current_room_initialized = True

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
        self.init_map()
        self.current_room.update()
        self.player_sprite.update()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        self.current_room.draw(self.screen)
        self.player_sprite.draw(self.screen)

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
