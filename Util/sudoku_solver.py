from .sudoku_util import SudokuUtil

class SudokuSolver():
    def __init__(self, board) -> None:
        self.board = board

    def solve_puzzle(self):
        if not self.solve(0, 0):
            print("ERROR")
            return False
        return True

    
    def solve(self, i, j):
        if i == len(self.board):
            j += 1
            if j == len(self.board):
                return True
            i = 0
        
        # Don't overwrite existing numbers
        if self.board[i][j] != 0:
            return self.solve(i+1, j)
        
        for x in range(1, 10):
            # If valid, set the value and continue
            if SudokuUtil.is_valid(i, j, x, self.board):
                self.board[i][j] = x

                if self.solve(i+1, j):
                    return True
                
                # If the next values are not valid, reset this one
                self.board[i][j] = 0
        
        return False