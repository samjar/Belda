from pygame import image

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
WALKRATE = 8  # how many pixels to move while walking per frame
ANIMRATE = 0.15  # how many seconds each frame of player's walking animation lasts
HEROSPRITEDOWN = image.load("images/sprites/player/player_down1.png")
HEROSPRITEDOWN2 = image.load("images/sprites/player/player_down2.png")

HEROSPRITEUP = image.load("images/sprites/player/player_up1.png")
HEROSPRITEUP2 = image.load("images/sprites/player/player_up2.png")

HEROSPRITELEFT = image.load("images/sprites/player/player_left1.png")
HEROSPRITELEFT2 = image.load("images/sprites/player/player_left2.png")

HEROSPRITERIGHT = image.load("images/sprites/player/player_right1.png")
HEROSPRITERIGHT2 = image.load("images/sprites/player/player_right2.png")

HERODOWNLIST = [HEROSPRITEDOWN, HEROSPRITEDOWN2]
HEROUPLIST = [HEROSPRITEUP, HEROSPRITEUP2]
HEROLEFTLIST = [HEROSPRITELEFT, HEROSPRITELEFT2]
HERORIGHTLIST = [HEROSPRITERIGHT, HEROSPRITERIGHT2]

CURHEROSPRITE = HERODOWNLIST[0]

# PLAYERSPRITESHEET = image.load("player_sprite_sheet.png")

# map properties
XMAPLENGTH = 10

# tile properties
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# mountain tiles
MOUNTAIN1 = image.load("images/tiles/mountain1.png")
CAVEOPENING1 = image.load("images/tiles/caveopening1.png")

# water tiles
WATER1 = image.load("images/tiles/water1.png")

# grass/ground/walking tiles
GRASS1 = image.load("images/tiles/grass1.png")
GRASS2 = image.load("images/tiles/grass2.png")
GRASS3 = image.load("images/tiles/grass3.png")
GROUND1 = image.load("images/tiles/ground1.png")
START = image.load("images/tiles/start.png")

# tree tiles
TREE1 = image.load("images/tiles/tree1.png")

# objects
CHEST1 = image.load("images/tiles/chest1.png")

# background & pictures
MENUBACKGROUND = image.load("images/menubackground.png")

# items, icons and cursors
SWORDCURSOR = image.load("images/icons/sword_cursor.png")
