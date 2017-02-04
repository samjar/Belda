from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, group, image):
        self.groups = group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
