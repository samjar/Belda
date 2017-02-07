from pygame import transform
from pygame.sprite import Sprite

from settings import TILESIZE


class Tile(Sprite):
    def __init__(self, x, y, group, image):
        Sprite.__init__(self, group)
        self.image = image
        self.image = transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
