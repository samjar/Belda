from beldarooms import *
from mainmenu import *
from player import *
from tiles import *

os.environ['SDL_VIDEO_CENTERED'] = '1'


class Game:
    def __init__(self):
        # initialize the program - not the game
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.music.load("Come_and_Find_Me.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(1)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.key.set_repeat(1, 150)
        self.cur_hero_img = HEROSPRITEDOWN
        self.beldaRooms = BeldaRoomClass()
        self.current_room = self.beldaRooms.current_room

    def quit(self):
        pygame.quit()
        sys.exit()

    def load_game(self):
        pass

    def new(self):
        # Initialize the Game
        pygame.key.set_repeat(1, 10)
        pygame.mixer.music.stop()
        pygame.mixer
        self.walls = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.alreadySpawned = False
        self.draw_map()
        self.run()
        # self.current_room = 0

    def draw_map(self):

        x = y = 0

        self.room = self.beldaRooms.room_list[self.current_room]

        # draw the map from map.txt
        for row in self.room:
            for col in row:
                if col == '.':
                    Tile(self, x, y, self.background_sprites, GRASS3)
                if col == "'":
                    Tile(self, x, y, self.background_sprites, GRASS1)
                if col == ';':
                    Tile(self, x, y, self.background_sprites, GRASS2)
                if col == ',':
                    Tile(self, x, y, self.background_sprites, GROUND1)
                if col == '1':
                    Tile(self, x, y, self.walls, MOUNTAIN1)
                if col == 't':
                    Tile(self, x, y, self.walls, TREE1)
                if col == 'C':
                    Tile(self, x, y, self.background_sprites, CAVEOPENING1)
                if col == 'c':
                    Tile(self, x, y, self.walls, CHEST1)
                if col == 'w':
                    Tile(self, x, y, self.walls, WATER1)
                if col == 'S':
                    if self.alreadySpawned is False:
                        self.player = Player(self, x, y)
                        self.player_sprite.add(self.player)
                        self.alreadySpawned = True
                    Tile(self, x, y, self.background_sprites, START)
                x += 1
            y += 1
            x = 0

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.move(-WALKRATE, 0)
                    self.cur_hero_img = HEROSPRITELEFT
                if event.key == pygame.K_RIGHT:
                    self.player.move(WALKRATE, 0)
                    self.cur_hero_img = HEROSPRITERIGHT
                if event.key == pygame.K_UP:
                    self.player.move(0, -WALKRATE)
                    self.cur_hero_img = HEROSPRITEUP
                if event.key == pygame.K_DOWN:
                    self.player.move(0, WALKRATE)
                    self.cur_hero_img = HEROSPRITEDOWN

    def update(self):
        # Game Loop - Update
        self.background_sprites.update()
        self.walls.update()
        self.player_sprite.update()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        self.background_sprites.draw(self.screen)
        self.walls.draw(self.screen)
        self.player_sprite.draw(self.screen)
        self.screen.blit(self.cur_hero_img,
                         (self.player.rect.x, self.player.rect.y))

        pygame.display.update()

    def start_screen(self):
        funcs = {'New Game': self.new,
                 'Load': self.load_game,
                 'Options': self.options,
                 'Quit': self.quit}
        mm = MainMenu(self.screen, funcs.keys(), funcs)
        mm.menu_run()

    def game_over_screen(self):
        pass

    def options(self):
        pass


g = Game()

while g.running:
    g.start_screen()
    g.game_over_screen()

# after Game Over screen, it goes back to start_screen
# (unless running = False)
