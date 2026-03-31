from .base_screen import BaseScreen
from Controllers.level_select_controller import LevelSelectController
from GameObjects.button import Button

class LevelSelectEngine(BaseScreen):
    def __init__(self) -> None:
        super().__init__(LevelSelectController)
        self.clickable = []

    def start_game(self):
        self.calculate_layout()
        self.add_buttons()
        super().start_game(self.screen_writer.print_level_select)

    def calculate_layout(self):
        self.btn_w = round(self.WIDTH * 0.25)
        self.btn_h = round(self.HEIGHT * 0.05)
        self.center_x = self.WIDTH / 2
        self.y_start = self.HEIGHT * 0.4
        self.spacing = self.btn_h * 2

    def add_buttons(self):
        self.clickable = []
        easy_btn = Button((self.btn_w, self.btn_h), (self.center_x, self.y_start), 
                          lambda: self.select_level("easy"), text="Easy", groups=[self.all_sprites])
        medium_btn = Button((self.btn_w, self.btn_h), (self.center_x, self.y_start + self.spacing), 
                            lambda: self.select_level("medium"), text="Medium", groups=[self.all_sprites])
        hard_btn = Button((self.btn_w, self.btn_h), (self.center_x, self.y_start + 2 * self.spacing), 
                          lambda: self.select_level("hard"), text="Hard", groups=[self.all_sprites])
        
        self.clickable.extend([easy_btn, medium_btn, hard_btn])

    def rebuild(self):
        for s in self.clickable:
            s.kill()
        self.clickable.clear()
        self.calculate_layout()
        self.add_buttons()

    def select_level(self, level):
        print(f"Selected level: {level}")
        # Logic to initiate the game with the selected level would go here.
        # For now, we return to the previous screen flow.
        self.return_to_start_screen()