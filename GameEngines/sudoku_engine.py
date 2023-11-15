from .base_screen import BaseScreen
from Controllers.sudoku_controller import SodukoController
from Util.sudoku_generator import Generator
from Util.sudoku_solver import SudokuSolver
from Util.number_remover import NumberRemover
from GameObjects.tile import Tile

class SudokuEngine(BaseScreen):
    def __init__(self) -> None:
        super().__init__(SodukoController)
        self.generator = Generator()
        self.puzzle = self.get_easy_puzzle()

    def start_game(self):
        self.add_numbers((100, 100), 100, self.puzzle)
        super().start_game(self.screen_writer.print_sudoku_board)
    

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
        for x in range(9):
            for y in range(9):
                location = (start_point[0] + (distance * x), start_point[1] + (distance * y))
                Tile(location, str(puzzle[x][y]), [self.all_sprites])

    def solve(self):
        SudokuSolver(self.puzzle).solve_puzzle()
        self.add_numbers((100, 100), 100, self.puzzle)