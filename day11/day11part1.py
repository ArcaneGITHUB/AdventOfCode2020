# https://adventofcode.com/2020/day/11
# Given a list of seats in rows, and rules to decide which ones become occupied/unoccupied based on adjacent seats,
# find the point at which no more changes occur.
import copy


def find_new_position(old_position):
    new_position = copy.deepcopy(old_position)
    for row_index, row in enumerate(old_position):
        for col_index, seat in enumerate(row):
            if seat != ".":
                adjacent = count_adjacent(row_index, col_index, old_position)
                if seat == "L" and adjacent == 0:
                    new_position[row_index][col_index] = "#"
                elif seat == "#" and adjacent >= 4:
                    new_position[row_index][col_index] = "L"
    return new_position


def count_adjacent(row_idx, col_idx, positions):
    adjacent = 0
    row_max = len(positions)
    col_max = len(positions[0])
    for i in range(row_idx - 1, row_idx + 2):
        for j in range(col_idx - 1, col_idx + 2):
            if not (i == row_idx and j == col_idx):
                if 0 <= i < row_max and 0 <= j < col_max:
                    if positions[i][j] == "#":
                        adjacent += 1

    return adjacent


with open("input.txt", "r") as file:
    current_position = [list(line[:-1]) for line in file]

change = True
while change:
    new_position = find_new_position(current_position)
    if new_position == current_position:
        change = False
    else:
        current_position = new_position
print("Answer: ", str(current_position).count("#"))
