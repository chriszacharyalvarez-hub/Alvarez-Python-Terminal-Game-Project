Rows = 6
Columns = 7 
Empty = '.'
First_player = 'X'
Second_player = 'O'

def create_board():
    # Nagrereturn lang yan ng 2d na board wherein each section has empty muna. It uses nested list comprehension to build the rows wherein each row contains a column item.
    return [[Empty for _ in range(Columns)] for _ in range(Rows)]

def print_board(board):
    print(" 1 2 3 4 5 6 7")
    for row in board:
        # basta ung .join ginagawa nun is cinocombine mga items ng iterable into a single string
        print("|" + "|".join(row) + "|")

def drop_piece(board, col, player):
    for r in range(Rows -1, -1, -1):
        if board [r][col] == Empty:
            board [r][col] = player
            return True
    return False

def check_winner(board, player):
    for r in range(Rows):
        for c in range (Columns - 3):
            if (board[r][c] == player and
                board[r][c+1] == player and
                board[r][c+2] == player and 
                board[r][c+3] == player):
                return True

def main():
    board = create_board()
    current_player = First_player

    print("----- Connect Four -----")
    print_board(board)

    while True:
        user_input = input(f"Player {current_player}, choose a column to place your disc (1-7) or 'q' to quit the game.")

# yung .islower ==, ano lang yan kumbaga ginagawang case insensitive para kahit capital Q man nilagay ni user edi meaning parin nun is q which is to exit 
        if user_input.lower() == 'q': 
            print("Thank you for playing Connect Four!")
            break
        # Drop logic na toh repa
        if not user_input.isdigit() or not (1 <= int(user_input) <= Columns):
            print("Invalid column! Please enter a number from 1 to 7.")
            continue

        col = int(user_input) - 1  # Convert 1-7 to 0-6 index

        if drop_piece(board, col, current_player):
            print_board(board)
        else:
            print("Column is full! Try a different one.")
            continue

        # Magswitch lang ung player kasi tapos na player one
        current_player = Second_player if current_player == First_player else First_player

if __name__ == "__main__":
    main()
