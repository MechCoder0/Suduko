from pygame.locals import *
from pygame.display import set_mode
from pygame import RESIZABLE
from .base_controller import Controller

class StartScreenController(Controller):
    def __init__(self, game_state) -> None:
        self.game_state = game_state
        self.chosen_game = 0
        self.actions = {
            QUIT: self.quit,
            KEYDOWN: {
                K_ESCAPE: self.quit,
                K_RETURN: self.start_chosen_game
            },
            VIDEORESIZE: self.resize
        }

    def run_action(self, approved_actions=[]):
        approved_actions.extend([self.quit, self.start_chosen_game, self.resize])
        return super().run_action(approved_actions)

    def resize(self):
        self.game_state.WIDTH = self.event.w
        self.game_state.HEIGHT = self.event.h
        self.game_state.displaysurface = set_mode((self.event.w, self.event.h), RESIZABLE)
        self.game_state.screen_writer.surface = self.game_state.displaysurface

    def start_chosen_game(self):
        self.game_state.selections[self.chosen_game][0].start_game()
        self.game_state.start_game()