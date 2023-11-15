from pygame import font
from pygame import Color
from .generic_sprite import GenericSprite

class Tile(GenericSprite):
    def __init__(self, location, text, can_edit=False, groups=None) -> None:
        size = (90, 90)
        super().__init__(location, size, groups=groups, color=(255,255,255))
        self.can_edit = can_edit
        self.font = font.SysFont("Arial", 50)
        self.textSurf = self.font.render(text, 1, (0,0,0))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [size[0]/2 - W/2, size[1]/2 - H/2])
        self.clicked = False

    def on_click(self):
        if self.can_edit:
            self.image.fill(Color('dodgerblue2'))

    def reset_color(self):
        self.image.fill((255,255,255))