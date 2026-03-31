from .base_screen import BaseScreen
from Controllers.start_controller import StartScreenController
from GameEngines.sudoku_engine import SudokuEngine
from GameEngines.level_select_engine import LevelSelectEngine
from GameObjects.marker import Marker
from Util.util import Util

class PlayEngine(BaseScreen):
    def __init__(self) -> None:
        super().__init__(StartScreenController)
        self.selections = [
            (SudokuEngine(), (0, self.WIDTH)),
            (LevelSelectEngine(), (0, self.WIDTH))
        ]

    def start_game(self):
        print("The game has begun")
        self.create_marker()
        super().start_game(self.screen_writer.print_start_screen)

    def create_marker(self):
        h = self.HEIGHT
        y_pos = h * (0.80 + (self.controller.chosen_game * 0.10))
        location = (Util.get_middle(0, self.WIDTH), y_pos)
        self.marker = Marker(location)
        self.all_sprites.add(self.marker)

    def rebuild(self):
        self.marker.kill()
        self.create_marker()