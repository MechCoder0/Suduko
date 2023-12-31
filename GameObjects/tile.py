from pygame import Color
from pygame.locals import *
from .generic_sprite import GenericSprite

class Tile(GenericSprite):
    def __init__(self, location, text, value, can_edit=False, groups=None, size=(90,90)) -> None:
        self.size = size
        color = (255,255,255)
        if can_edit:
            color = (255, 200, 200)
        super().__init__(location, self.size, groups=groups, color=color, text=text)
        self.can_edit = can_edit
        self.clicked = False
        self.value = value

    def on_click(self):
        if not self.can_edit:
            return 
        
        self.image.fill(Color('dodgerblue2'))
        self.write_text()

    def set_text(self, event):
        self.reset(False)
        self.text = event.unicode
        self.value = self.text
        self.write_text()

    def reset(self, keep_number):
        self.image.fill(self.color)
        if keep_number:
            self.write_text()
        else:
            self.text = ""
            self.value = 0