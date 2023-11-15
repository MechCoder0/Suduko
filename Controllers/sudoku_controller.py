from .base_controller import Controller
from pygame.locals import *
from pygame.mouse import get_pos

class SodukoController(Controller):
    def __init__(self, game_state) -> None:
        self.game_state = game_state
        self.chosen_game = 0
        self.clicked_sprites = []
        self.actions = {
            QUIT: self.quit,
            KEYDOWN: {
                K_ESCAPE: self.quit,
                K_s: game_state.solve,
                K_BACKSPACE: self.reset_sprite,
                K_1: self.set_text,
                K_2: self.set_text,
                K_3: self.set_text, 
                K_4: self.set_text, 
                K_5: self.set_text,
                K_6: self.set_text,
                K_7: self.set_text,
                K_8: self.set_text,
                K_9: self.set_text
            },
            MOUSEBUTTONUP:self.mouse_up,
            MOUSEBUTTONDOWN:self.mouse_down
        }

    def run_action(self, approved_actions=[]):
        # all actions are always approved for this controller.
        approved_actions.extend([self.quit, self.game_state.solve, self.mouse_down, self.mouse_up, self.set_text, self.reset_sprite])
        super().run_action(approved_actions)
    
    def mouse_up(self):
        self.set_clicked(False, True)

    def mouse_down(self):
        self.reset_sprite(True)
        self.set_clicked(True, False)

    def set_clicked(self, clicked, run_function):
        pos = get_pos()

        for s in self.game_state.clickable:
            if s.rect.collidepoint(pos) and s.can_edit:
                s.clicked = clicked
                if clicked:
                    self.clicked_sprites.append(s)

                if run_function and hasattr(s, "on_click"):
                    s.on_click()

    def reset_sprite(self, keep_number=False):
        if len(self.clicked_sprites) > 0:
            self.clicked_sprites.pop().reset(keep_number)

    def set_text(self):
        length = len(self.clicked_sprites)
        if length > 0:
            sprite = self.clicked_sprites[length-1]
            if sprite.can_edit:
                sprite.set_text(self.event)