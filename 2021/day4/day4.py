# https://adventofcode.com/2021/day/4
# 5x5 grids of numbers <= 2 digits
# Numbers drawn in given order and all occurrences of number are marked
# First row with a full row or full column of marked numbers wins
# Score of the winning board = sum of all unmarked numbers * number that was just called
#
# Part 1: What is the final score of the winning board?
#   Option 1: Go through each board one by one and find out how many turns it would take to win. Use lowest.
#   Option 2: Go through all boards for each drawn number until winning board is found.

# Input number draw and boards
def input_values():
    with open("input", "r") as input_file:
        input_data = [line.rstrip("\n") for line in input_file]
        number_draw = input_data.pop(0).split(",")
        boards = []
        new_board = []
        for index, line in enumerate(input_data):
            if line != "":
                new_board.append(line.split())
                if len(new_board) == 5:
                    boards.append(new_board)
                    new_board = []
    return number_draw, boards


# Converts element of nested list into tuple containing the drawn number and True
def mark_draw(board, draw):
    for r, row in enumerate(board):
        for n, number in enumerate(row):
            if number == draw:
                board[r][n] = (draw, True)
                return board
    return board


# Returns true if a row or colum contains 5 numbers marked with True
def validate_win(board):
    # Check for complete rows
    column_marks = [0] * 5
    for row in board:
        row_marks = 0
        for column, element in enumerate(row):
            if type(element) is not str:
                row_marks += 1
                column_marks[column] += 1
        if row_marks == 5 or 5 in column_marks:
            return True
    return False


# Returns the sum of the unmarked values multiplied by the drawn number
def calc_score(board, draw):
    unmarked_sum = 0
    for row in board:
        for element in row:
            if type(element) is str:
                unmarked_sum += int(element)
    return str(unmarked_sum * int(draw))


# Find first winner by repeatedly marking a number in all boards then checking for winners
def part_one():
    number_draw, boards = input_values()
    for draw in number_draw:
        for b, board in enumerate(boards):
            boards[b] = mark_draw(board, draw)
            if validate_win(boards[b]):
                return calc_score(boards[b], draw) + " Table: " + str(b)


# Remove winners from list until one remains, then play the game out until it wins and return its score
def part_two():
    number_draw, boards = input_values()
    non_winning_boards = [x for x in range(len(boards))]
    for draw in number_draw:
        for b, board in enumerate(boards):
            boards[b] = mark_draw(board, draw)
            if validate_win(boards[b]):
                if b in non_winning_boards:
                    if len(non_winning_boards) == 1 and validate_win(boards[b]):
                        return calc_score(boards[non_winning_boards[0]], draw) + " Table: " + str(b)
                    non_winning_boards.remove(b)


print(part_one())
print(part_two())
