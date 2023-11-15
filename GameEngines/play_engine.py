from .base_screen import BaseScreen
from Controllers.start_controller import StartScreenController
from GameEngines.sudoku_engine import SudokuEngine
from GameObjects.marker import Marker
from Util.util import Util

class PlayEngine(BaseScreen):
    def __init__(self) -> None:
        super().__init__(StartScreenController)
        self.selections = [
            (SudokuEngine(), (0, self.WIDTH))
        ]

    def start_game(self):
        print("The game has begun")
        super().start_game(self.screen_writer.print_start_screen)

    def create_marker(self):
        location = (Util.get_middle(0, self.WIDTH), self.HEIGHT * .80)
        self.marker = Marker(location)