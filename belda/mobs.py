# Mob class
from pygame import Surface, SRCALPHA, transform, sprite
from pygame.sprite import Sprite

from settings import TILESIZE


class Mob(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.mob_sprites
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = Surface((16, 16), SRCALPHA)
        self.image = transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def move(self, movex, movey):
        self.speed_x = movex
        self.speed_y = movey

    def collision_with_walls(self):
        for wall in self.game.walls:
            if sprite.collide_rect(self.game.mob, wall):
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

        self.rect.x = self.speed_x
        self.rect.y = self.speed_y

        self.collision_with_walls()

        self.speed_x = 0
        self.speed_y = 0
