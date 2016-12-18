import pygame

# game options/settings
TITLE = "The Adventure of Belda"
WIDTH = 1024
HEIGHT = 704
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GREY = (170, 170, 170)

# player properties
WALKRATE = 5 # how many pixels to move while walking per frame
ANIMRATE = 0.15 # how many seconds each frame of player's walking animation lasts
HEROSPRITEDOWN = pygame.image.load("player_down.png")
HEROSPRITEUP = pygame.image.load("player_up.png") 
HEROSPRITELEFT = pygame.image.load("player_left.png")
HEROSPRITERIGHT = pygame.image.load("player_right.png")
CURHEROSPRITE = HEROSPRITEDOWN
#PLAYERSPRITESHEET = pygame.image.load("player_sprite_sheet.png")

# map properties
XMAPLENGTH = 10

# tile properties
TILESIZE = 32 
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# mountain tiles
MOUNTAIN1 = pygame.image.load("mountain1.png")
MOUNTAIN2 = pygame.image.load("mountain2.png")
MOUNTAIN3 = pygame.image.load("mountain3.png")
MOUNTAIN4 = pygame.image.load("mountain4.png")

# grass tiles
GRASS1 = pygame.image.load("grass1.png")
GRASS2 = pygame.image.load("grass2.png")
GRASS3 = pygame.image.load("grass3.png")
