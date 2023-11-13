from pygame.locals import *
from .base_controller import Controller
from util import Util

class StartScreenController(Controller):
    def __init__(self, game_state) -> None:
        self.game_state = game_state
        self.chosen_game = 0
        self.actions = {
            QUIT: game_state.quit,
            KEYDOWN: {
                K_ESCAPE: game_state.quit,
                K_RETURN: self.start_chosen_game
            }
        }

    def run_action(self, events, approved_actions=[]):
        # all actions are always approved for this controller.
        approved_actions.extend([self.game_state.quit, self.start_chosen_game])
        return super().run_action(events, approved_actions)

    def start_chosen_game(self):
        self.game_state.selections[self.chosen_game][0]().start_game()
        # if the game loop ends, return to start screen
        self.game_state.start_game()