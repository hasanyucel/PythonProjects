def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("---------------------")

        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)  # row, col

    return None

def valid(sudoku, num, pos):
    # Check row
    for i in range(len(sudoku[0])):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    # Check sudokux
    sudokux_x = pos[1] // 3
    sudokux_y = pos[0] // 3

    for i in range(sudokux_y*3, sudokux_y*3 + 3):
        for j in range(sudokux_x * 3, sudokux_x*3 + 3):
            if sudoku[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(sudoku, i, (row, col)):
            sudoku[row][col] = i

            if solve(sudoku):
                return True

            sudoku[row][col] = 0

    return False

