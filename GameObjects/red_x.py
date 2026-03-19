import pygame

class RedX(pygame.sprite.Sprite):
    def __init__(self, width, height, groups=None):
        super().__init__()
        size = round(min(width, height) * 0.4)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.alpha = 255
        self.size = size
        self._draw()
        self.rect = self.image.get_rect(center=(width / 2, height / 2))
        if groups:
            for g in groups:
                g.add(self)

    def _draw(self):
        self.image.fill((0, 0, 0, 0))
        thickness = round(self.size * 0.15)
        color = (220, 30, 30, int(self.alpha))
        pygame.draw.line(self.image, color, (0, 0), (self.size, self.size), thickness)
        pygame.draw.line(self.image, color, (self.size, 0), (0, self.size), thickness)

    def update(self):
        self.alpha -= 3
        if self.alpha <= 0:
            self.kill()
            return
        self._draw()
