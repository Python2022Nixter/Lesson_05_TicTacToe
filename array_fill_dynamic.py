EMPTY_CELL = "."
board_size = int(input("Enter board size: "))
game_board = [EMPTY_CELL for i in range(board_size)]
print()
print (game_board)
game_board = [i for i in range(board_size)]
print()
print (game_board)
game_board = [[EMPTY_CELL for i in range(board_size)] for j in range(board_size)]
print()
print (game_board)
game_board = [[[j, i] for i in range(board_size)] for j in range(board_size)]
print()
print (game_board)
game_board = [[str(j)+":"+str(i) for i in range(board_size)] for j in range(board_size)]
print (game_board)
print()
single_row = ["*" for i in range(10)]
all_rows = [single_row for i in range (5)]
print(all_rows)
