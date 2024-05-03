import random



def blank_sudoku():
    sudoku = []
    for i in range(9):
        line = []
        for j in range(1, 10):
            line.append(0)
        sudoku.append(line)
    return sudoku


def print_sudoku(sudoku):
    sudoku.insert(3, ["--------------+--------------+--------------"])
    sudoku.insert(7, ["--------------+--------------+--------------"])
    for line in sudoku:
        if line == ["--------------+--------------+--------------"]:
            print(line[0])
        else:
            for index, num in enumerate(line):
                if num == 0:
                    num_str = ' ' * 3
                else:
                    num_str = "%3d" % num

                if index == 2 or index == 5:
                    print("%s |" % num_str, end="")
                else:
                    print("%s  " % num_str, end="")

            print()
    print("\n")


def find_empty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return [True, i, j]
    return [False, i, j]


def isvalid(num, row, col, sudoku):
    if num in sudoku[row]:
        return False

    for line in sudoku:
        if num == line[col]:
            return False

    if not cubes(num, row, col, sudoku):
        return False

    return True


def cubes(num: int, row: int, col: int, sudoku: list):
    left = range(0, 3)
    center = range(3, 6)
    right = range(6, 9)

    up = range(0, 3)
    middle = range(3, 6)
    down = range(6, 9)

    if row in up:
        row_cube = up
    elif row in middle:
        row_cube = middle
    elif row in down:
        row_cube = down

    if col in left:
        col_cube = left
    elif col in center:
        col_cube = center
    elif col in right:
        col_cube = right

    for index_row in row_cube:
        for index_col in col_cube:
            if num == sudoku[index_row][index_col]:
                return False
    return True


def sudoku_solver():
    sudoku = blank_sudoku()

    iteration_counter = 0
    while find_empty(sudoku)[0]:
        empty = find_empty(sudoku)
        shuffle_line = random.sample(range(1, 10), 9)
        count = 0
        for num in shuffle_line:
            row = empty[1]
            col = empty[2]
            if isvalid(num, row, col, sudoku):
                sudoku[row][col] = num
                break
            count += 1
        if count == 9:
            if not num_needed(row, col, sudoku):
                sudoku[row] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        iteration_counter += 1
        if iteration_counter > 600:
            print("failed !, try again ...")
            exit()

    return sudoku


def num_needed(row: int, col: int, sudoku: list):
    # checks if solution is possible
    one_to_nine = range(1, 10)
    needed_numbers = []
    for num in one_to_nine:
        if num not in sudoku[row]:
            needed_numbers.append(num)

    for i in range(9):
        for num in needed_numbers:
            if num == sudoku[i][col]:
                return False
    return True


print_sudoku(sudoku_solver())
