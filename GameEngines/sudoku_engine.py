from .base_screen import BaseScreen
from Controllers.sudoku_controller import SodukoController

class SudokuEngine(BaseScreen):
    def __init__(self) -> None:
        super().__init__(SodukoController)

    def start_game(self):
        return super().start_game(self.screen_writer.print_sudoku_board)
    

    