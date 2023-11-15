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
        if not self.can_edit:
            return 
        
        self.image.fill(Color('dodgerblue2'))

        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_RETURN:
        #         self.text = ''
        #     elif event.key == pg.K_BACKSPACE:
        #         self.text = self.text[:-1]
        #     else:
        #         self.text += event.unicode
        #     # Re-render the text.
        #     self.textSurf = FONT.render(self.text, True, self.color)


    def reset(self):
        self.image.fill((255,255,255))
