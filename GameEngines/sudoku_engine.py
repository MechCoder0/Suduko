from .base_screen import BaseScreen
from Controllers.sudoku_controller import SodukoController
from Util.sudoku_generator import Generator
from Util.sudoku_solver import SudokuSolver
from Util.number_remover import NumberRemover
from GameObjects.tile import Tile
from GameObjects.button import Button

class SudokuEngine(BaseScreen):
    def __init__(self) -> None:
        super().__init__(SodukoController)
        self.generator = Generator()
        self.puzzle = self.get_easy_puzzle()
        self.clickable = []
        self.tiles = []

    def start_game(self):
        top_left = (50, 50)
        bottom_right = (self.WIDTH *.9, self.HEIGHT *.9)
        distance_between = (bottom_right[0] - top_left[0])/9
        top_left = (round(distance_between/2)+ 50, round(distance_between/2) + 50)
        self.add_numbers(top_left, distance_between, self.puzzle)
        self.add_buttons()
        super().start_game(self.screen_writer.print_sudoku_board)

    def add_buttons(self):
        check_solution_button = Button((300,50), (self.WIDTH/2, self.HEIGHT * 0.9), self.check_solution, 
                                       text="Check Solution", groups=[self.all_sprites])
        self.clickable.append(check_solution_button)


    def get_easy_puzzle(self):
        new_puzzle = self.generator.create_puzzle()
        # solve the puzzle
        can_solve = SudokuSolver(new_puzzle).solve_puzzle()
        while not can_solve:
            print("Making a new puzzle")
            new_puzzle = self.generator.create_puzzle()
            can_solve = SudokuSolver(new_puzzle).solve_puzzle()
        # remove 15 numbers
        NumberRemover.remove(15, new_puzzle)
        return new_puzzle
    
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
        self.add_numbers((100, 100), 100, self.puzzle)

    def check_solution(self):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                print("Checking:", x, y)
                is_valid = self.is_valid(x, y, self.tiles[x][y].value)
                print("It is valid: ", is_valid)
                if not is_valid:
                    print("Is not the valid solution")
                    return False
        print("Is the valid solution.")
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