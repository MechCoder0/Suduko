from pygame import font
from .generic_sprite import GenericSprite

class Tile(GenericSprite):
    def __init__(self, location, text, groups=None) -> None:
        size = (90, 90)
        super().__init__(location, size, groups=groups, color=(255,255,255))
        self.font = font.SysFont("Arial", 50)
        self.textSurf = self.font.render(text, 1, (0,0,0))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [size[0]/2 - W/2, size[1]/2 - H/2])