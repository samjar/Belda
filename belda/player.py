# Player class
import pygame
from pygame import sprite, Surface, transform, SRCALPHA
from pygame.sprite import Sprite

from settings import TILESIZE, WIDTH, HEIGHT, XMAPLENGTH, HEROSPRITEUP, HEROSPRITERIGHT, HEROSPRITELEFT, HEROSPRITEDOWN


class Player(Sprite):
    def __init__(self, game, x, y):
        # initialize the player's attributes
        self.groups = game.player_sprite
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = HEROSPRITEDOWN
        self.image = transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def collides(self, sprite_group):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            return False

        for s in sprite_group:
            if self.rect.colliderect(s.rect):
                return True

        return False

    def try_move(self, x, y):
        if x != 0:
            self.rect.x += x
            if self.collides(self.game.current_room.wall_group):
                self.rect.x -= x
                return False

        if y != 0:
            self.rect.y += y
            if self.collides(self.game.current_room.wall_group):
                self.rect.y -= y
                return False

        return True

    def update(self):
        # update player movement
        self.try_move(self.speed_x, 0)
        self.try_move(0, self.speed_y)

        if self.rect.x < 0:
            # switchroom on levellist x axis (-1)
            # self.game.draw_map()
            self.game.set_room(self.game.current_room_index - 1)
            self.rect.x = WIDTH - TILESIZE
        elif self.rect.x > WIDTH - TILESIZE:
            # switchroom on levellist x axis (+1)
            # self.game.draw_map()
            self.game.set_room(self.game.current_room_index + 1)
            self.rect.x = 0
        elif self.rect.y < 0:
            # switchroom on levellist y axis (-1)
            # self.game.draw_map()
            self.game.set_room(self.game.current_room_index - XMAPLENGTH)
            self.rect.y = HEIGHT - TILESIZE
        elif self.rect.y > HEIGHT - TILESIZE:
            # switchroom on levellist y axis (+1)
            # self.game.draw_map()
            self.game.set_room(self.game.current_room_index + XMAPLENGTH)
            self.rect.y = 0

        # determine sprite direction based on our current speed_x/y
        if self.speed_x > 0:
            self.image = HEROSPRITERIGHT
        elif self.speed_x < 0:
            self.image = HEROSPRITELEFT
        elif self.speed_y > 0:
            self.image = HEROSPRITEDOWN
        elif self.speed_y < 0:
            self.image = HEROSPRITEUP

