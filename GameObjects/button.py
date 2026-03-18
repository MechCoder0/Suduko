import pygame
from .generic_sprite import GenericSprite

class Button(GenericSprite):
    BACKGROUND = (30, 90, 180)
    BORDER = (20, 60, 130)
    HOVER = (50, 120, 220)
    TEXT_COLOR = (255, 255, 255)
    RADIUS = 10

    def __init__(self, size, center, on_click, text, color=None, groups=None):
        super().__init__(center, size, groups=groups, color=self.BACKGROUND, text=text)
        self.clicked = False
        self.on_click = on_click
        self._draw(self.BACKGROUND)

    def _draw(self, bg_color):
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.BORDER, (0, 0, *self.size), border_radius=self.RADIUS)
        pygame.draw.rect(self.image, bg_color, (2, 2, self.size[0]-4, self.size[1]-4), border_radius=self.RADIUS)
        font = pygame.font.SysFont("Arial", round(self.size[1] * 0.5), bold=True)
        text_surf = font.render(self.text, True, self.TEXT_COLOR)
        self.image.blit(text_surf, (self.size[0]/2 - text_surf.get_width()/2,
                                    self.size[1]/2 - text_surf.get_height()/2))

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        color = self.HOVER if self.rect.collidepoint(mouse_pos) else self.BACKGROUND
        self._draw(color)