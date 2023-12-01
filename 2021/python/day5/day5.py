# https://adventofcode.com/2021/day/5
# Given a list of vertical, horizontal and 45 degree diagonal line segments:
# Part 1: Only considering horizontal and vertical lines, determine the number of points where at least 2 lines overlap.
# Part 2: Considering all lines, determine the number of points where at least 2 lines overlap.

import numpy


# Input line_segments
def input_values():
    with open("input", "r") as input_file:
        line_segments = [x.rstrip("\n") for x in input_file]  # Put lines of file into list, removing newlines
        line_segments = [x.split(" -> ") for x in line_segments]  # split each line into start & end points
        line_segments = [[x[0].split(","), x[1].split(",")] for x in line_segments]  # split each point into x,y co-ords
        # Convert string to int
        line_segments = [[[int(coord) for coord in point] for point in line_segment] for line_segment in line_segments]
    return line_segments


# Separately draws horizontal and vertical lines only on a grid
# Then counts any coordinates that have been marked more than once
def part_one():
    grid = numpy.zeros((1000, 1000), dtype=int)
    line_segments = input_values()
    for line_segment in line_segments:
        # if x values are the same (line is vertical)
        if line_segment[0][0] == line_segment[1][0]:
            x = line_segment[0][0]
            y = min(line_segment[0][1], line_segment[1][1])
            while y <= max(line_segment[0][1], line_segment[1][1]):
                grid[y][x] += 1
                y += 1
        # if y values are the same (line is horizontal)
        elif line_segment[0][1] == line_segment[1][1]:
            y = line_segment[0][1]
            x = min(line_segment[0][0], line_segment[1][0])
            while x <= max(line_segment[0][0], line_segment[1][0]):
                grid[y][x] += 1
                x += 1
    overlap_points = numpy.count_nonzero(grid > 1)
    return overlap_points


# Find all points where at least 2 lines overlap.
# Finds vector from point 1 to point 2 and uses that to mark the coordinates on a grid from point 1 to
# point 2 (inclusively).
# Then counts any coordinates that have been marked more than once.
def part_two():
    grid = numpy.zeros((1000, 1000), dtype=int)
    line_segments = input_values()
    for line_segment in line_segments:
        x_diff = line_segment[1][0] - line_segment[0][0]
        y_diff = line_segment[1][1] - line_segment[0][1]
        x, y = line_segment[0]
        reached_end = False
        while not reached_end:
            if [x, y] == line_segment[1]:
                reached_end = True
            grid[y][x] += 1
            x += numpy.sign(x_diff)
            y += numpy.sign(y_diff)
    overlap_points = numpy.count_nonzero(grid > 1)
    return overlap_points


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
