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

def main():
    board = create_board()
    current_player = First_player

    print("----- Connect Four -----")
    print_board(board)

    while True:
        user_input = input(f"Player {current_player}, choose a column to place your disc (1-7) or 'q' to quit the game.")

# yung .islower ==, ano lang yan kumbaga ginagawang case insensitive para kahit capital Q man nilagay ni user edi meaning parin nun is q which is to exit 
        if user_input.islower() == 'q': 
            print("Thank you for playing Connect Four!")
            break
        # Drop logic na toh repa
        print(f"You selected {user_input}.")

        # Magswitch lang ung player kasi tapos na player one
        current_player = Second_player if current_player == First_player else First_player

if __name__ == "__main__":
    main()
