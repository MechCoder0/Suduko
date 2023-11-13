import pygame

class GenericSprite(pygame.sprite.Sprite):

    def __init__(self, location, size, path=None, groups=None, color=None) -> None:
        super().__init__()
        self.surf = pygame.Surface(size)
        if path:
            image = pygame.image.load(path)
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = self.surf
            self.image.fill(color)
        self.rect = self.surf.get_rect(center=location)

        if groups:
            for g in groups:
                g.add(self)