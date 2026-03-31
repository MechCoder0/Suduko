import random
from .sudoku_util import SudokuUtil
import copy

class Generator():

    def create_puzzle(self, difficulty="easy"):
        board = self.new_board()
        self.fill(board)
        puzzle = copy.deepcopy(board)

        # Determine how many numbers to remove based on difficulty
        if difficulty == "easy":
            remove_count = 30
        elif difficulty == "medium":
            remove_count = 45
        else: # hard
            remove_count = 60

        NumberRemover.remove(remove_count, puzzle)
        return puzzle

    def new_board(self):
        return [[0]*9 for _ in range(9)]

    def fill(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for val in nums:
                        if SudokuUtil.is_valid(i, j, val, board):
                            board[i][j] = val
                            if self.fill(board):
                                return True
                            board[i][j] = 0
                    return False
        return True


class NumberRemover():
    @staticmethod
    def remove(nums_to_remove, board):
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)
        for i, j in cells[:nums_to_remove]:
            board[i][j] = 0