import pygame
import sys
from GameDataInterfaces.game_data_accessor import GameDataAccessor
from screen_writer import ScreenWriter

class BaseScreen():
    def __init__(self, controller) -> None:
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Sudoku")
        icon = pygame.image.load('Assets/Icon.png')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.gda = GameDataAccessor("GameData/data.json")
        game_data = self.gda.get_game_data()
        self.game_data = game_data
        self.HEIGHT = game_data["height"]
        self.WIDTH = game_data["width"]
        self.FPS = game_data["fps"]
        self.displaysurface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen_writer = ScreenWriter(self.displaysurface, self)
        self.controller = controller(self)
        self.keep_playing = True
        self.all_sprites = pygame.sprite.Group()


    def start_game(self, screen, screen_params=None):
        self.keep_playing = True
        while self.keep_playing:
            if screen_params:
                screen(screen_params)
            else:
                screen()
            events = pygame.event.get()
            self.controller.run_action(events)
            self.all_sprites.draw(self.displaysurface)
            
            pygame.display.update()
            self.clock.tick(self.FPS)

    def quit(self):
        print("Quitting the game.")
        pygame.quit()
        sys.exit()

    def return_to_start_screen(self):
        print("Returning to Start")
        self.keep_playing = False