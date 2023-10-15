#VinayRatnam
#10/05/23
"""Program for Connect-Four game"""

def initialize_board(num_rows, num_cols):
    """Creates nested list for game board based on user inputs of height and width"""
    board = []
    for i in range(0, num_rows):
       board.append([])
       for j in range(0, num_cols):
           board[i].append("-")
    return board

def print_board(board):
    """Prints board whenever called"""
    board_copy = board[:]
    board_copy.reverse()
    for i in range(0, len(board_copy)):
        for j in range(0, len(board_copy[i])):
            print(board_copy[i][j], end = " ")
        print()
    print()

def insert_chip(board, col, chip_type):
    """Inserts user's chip into proper spot"""
    i = 0
    for i in range(0, len(board)):
        if board[i][col] == "-":
            board[i][col] = chip_type
            break
    return i

def check_if_winner(board, col, row, chip_type):
    """Checks if there is a winner after a user inputs a token"""
    output = ""
    if row >= 3:
        x = [board[row][col], board[row - 1][col], board[row - 2][col], board[row - 3][col]]
        if x == [chip_type, chip_type, chip_type, chip_type]:
            output = True
    for i in range(0, len(board[row]) - 3):
        if board[row][i:i + 4] == [chip_type, chip_type, chip_type, chip_type]:
            output = True
            break
    return output

def main():
    #ask user for height and length of board to create board
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    game_board = initialize_board(height, length)
    print_board(game_board)

    #assign players with their tokens
    print("Player 1: x\nPlayer 2: o")

    turn = 0
    chosen_column = 1000
    chip = ""
    winner = 0
    condition = True
    while condition == True: #while loop for the game
        if turn % 2 == 0:
            chosen_column = int(input("Player 1: Which column would you like to choose? "))
            chip = "x"
            winner = 1
        else:
            chosen_column = int(input("Player 2: Which column would you like to choose? "))
            chip = "o"
            winner = 2
        chosen_row = insert_chip(game_board, chosen_column, chip)
        print_board(game_board)

        winner_or_not = check_if_winner(game_board, chosen_column, chosen_row, chip)
        if winner_or_not: #checks if there is a winner and ends program if there is
            print(f"Player {winner} won the game!")
            break
        if game_board[len(game_board) - 1].count("-") == 0: #checks if it is a draw and ends program if so
            print("Draw. Nobody wins.")
            break
        turn += 1

if __name__=="__main__":
    main()