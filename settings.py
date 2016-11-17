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
WALKRATE = 3 # how many pixels to move while walking per frame
ANIMRATE = 0.15 # how many seconds each frame of player's walking animation lasts
#HEROSPRITE = pygame.image.load("player.png")

"""
for animated movement (eventually)

down1 = pygame.image.load('player_down1.png')
down2 = pygame.image.load('player_down2.png')
up1   = pygame.image.load('player_up1.png')
up2   = pygame.image.load('player_up2.png')
left1 = pygame.image.load('player_left1.png')
left2 = pygame.image.load('player_left2.png')
"""

# tile properties
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

