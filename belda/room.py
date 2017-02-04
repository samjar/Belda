from settings import (GRASS1, GRASS2, GRASS3, GROUND1, MOUNTAIN1, TREE1,
                      CAVEOPENING1, CHEST1, WATER1, START)
from tiles import Tile
from pygame.sprite import Group


class Room(object):
    def __init__(self, room_data):
        self.tiles = None
        self.player_position = None
        self.background_group = Group()
        self.wall_group = Group()

        self.parse_map(room_data)

    def get_player_position(self):
        return self.player_position

    def parse_map(self, room_data):
        x = y = 0

        self.tiles = []
        for index, row in enumerate(room_data):
            self.tiles.append([])
            for col in row:
                if col == '.':
                    tile = Tile(x, y, self.background_group, GRASS3)
                elif col == "'":
                    tile = Tile(x, y, self.background_group, GRASS1)
                elif col == ';':
                    tile = Tile(x, y, self.background_group, GRASS2)
                elif col == ',':
                    tile = Tile(x, y, self.background_group, GROUND1)
                elif col == '1':
                    tile = Tile(x, y, self.wall_group, MOUNTAIN1)
                elif col == 't':
                    tile = Tile(x, y, self.wall_group, TREE1)
                elif col == 'C':
                    tile = Tile(x, y, self.background_group, CAVEOPENING1)
                elif col == 'c':
                    tile = Tile(x, y, self.wall_group, CHEST1)
                elif col == 'w':
                    tile = Tile(x, y, self.wall_group, WATER1)
                elif col == 'S':
                    self.player_position = (x, y)
                    tile = Tile(x, y, self.background_group, START)
                else:
                    raise RuntimeError(
                        "Unexpected token in map: [{}]".format(col))

                self.tiles[index].append(tile)

                x += 1

            y += 1
            x = 0

    def update(self):
        self.background_group.update()
        self.wall_group.update()

    def draw(self, screen):
        self.background_group.draw(screen)
        self.wall_group.draw(screen)
