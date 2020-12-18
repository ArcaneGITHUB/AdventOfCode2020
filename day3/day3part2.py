# https://adventofcode.com/2020/day/3
# Moving in specific increments down and across a grid, count how many "#"s occur in checked positions.
# Part 2 involves checking multiple slopes and multiplying their tree amounts together.

from functools import reduce

with open("input.txt", "r") as input_file:
    grid = input_file.read().splitlines()   # list element = y axis, character in element = x axis (of a 2D grid)
    max_lines = len(grid)
    pattern_width = len(grid[0])
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    slopes_results = []

    for slope_num, slope in enumerate(slopes):
        tree_count = 0
        x = 0
        x_interval = slope[0]
        y_interval = slope[1]

        for line in grid[::y_interval]:
            if line[(x % pattern_width)] == "#":
                tree_count += 1
            x += x_interval

        slopes_results.append(tree_count)

    print(reduce((lambda a, b: a * b), slopes_results))
