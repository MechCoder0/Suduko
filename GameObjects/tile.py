from pygame import font
from pygame import Color
from pygame.locals import *
from .generic_sprite import GenericSprite

class Tile(GenericSprite):
    def __init__(self, location, text, can_edit=False, groups=None) -> None:
        self.size = (90, 90)
        super().__init__(location, self.size, groups=groups, color=(255,255,255))
        self.can_edit = can_edit
        self.font = font.SysFont("Arial", 50)
        self.text = text
        self.write_text()
        self.clicked = False

    def on_click(self):
        if not self.can_edit:
            return 
        
        self.image.fill(Color('dodgerblue2'))
        self.write_text()

    def write_text(self):
        self.textSurf = self.font.render(self.text, True, (0,0,0))
        self.W = self.textSurf.get_width()
        self.H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.size[0]/2 - self.W/2, self.size[1]/2 - self.H/2])

    def set_text(self, event):
        self.reset(False)
        self.text = event.unicode
        self.write_text()

    def reset(self, keep_number):
        self.image.fill((255,255,255))
        if keep_number:
            self.write_text()