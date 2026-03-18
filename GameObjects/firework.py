import pygame
import random
import math

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, groups=None):
        super().__init__()
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 8)
        self.vel_x = math.cos(angle) * speed
        self.vel_y = math.sin(angle) * speed
        self.alpha = 255
        self.color = color
        self.image = pygame.Surface((6, 6), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (*color, self.alpha), (3, 3), 3)
        self.rect = self.image.get_rect(center=(x, y))
        self.x = float(x)
        self.y = float(y)
        if groups:
            for g in groups:
                g.add(self)

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += 0.2
        self.alpha -= 6
        if self.alpha <= 0:
            self.kill()
            return
        self.image = pygame.Surface((6, 6), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (*self.color, int(self.alpha)), (3, 3), 3)
        self.rect.center = (round(self.x), round(self.y))


class Firework:
    COLORS = [(255,50,50), (50,255,50), (50,50,255), (255,255,50), (255,50,255), (50,255,255)]

    @staticmethod
    def launch(width, height, groups, count=6):
        for _ in range(count):
            x = random.randint(round(width * 0.2), round(width * 0.8))
            y = random.randint(round(height * 0.1), round(height * 0.6))
            color = random.choice(Firework.COLORS)
            for _ in range(40):
                Particle(x, y, color, groups)
