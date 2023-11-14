
from Util.sudoku_generator import Generator
from Util.sudoku_solver import SudokuSolver
from Util.sudoku_util import SudokuUtil
from Util.number_remover import NumberRemover


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

board2 = [
  [0, 0, 1, 5, 0, 0, 0, 7, 0],
  [0, 0, 4, 0, 6, 0, 0, 0, 9],
  [0, 3, 0, 0, 0, 4, 0, 0, 0],
  [6, 2, 0, 0, 0, 5, 1, 0, 0],
  [0, 4, 0, 0, 0, 0, 5, 2, 0],
  [0, 0, 0, 0, 4, 8, 0, 0, 3],
  [4, 1, 0, 0, 7, 0, 0, 0, 0],
  [0, 0, 6, 8, 0, 0, 0, 0, 1],
  [8, 0, 0, 0, 0, 9, 0, 3, 0],
]

new_board = Generator().create_puzzle()
SudokuUtil.print_board(new_board)
solver = SudokuSolver(new_board)
solver.solve_puzzle()
SudokuUtil.print_board(new_board)