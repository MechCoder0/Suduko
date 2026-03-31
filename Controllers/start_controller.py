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
                K_RETURN: self.start_chosen_game,
                K_UP: self.move_up,
                K_DOWN: self.move_down
            },
            VIDEORESIZE: self.resize
        }

    def run_action(self, approved_actions=[]):
        approved_actions.extend([self.quit, self.start_chosen_game, self.resize, self.move_up, self.move_down])
        return super().run_action(approved_actions)

    def resize(self):
        self.game_state.WIDTH = self.event.w
        self.game_state.HEIGHT = self.event.h
        self.game_state.displaysurface = set_mode((self.event.w, self.event.h), RESIZABLE)
        self.game_state.screen_writer.surface = self.game_state.displaysurface
        self.game_state.rebuild()

    def start_chosen_game(self):
        self.game_state.selections[self.chosen_game][0].start_game()
        self.game_state.start_game()

    def move_up(self):
        if self.chosen_game > 0:
            self.chosen_game -= 1
            self.update_marker_pos()

    def move_down(self):
        if self.chosen_game < len(self.game_state.selections) - 1:
            self.chosen_game += 1
            self.update_marker_pos()

    def update_marker_pos(self):
        h = self.game_state.HEIGHT
        y_pos = h * (0.80 + (self.chosen_game * 0.10))
        self.game_state.marker.rect.centery = y_pos