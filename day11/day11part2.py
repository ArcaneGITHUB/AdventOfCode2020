# https://adventofcode.com/2020/day/11
# Given a list of seats in rows, and rules to decide which ones become occupied/unoccupied based on adjacent seats,
# find the point at which no more changes occur.
import copy


def find_new_position(old_position):
    new_position = copy.deepcopy(old_position)
    for row_index, row in enumerate(old_position):
        for col_index, seat in enumerate(row):
            if seat != ".":
                nearby = count_nearby(row_index, col_index, old_position)
                if seat == "L" and nearby == 0:
                    new_position[row_index][col_index] = "#"
                elif seat == "#" and nearby >= 5:
                    new_position[row_index][col_index] = "L"
    return new_position


def count_nearby(row_idx, col_idx, positions):
    nearby = 0
    row_max = len(positions)
    col_max = len(positions[0])

    # Check Above
    for i in range(row_idx-1, -1, -1):
        if positions[i][col_idx] == "#":
            nearby += 1
            break
        elif positions[i][col_idx] == "L":
            break
    # Check Below
    for i in range(row_idx+1, row_max):
        if positions[i][col_idx] == "#":
            nearby += 1
            break
        elif positions[i][col_idx] == "L":
            break
    # Check Left
    for j in range(col_idx-1, -1, -1):
        if positions[row_idx][j] == "#":
            nearby += 1
            break
        elif positions[row_idx][j] == "L":
            break
    # Check Right
    for j in range(col_idx+1, col_max):
        if positions[row_idx][j] == "#":
            nearby += 1
            break
        elif positions[row_idx][j] == "L":
            break
    # Check up and right
    for i, j in zip(range(row_idx-1, -1, -1), range(col_idx+1, col_max)):
        if positions[i][j] == "#":
            nearby += 1
            break
        elif positions[i][j] == "L":
            break
    # Check up and left
    for i, j in zip(range(row_idx-1, -1, -1), range(col_idx-1, -1, -1)):
        if positions[i][j] == "#":
            nearby += 1
            break
        elif positions[i][j] == "L":
            break
    # Check down and right
    for i, j in zip(range(row_idx+1, row_max), range(col_idx+1, col_max)):
        if positions[i][j] == "#":
            nearby += 1
            break
        elif positions[i][j] == "L":
            break
    # Check down and left
    for i, j in zip(range(row_idx+1, row_max), range(col_idx-1, -1, -1)):
        if positions[i][j] == "#":
            nearby += 1
            break
        elif positions[i][j] == "L":
            break
    return nearby


with open("input.txt", "r") as file:
    current_position = [list(line[:-1]) for line in file]

change = True
while change:
    for row in current_position:
        print(row)
    print("-----\n")
    new_position = find_new_position(current_position)
    if new_position == current_position:
        change = False
    else:
        current_position = new_position
print("Answer: ", str(current_position).count("#"))
