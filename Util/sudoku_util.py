
class SudokuUtil():

    @staticmethod
    def is_valid(i, j, val, board):

        for k in range(9):
            if board[i][k] == val or board[k][j] == val:
                return False
        
        start_x = i - (i % 3)
        start_y = j - (j % 3)
        for l in range(start_x, start_x + 3):
            for m in range(start_y, start_y + 3):
                if board[l][m] == val:
                    return False
        
        return True
    
    @staticmethod
    def print_board(board):
        for i in range(len(board)):
            row = ""
            for j in range(len(board)):
                if j % 3 == 0:
                    row += "|"
                row += str(board[i][j])
            
            row += "|"

            if i % 3 == 0:
                print("-------------")
            print(row)

        print("-------------")