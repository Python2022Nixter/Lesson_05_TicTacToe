# define constants
PLAYER_1 = "\u274c"
PLAYER_2 = "\u2b55"
EMPTY_CELL = "\u2b1c"
MAX_BOARD_SIZE = 15


# variables

# game_board = [
#     #   1           2           3
#     [EMPTY_CELL,EMPTY_CELL,EMPTY_CELL], # row 1
#     [EMPTY_CELL,EMPTY_CELL,EMPTY_CELL], # row 2
#     [EMPTY_CELL,EMPTY_CELL,EMPTY_CELL]  # row 3
# ]

# game_board = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]


# functions
def create_game_board():
    board_size = 0
    while board_size not in range(3, MAX_BOARD_SIZE+1):
        board_size = int(input("Enter board size: "))
        pass
    board = [[EMPTY_CELL for i in range(board_size)]
             for j in range(board_size)]
    # board = [[10*i+j for i in range(board_size)] for j in range(board_size)]

    return board


def draw_board(board):
    board_string = ""

    """
        A B C D E \n
    1   . . . . . \n
    2   . x . . . \n
    3   . . . o . \n
    4   . x . . . \n
    5   . . . . . \n
    """
    # create column titles
    board_string += "\t"
    for i in range(len(board)):  # board width = board height
        board_string += chr(65 + i) + "  "
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


def next_move(board, player):
    # Request coordinates move
    user_input = input(f"Enter coordinates ({player}) [A:3]: ")
    row_index = int(user_input[2]) - 1
    cell_index = ord(user_input[0].upper()) - 65
    
    # check cell in range
    
    

    # Change game board
    board[row_index][cell_index] = player
    return


def game_over(board):

    return False


current_player = PLAYER_1
game_board = create_game_board()

while not game_over(game_board):

    print(draw_board(game_board))

    next_move(game_board, current_player)

    # Switch user
    current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1

    pass



