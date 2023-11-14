from .base_controller import Controller
from pygame.locals import *

class SodukoController(Controller):
    def __init__(self, game_state) -> None:
        self.game_state = game_state
        self.chosen_game = 0
        self.actions = {
            QUIT: game_state.quit,
            KEYDOWN: {
                K_ESCAPE: game_state.quit,
                K_s: game_state.solve
            }
        }

    def run_action(self, events, approved_actions=[]):
        # all actions are always approved for this controller.
        approved_actions.extend([self.game_state.quit, self.game_state.solve])
        return super().run_action(events, approved_actions)