import pygame
from Util.util import Util

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

        #Board is 300 x 300 px
        top_left = (50, 50)
        bottom_right = (950, 950)
        distance_between = 100

        self.draw_square(top_left, bottom_right)
        self.draw_vertical_soduko(top_left[1], bottom_right[1], distance_between, top_left[0])
        self.draw_horizontal_soduko(top_left[0], bottom_right[0], distance_between, top_left[1])
        

    def draw_horizontal_soduko(self, start, end, dist, start_y):
        for x in range(9):
            if x % 3 == 0:
                pygame.draw.line(self.surface, self.BLACK, (start, (dist * x) + start_y), 
                             (end, dist * x + start_y), 15)
            else:
                pygame.draw.line(self.surface, self.BLACK, (start, (dist * x) + start_y), 
                             (end, dist * x + start_y), 5)

    def draw_vertical_soduko(self, start, end, dist, start_x):
        for x in range(9):
            if x % 3 == 0:
                pygame.draw.line(self.surface, self.BLACK, ((dist * x) + start_x, start), 
                             (dist * x + start_x, end), 15)
            else:
                pygame.draw.line(self.surface, self.BLACK, ((dist * x) + start_x, start), 
                             (dist * x + start_x, end), 5)


    def draw_square(self, top_left, bottom_right):
        top = top_left[1]
        left = top_left[0]
        bottom = bottom_right[1]
        right = bottom_right[0]
        top_left = (left,top)
        top_right = (right, top)
        bottom_left = (left, bottom)
        bottom_right = (right, bottom)
        pygame.draw.line(self.surface, self.BLACK, top_left, top_right, 15)
        pygame.draw.line(self.surface, self.BLACK, top_left, bottom_left, 15)
        pygame.draw.line(self.surface, self.BLACK, bottom_left, bottom_right, 15)
        pygame.draw.line(self.surface, self.BLACK, bottom_right, top_right, 15)
