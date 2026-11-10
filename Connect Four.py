Rows = 6
Columns = 7 
Empty = '.'
First_player = 'X'
Second_player = 'O'

def create_board():
    return [[Empty for _ in range(Columns)] for _ in range(Rows)]

def print_board():
    print(" 1 2 3 4 5 6 7")
    for row in board:
        print("|" + "|".join(row) + "|")

def main():
    board = create_board()
    current_player = First_player

    print("----- Connect Four -----")
    print_board(board)