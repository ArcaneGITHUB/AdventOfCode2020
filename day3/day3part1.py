# https://adventofcode.com/2020/day/3
# Moving in specific increments down and across a grid, count how many "#"s occur in checked positions.

with open("input.txt", "r") as input_file:
    grid = input_file.read().splitlines()   # list element = y axis, character in element = x axis (of a 2D grid)
max_lines = len(grid)
pattern_width = len(grid[0])
x = 0
tree_count = 0

for line in grid:
    if line[(x % pattern_width)] == "#":
        tree_count += 1
    x += 3

print("Tree count = " + str(tree_count))
