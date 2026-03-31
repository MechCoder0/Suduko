from .base_screen import BaseScreen
from Controllers.sudoku_controller import SodukoController
from Util.sudoku_generator import Generator
from Util.sudoku_solver import SudokuSolver
from GameObjects.tile import Tile
from GameObjects.button import Button
from GameObjects.firework import Firework
from GameObjects.red_x import RedX

class SudokuEngine(BaseScreen):
    def __init__(self) -> None:
        super().__init__(SodukoController)
        self.generator = Generator()
        self.difficulty = "easy"
        self.puzzle = self.get_puzzle()
        self.clickable = []
        self.tiles = []

    def start_game(self):
        # Cleanup existing objects to prevent duplicates on restart
        for s in self.all_sprites:
            s.kill()
        self.clickable.clear()

        self.calculate_layout()
        self.add_numbers(self.top_left, self.distance_between, self.puzzle)
        self.add_buttons()
        super().start_game(self.screen_writer.print_sudoku_board)

    def calculate_layout(self):
        board_size = min(self.WIDTH, self.HEIGHT) * 0.8
        self.distance_between = board_size / 9
        left = (self.WIDTH - board_size) / 2
        top = (self.HEIGHT - board_size) / 2
        self.top_left = (round(left + self.distance_between / 2), round(top + self.distance_between / 2))

    def add_buttons(self):
        btn_w = round(self.WIDTH * 0.25)
        btn_h = round(self.HEIGHT * 0.05)
        board_size = min(self.WIDTH, self.HEIGHT) * 0.8
        board_bottom = (self.HEIGHT - board_size) / 2 + board_size
        btn_y = board_bottom + (self.HEIGHT - board_bottom) / 2
        spacing = btn_w * 0.6
        center_x = self.WIDTH / 2
        check_solution_button = Button((btn_w, btn_h), (center_x + spacing, btn_y), self.check_solution,
                                       text="Check Solution", groups=[self.all_sprites])
        new_game_button = Button((btn_w, btn_h), (center_x - spacing, btn_y), self.make_new_game,
                                       text="New Game", groups=[self.all_sprites])
        self.clickable.append(check_solution_button)
        self.clickable.append(new_game_button)

    def rebuild(self):
        for tile in self.tiles:
            for t in tile:
                t.kill()
        for s in [s for s in self.clickable if isinstance(s, Button)]:
            s.kill()
        self.clickable.clear()
        self.calculate_layout()
        self.add_numbers(self.top_left, self.distance_between, self.puzzle)
        self.add_buttons()

    def make_new_game(self):
        for tile in self.tiles:
            for t in tile:
                t.kill()
        self.clickable = [s for s in self.clickable if not isinstance(s, Tile)]
        self.puzzle = self.get_puzzle()
        self.add_numbers(self.top_left, self.distance_between, self.puzzle)

    def get_puzzle(self):
        return self.generator.create_puzzle(self.difficulty)

    def add_numbers(self, start_point, distance, puzzle):
        self.tiles = []
        size = (round(distance * .5), round(distance * .5))
        for x in range(9):
            self.tiles.append([])
            for y in range(9):
                location = (start_point[0] + (distance * x), start_point[1] + (distance * y))
                value = puzzle[x][y]
                can_edit = value == 0
                if can_edit:
                    tile = Tile(location, '', value, can_edit=True, groups=[self.all_sprites], size=size)
                    self.clickable.append(tile)
                else:
                    tile = Tile(location, str(puzzle[x][y]), value, groups=[self.all_sprites], size=size)
                self.tiles[x].append(tile)
                

    def solve(self):
        SudokuSolver(self.puzzle).solve_puzzle()
        for tile in self.tiles:
            for t in tile:
                t.kill()
        self.clickable = [s for s in self.clickable if not isinstance(s, Tile)]
        self.add_numbers(self.top_left, self.distance_between, self.puzzle)

    def check_solution(self):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                if not self.is_valid(x, y, self.tiles[x][y].value):
                    RedX(self.WIDTH, self.HEIGHT, [self.all_sprites])
                    return False
        Firework.launch(self.WIDTH, self.HEIGHT, [self.all_sprites])
        return True
    
    def is_valid(self, i, j, val):
        if val == 0:
            return False 
        
        for k in range(9):
            if (self.tiles[i][k].value == val and k != j) or (self.tiles[k][j].value == val and k != i):
                print("Invalid at ", i, j, k)
                return False
        
        start_x = i - (i % 3)
        start_y = j - (j % 3)
        for l in range(start_x, start_x + 3):
            for m in range(start_y, start_y + 3):
                if self.tiles[l][m].value == val and l != i and m != j:
                    print("Invalid because: ", l, m)
                    return False
        
        return True