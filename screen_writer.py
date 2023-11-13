import pygame
from util import Util

class ScreenWriter:

    def __init__(self, surface, game_state) -> None:
        self.surface = surface
        self.screen_width = game_state.WIDTH
        self.screen_height = game_state.HEIGHT
        self.game_state = game_state

        #Colors
        self.GAME_BACKGROUND_COLOR = (0,50,125)
        self.SCREEN_BACKGROUND_COLOR = (74,101,134)
        self.GREEN = (0,0,255)
        self.RED = (255,0,0)
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

    def get_rendered_text(self, text):
        f = pygame.font.SysFont("Verdana", 20)
        return f.render(text, True, (123,255,0))

    def write_text(self, position, text, should_center_x=True, middle=-1):
        rendered_text = self.get_rendered_text(text)

        if should_center_x:
            if middle == -1:
                middle = self.screen_width/2
            text_rect = rendered_text.get_rect(center = (middle, position[1]))
        else:
            text_rect = rendered_text.get_rect(left = position[0], centery = position[1])
        self.surface.blit(rendered_text, text_rect)
        return text_rect

    def print_values(self, values, text, width, starting_height):
        for val in values:
            self.write_text((width, starting_height), text + str(val))
            starting_height += 30

    def print_start_screen(self):
        self.surface.fill(self.SCREEN_BACKGROUND_COLOR)
        self.write_text((0, self.screen_height/4), "Sudoku")
        self.write_text((0, self.screen_height/2), "Press Enter to start!")
        self.write_text((0, self.screen_height * .75), "Begin!", True, Util.get_middle(0, self.screen_width))


    def print_sudoku_board(self):
        self.surface.fill(self.WHITE)
        pygame.draw.line(self.surface, self.BLACK, (100, 100), (700, 500), 5)