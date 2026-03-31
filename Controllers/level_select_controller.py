from .base_controller import Controller
from pygame.locals import *
from pygame.mouse import get_pos
from pygame.display import set_mode
from pygame import RESIZABLE

class LevelSelectController(Controller):
    def __init__(self, game_state) -> None:
        self.game_state = game_state
        self.actions = {
            QUIT: self.quit,
            KEYDOWN: {
                K_ESCAPE: self.quit
            },
            MOUSEBUTTONUP: self.mouse_up,
            MOUSEBUTTONDOWN: self.mouse_down,
            VIDEORESIZE: self.resize
        }

    def run_action(self, approved_actions=[]):
        approved_actions.extend([self.quit, self.mouse_down, self.mouse_up, self.resize])
        super().run_action(approved_actions)

    def mouse_up(self):
        self.set_clicked(False, True)

    def mouse_down(self):
        self.set_clicked(True, False)

    def set_clicked(self, clicked, run_function):
        pos = get_pos()
        for s in self.game_state.clickable:
            if s.rect.collidepoint(pos):
                s.clicked = clicked
                if run_function and hasattr(s, "on_click"):
                    s.on_click()

    def resize(self):
        self.game_state.WIDTH = self.event.w
        self.game_state.HEIGHT = self.event.h
        self.game_state.displaysurface = set_mode((self.event.w, self.event.h), RESIZABLE)
        self.game_state.screen_writer.surface = self.game_state.displaysurface
        self.game_state.rebuild()