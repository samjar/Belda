from belda.belda import Game
import logging
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)
log = logging.getLogger(__name__)

if __name__ == '__main__':
    log.info("Initialized")
    game = Game()
    game.start_screen()