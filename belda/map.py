import pygame
from pytmx.util_pygame import load_pygame
from settings import TILESIZE


class BeldaMap(object):
    def __init__(self, filename):
        self.map = load_pygame(filename)
        self.tilesets = {}
        self.tiles = {}
        self.room_width = 16
        self.room_height = 11
        self.layer_name_to_index = {}

        tmx_player_start = self.map.get_object_by_name("player_start")
        self.player_position = (int(tmx_player_start.x / self.map.tilewidth),
                                int(tmx_player_start.y / self.map.tileheight))
        self.rect = pygame.sprite.Rect(0, 0, TILESIZE, TILESIZE)

        self.collidable = {}
        for key, tile_props in self.map.tile_properties.iteritems():
            collidable = tile_props.get('collidable', False)
            self.collidable[key] = bool(collidable)

        for index, layer in enumerate(self.map.layers):
            self.layer_name_to_index[layer.name] = index

        self.walls_for_room = None

    def get_player_position(self):
        return self.player_position

    def get_player_room_position(self):
        return (self.player_position[0] % self.room_width,
                self.player_position[1] % self.room_height)

    def get_room(self, x, y):
        """
        Returns the room corresponding to the tile coordinates.
        """
        return x / self.room_width, y / self.room_height

    def get_walls(self, room):
        if self.walls_for_room is not None:
            if self.walls_for_room[0] == room:
                return self.walls_for_room[1]

        self.walls_for_room = (room, self._determine_walls(room))
        return self.walls_for_room[1]

    def _determine_walls(self, room):
        room_x_offset = room[0] * self.room_width
        room_y_offset = room[1] * self.room_height
        layer = self.layer_name_to_index['Background']

        walls = []
        for x in range(0, self.room_width):
            for y in range(0, self.room_height):
                tile_x = x + room_x_offset
                tile_y = y + room_y_offset

                tile_gid = self.map.get_tile_gid(tile_x, tile_y, layer)
                if not self.collidable[tile_gid]:
                    continue

                rect = pygame.sprite.Rect(x * TILESIZE,
                                          y * TILESIZE,
                                          TILESIZE,
                                          TILESIZE)
                wall = Wall(rect)
                walls.append(wall)
        return walls

    def draw(self, screen, room):
        # constants
        layer = self.layer_name_to_index['Background']

        room_x_offset = room[0] * self.room_width
        room_y_offset = room[1] * self.room_height

        for x in range(0, self.room_width):
            for y in range(0, self.room_height):
                tile_x = x + room_x_offset
                tile_y = y + room_y_offset

                image = self.map.get_tile_image(tile_x, tile_y, layer)
                self.rect.x = x * self.rect.w
                self.rect.y = y * self.rect.h
                screen.blit(
                    pygame.transform.scale(image, (TILESIZE, TILESIZE)),
                    self.rect)


class Wall(object):
    def __init__(self, rect):
        self.rect = rect
