# https://adventofcode.com/2020/day/5
# Import a set of airplane seat identifiers (described using binary space partitioning)
# Identify the highest value seat ID according to a formula (seatID = (8*row) + column)

from math import ceil as round_up

with open("input.txt", "r") as boarding_pass_list:
    highest_ID = 0
    for boarding_pass in boarding_pass_list:
        row_min = 0
        row_max = 127
        column_min = 0
        column_max = 7

        # Find row
        for split_direction in boarding_pass[0:7]:
            if split_direction == "F":
                row_max = (row_min + row_max)//2
            else:
                row_min = round_up(((row_min + row_max)/2))
        row = row_min

        # Find column
        for split_direction in boarding_pass[7:10]:
            if split_direction == "L":
                column_max = (column_min + column_max) // 2
            else:
                column_min = round_up(((column_min + column_max) / 2))
        column = column_min

        # Calculate seat ID and compare to highest found so far
        seat_ID = (8*row) + column
        if seat_ID > highest_ID:
            highest_ID = seat_ID

    print("Highest ID: " + str(highest_ID))
