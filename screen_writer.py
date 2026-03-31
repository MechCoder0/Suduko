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
        w = self.game_state.WIDTH
        h = self.game_state.HEIGHT
        self.write_text((0, h / 4), "Sudoku", middle=w / 2)
        self.write_text((0, h / 2), "Press Enter to start!", middle=w / 2)
        self.write_text((0, h * .75), "Begin!", True, Util.get_middle(0, w))
        self.write_text((0, h * .85), "Level Select", True, Util.get_middle(0, w))

    def print_level_select(self):
        self.surface.fill(self.SCREEN_BACKGROUND_COLOR)
        w = self.game_state.WIDTH
        h = self.game_state.HEIGHT
        self.write_text((0, h / 4), "Select Difficulty", middle=w / 2)

    def print_sudoku_board(self):
        self.surface.fill(self.WHITE)

        board_size = min(self.game_state.WIDTH, self.game_state.HEIGHT) * 0.8
        left = (self.game_state.WIDTH - board_size) / 2
        top = (self.game_state.HEIGHT - board_size) / 2
        top_left = (left, top)
        bottom_right = (left + board_size, top + board_size)
        distance_between = board_size / 9

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
        width = 15
        half = width // 2
        top = top_left[1]
        left = top_left[0]
        bottom = bottom_right[1]
        right = bottom_right[0]
        pygame.draw.line(self.surface, self.BLACK, (left - half, top), (right + half, top), width)
        pygame.draw.line(self.surface, self.BLACK, (left, top - half), (left, bottom + half), width)
        pygame.draw.line(self.surface, self.BLACK, (left - half, bottom), (right + half, bottom), width)
        pygame.draw.line(self.surface, self.BLACK, (right, top - half), (right, bottom + half), width)
