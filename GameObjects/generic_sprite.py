import pygame

class GenericSprite(pygame.sprite.Sprite):

    def __init__(self, location, size, path=None, groups=None, color=None, text=None) -> None:
        super().__init__()
        self.size = size
        self.surf = pygame.Surface(size)
        self.color = color
        if path:
            image = pygame.image.load(path)
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = self.surf
            self.image.fill(color)

        if text is not None:
            self.font = pygame.font.SysFont("Arial", size[1])
            self.text = text
            self.write_text()

        self.rect = self.surf.get_rect(center=location)

        if groups:
            for g in groups:
                g.add(self)

    def write_text(self):
        self.textSurf = self.font.render(self.text, True, (0,0,0))
        self.W = self.textSurf.get_width()
        self.H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.size[0]/2 - self.W/2, self.size[1]/2 - self.H/2])