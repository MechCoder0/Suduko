from .generic_sprite import GenericSprite

class Button(GenericSprite):
    def __init__(self, size, center, onclick, text, color=(255,0,0), groups=None):
        super().__init__(center, size, groups=groups, color=color, text=text)
        self.clicked = False
        self.on_click = onclick
        