# tic_tac_toe is a program that simulates the real tic_tac_toe game.
# Two players fight against each other and input their coordinates for 'X' or 'O'.

# empty list and nested list for printing and working upon
game_grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


# print the game grid with updated 'X' and 'O'
def print_grid(a_list):
    print("---------")
    for i in range(0, len(a_list), 3):
        print("|", a_list[i].replace("_", " "), a_list[i + 1].replace("_", " "), a_list[i + 2].replace("_", " "), "|")
    print("---------")


# switch players ( 1 for 'X' and 0 for 'O')
player_switch = 1

print_grid(game_grid)

# loop runs until grid runs out empty spaces
while sum(i.count(' ') for i in grid) != 0:

    # store coordinates in a list -> [1, 2]
    move = [x for x in input("Enter the coordinates: ") if x != ' ']

    # check if the coordinates are valid
    if move[0] in ['1', '2', '3'] and move[1] in ['1', '2', '3'] and len(move) == 2:

        # progress further in the game
        if grid[int(move[0]) - 1][int(move[1]) - 1] == ' ':
            row = int(move[0]) - 1
            column = int(move[1]) - 1
            if player_switch == 1:
                grid[row][column] = grid[row][column].replace(' ', 'X')
                player_switch = 0
            else:
                grid[row][column] = grid[row][column].replace(' ', 'O')
                player_switch = 1
            game_grid = [grid[i][j] for i in range(len(grid)) for j in range(len(grid))]
            print_grid(game_grid)

            # store the columns in a nested list -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
            rows = grid
            sorted_rows = [grid[j][i] for i in range(len(grid)) for j in range(len(grid))]
            columns = [sorted_rows[i:i + 3] for i in range(0, len(sorted_rows), 3)]

            # True if the row contains the same symbol i.e., either 'X' or 'O' else False
            row_X = [grid[0].count('X') == 3, grid[1].count('X') == 3, grid[2].count('X') == 3]
            row_O = [grid[0].count('O') == 3, grid[1].count('O') == 3, grid[2].count('O') == 3]

            # True if the column contains the same symbol i.e., either 'X' or 'O' else False
            column_X = [columns[0].count('X') == 3, columns[1].count('X') == 3, columns[2].count('X') == 3]
            column_O = [columns[0].count('O') == 3, columns[1].count('O') == 3, columns[2].count('O') == 3]

            # True if the diagonals contain the same symbol i.e., either 'X' or 'O' else False
            diagonal_1_X = [grid[0][0] == 'X', grid[1][1] == 'X', grid[2][2] == 'X']
            diagonal_2_X = [grid[0][2] == 'X', grid[1][1] == 'X', grid[2][0] == 'X']
            diagonal_1_O = [grid[0][0] == 'O', grid[1][1] == 'O', grid[2][2] == 'O']
            diagonal_2_O = [grid[0][2] == 'O', grid[1][1] == 'O', grid[2][0] == 'O']

            # game conditions
            if abs((sum(i.count('X') for i in grid)) - (sum(i.count('O') for i in grid))) >= 2:
                print("Impossible")
                break
            elif any(row_X) or any(row_O) or any(column_X) or any(column_O):
                print("X wins" if any(row_X) or any(column_X) else "O wins")
                break
            elif all(diagonal_1_X) or all(diagonal_2_X) or all(diagonal_1_O) or all(diagonal_2_O):
                print("{} wins".format(grid[1][1]))
                break
            elif any(row_X) is False and any(column_X) is False and any(row_O) is False and any(column_O) is False:
                if abs((sum(i.count('X') for i in rows)) - (sum(i.count('O') for i in rows))) >= 2:
                    print("Impossible")
                elif sum(i.count(' ') for i in grid) <= 1:
                    print("Draw")
                else:
                    continue

        # same coordinates can't be entered again
        else:
            print("This cell is occupied! Choose another one!")
            continue

    # coordinates cant be invalid
    else:
        if not move[0].isnumeric() or not move[1].isnumeric():
            print("You should enter numbers!")
            continue
        else:
            print("Coordinates should be from 1 to 3!")
        continue
