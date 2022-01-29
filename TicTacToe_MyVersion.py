###############################################################################
#                          ЗАКОНЧЕНО РАБОТАЕТ                                 #
###############################################################################

# define constants
PLAYER_1 = 'X'
PLAYER_2 = 'O'
EMPTY_CELL = '.'
MAX_BOARD_SIZE = 15


# variables

# game_board = [
#         [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
#         [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
#         [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL]
#  ]

# functions
def create_game_board():
    '''
    Создание пустой доски
    '''
    board_size = 0
    while int(board_size) not in range(3, MAX_BOARD_SIZE+1):
        board_size = input("Enter board size[3-15]: ")
        pass
    game_board = [[EMPTY_CELL for i in range(
        int(board_size))] for j in range(int(board_size))]
    return game_board


def draw_board(board):
    board_string = ''
    """
        A B C D E
       1 . . . . .
       2 . . . . .
       3 . . . . .
       4 . . . . .
       5 . . . . .
    
    """
    # create column titles
    board_string += "\t"
    for i in range(len(board)):  # board width = board height
        board_string += chr(65 + i) + " "
        pass
    board_string += "\n"

    # add board with row numbers
    for row_index in range(len(board)):  # board width = board height
        # add next row
        board_string += str(row_index + 1) + "\t"
        for cell_index in range(len(board)):
            board_string += board[row_index][cell_index] + " "
            pass
        board_string += "\n"
        pass
    return board_string


def next_move(board):
    entred_cell = ""
    if current_player == "X":
        print(f"Player 1: ")
        entred_cell = input("Enter cell(a1 or b2 or c4...): ")
    else:
        print(f"Player 2: ")
        entred_cell = input("Enter cell(a1 or b2 or c4...): ")

    cell = [(ord(entred_cell[0].upper()) - 65),
            int(entred_cell[1:len(entred_cell)]) - 1]

    if cell[0] not in range(len(board)) or cell[1] not in range(len(board)):
        print("Invalid cell")
        return next_move(board)
    if board[cell[1]][cell[0]] == EMPTY_CELL:
        board[cell[1]][cell[0]] = current_player

    return board


def game_over(game_board):
    # check rows
    for row in game_board:
        if row.count(current_player) == len(row):
            print(f"Player {current_player} wins!")
            return True
        pass
    # check columns
    for i in range(len(game_board)):
        column = []
        for row in game_board:
            column.append(row[i])
            pass
        if column.count(current_player) == len(column):
            print(f"Player {current_player} wins!")
            return True
        pass
    # check diagonals
    diagonal_1 = []
    diagonal_2 = []
    for i in range(len(game_board)):
        diagonal_1.append(game_board[i][i])
        diagonal_2.append(game_board[i][len(game_board) - i - 1])
        pass
    if diagonal_1.count(current_player) == len(diagonal_1):
        print(f"Player {current_player} wins!")
        return True
    return False


game_board = create_game_board()
current_player = PLAYER_1

while not game_over(game_board):

    print(draw_board(game_board))
    game_board = next_move(game_board)
    if game_over(game_board):
        break
    # Switching players
    current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1

    pass
