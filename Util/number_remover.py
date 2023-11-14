import random

class NumberRemover():
    
    @staticmethod
    def remove(nums_to_remove, board):
        for i in range(nums_to_remove):
            rand_x = random.randint(0, 8)
            rand_y = random.randint(0, 8)

            while board[rand_x][rand_y] == 0:
                rand_x = random.randint(1, 8)
                rand_y = random.randint(1, 8)
            board[rand_x][rand_y] = 0