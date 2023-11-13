import json
import os

class GameDataAccessor():

    def __init__(self, game_file) -> None:
        self.game_file = game_file        

    def get_game_data(self):
        with open(self.game_file, "r") as fp:
            return json.load(fp)
        

    def save_game_data(self, game_data):
        with open(self.game_file, "w") as fp:
            json.dump(game_data, fp, indent=2)
        
    def get_dir(self):
        dir = os.path.abspath(os.path.join(self.game_file, os.pardir))
        return dir


    def get_number_of_files(self):
        dir = self.get_dir()
        count = 0
        for file in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, file)):
                count += 1
        return count
    

    @staticmethod
    def get_files_in_folder(folder):
        return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]