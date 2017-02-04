# Player class
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # initialize the player's attributes
        self.groups = game.player_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
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
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            print("Clipmode activated!")
        if not key[pygame.K_w]:
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
            # switchroom on levellist x axis (-1)
            # self.game.draw_map()
            self.game.current_room -= 1
            self.nextRoom = True
            self.rect.x = WIDTH - TILESIZE
        elif self.rect.x > WIDTH - TILESIZE:
            # switchroom on levellist x axis (+1)
            # self.game.draw_map()
            self.game.current_room += 1
            self.nextRoom = True
            self.rect.x = 0
        elif self.rect.y < 0:
            # switchroom on levellist y axis (-1)
            # self.game.draw_map()
            self.game.current_room -= XMAPLENGTH
            self.nextRoom = True
            self.rect.y = HEIGHT - TILESIZE
        elif self.rect.y > HEIGHT - TILESIZE:
            # switchroom on levellist y axis (+1)
            # self.game.draw_map()
            self.game.current_room += XMAPLENGTH
            self.nextRoom = True
            self.rect.y = 0
        if self.nextRoom:
            self.game.background_sprites.empty()
            self.game.walls.empty()
            self.game.draw_map()
            self.nextRoom = False

        self.speed_x = 0
        self.speed_y = 0
