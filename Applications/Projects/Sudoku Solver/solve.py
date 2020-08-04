import numpy as np

sudoku = np.array([ [7, 8, 0, 4, 0, 0, 1, 2, 0], 
                    [6, 0, 0, 0, 7, 5, 0, 0, 9], 
                    [0, 0, 0, 6, 0, 1, 0, 7, 8], 
                    [0, 0, 7, 0, 4, 0, 2, 6, 0], 
                    [0, 0, 1, 0, 5, 0, 9, 3, 0], 
                    [9, 0, 4, 0, 6, 0, 0, 0, 5], 
                    [0, 7, 0, 3, 0, 0, 0, 1, 2], 
                    [1, 2, 0, 0, 0, 7, 4, 0, 0], 
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]  ])

def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")

print_sudoku(sudoku)