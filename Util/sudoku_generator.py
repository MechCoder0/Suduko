import random
from .sudoku_util import SudokuUtil

class Generator():

    def __init__(self) -> None:
        self.min = 17

    def create_puzzle(self):
        return self.generate_puzzle(0,0, self.new_board())
    

    def new_board():
        return [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    
    def generate_puzzle(self, x, y, board):
        if self.min <= 0:
            return True
        
        rand_x = random.randint(1, 9)
        rand_y = random.randint(1, 9)

        if board[x][y] != 0:
            return self.generate_puzzle(rand_x, rand_y, board)
        
        for val in range(1, 10):
            if board[x][y] == 0 and SudokuUtil.is_valid(x, y, val, board):
                board[x][y] = val
                self.min -= 1

                if self.generate_puzzle(rand_x, rand_y, board):
                    return True
                
                board[x][y] = 0
                self.min +=1

        return False