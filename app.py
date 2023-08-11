import pygame
import sys

pygame.init()
HEIGHT = 500
WIDTH = 500
FPS = 60
white = [255, 255, 255]
black = [0,0,0]

FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def draw_board():
    pygame.draw.line(displaysurface, black, (100, 100), (700, 500), 5)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill(white)
    draw_board()
    # pygame.display.update()
    # FramePerSec.tick(FPS)
    pygame.display.flip()