# https://adventofcode.com/2021/day/11
# Given a list of octopuses described by their energy level. Each "turn", all energy levels are increased by 1.
# When an octopus has an energy level greater than 9, it "flashes". This increases the energy level of all adjacent
# octopuses by 1. If they are above 9, they flash too. An octopus can only flash once per step.
# Part 1: Return the number of flashes after 100 iterations
# Part 2: Return the first step where all octopuses flash.

# Input grid as list of list of ints
def get_starting_grid() -> list[list]:
    with open("input", "r") as input_file:
        octopus_grid = input_file.read().strip().split("\n")
        for index, line in enumerate(octopus_grid):
            octopus_grid[index] = [int(octopus) for octopus in line]
    return octopus_grid


# Implements grid cycle and runs it for 100 iterations. Returns number of flashes.
def part_one():
    octopus_grid: list[list] = get_starting_grid()
    flashes = 0
    for i in range(100):
        # increase all energy levels by 1
        for v, line in enumerate(octopus_grid):
            for h, octopus in enumerate(line):
                octopus_grid[v][h] += 1
        # For all >9, flash. Increase adjacents(including diagonals) by 1 and check for >9s again. Repeat until
        # no more flashes.
        flashing = True
        already_flashed = []
        while flashing:
            flashing = False
            for v, line in enumerate(octopus_grid):
                for h, octopus in enumerate(line):
                    if octopus > 9 and (v, h) not in already_flashed:
                        flashing = True
                        flashes += 1
                        already_flashed.append((v, h))
                        # increments adjacents top to bottom, left to right
                        # Line above
                        if v-1 >= 0:
                            if h-1 >= 0:
                                octopus_grid[v-1][h-1] += 1
                            octopus_grid[v-1][h] += 1
                            if h+1 < len(line):
                                octopus_grid[v-1][h+1] += 1
                        # Current line
                        if h-1 >= 0:
                            octopus_grid[v][h-1] += 1
                        if h+1 < len(line):
                            octopus_grid[v][h+1] += 1
                        # Line below
                        if v+1 < len(octopus_grid):
                            if h-1 >= 0:
                                octopus_grid[v+1][h-1] += 1
                            octopus_grid[v+1][h] += 1
                            if h+1 < len(line):
                                octopus_grid[v+1][h+1] += 1

        # Any that flashed get set to 0
        for v, line in enumerate(octopus_grid):
            for h, octopus in enumerate(line):
                if octopus > 9:
                    octopus_grid[v][h] = 0
    return flashes


# Implements grid cycle and runs it until all octopuses flash during a step. Returns that step.
def part_two():
    octopus_grid: list[list] = get_starting_grid()
    flashes = 0
    i = 0
    while True:
        i += 1
        # increase all energy levels by 1
        for v, line in enumerate(octopus_grid):
            for h, octopus in enumerate(line):
                octopus_grid[v][h] += 1
        # For all >9, flash. Increase adjacents(including diagonals) by 1 and check for >9s again. Repeat until
        # no more flashes.
        flashing = True
        already_flashed = []
        while flashing:
            flashing = False
            for v, line in enumerate(octopus_grid):
                for h, octopus in enumerate(line):
                    if octopus > 9 and (v, h) not in already_flashed:
                        flashing = True
                        flashes += 1
                        already_flashed.append((v, h))
                        # Increment Adjacents:
                        # Line above
                        if v-1 >= 0:
                            if h-1 >= 0:
                                octopus_grid[v-1][h-1] += 1
                            octopus_grid[v-1][h] += 1
                            if h+1 < len(line):
                                octopus_grid[v-1][h+1] += 1
                        # Current line
                        if h-1 >= 0:
                            octopus_grid[v][h-1] += 1
                        if h+1 < len(line):
                            octopus_grid[v][h+1] += 1
                        # Line below
                        if v+1 < len(octopus_grid):
                            if h-1 >= 0:
                                octopus_grid[v+1][h-1] += 1
                            octopus_grid[v+1][h] += 1
                            if h+1 < len(line):
                                octopus_grid[v+1][h+1] += 1
        # Any that flashed get set to 0
        for v, line in enumerate(octopus_grid):
            for h, octopus in enumerate(line):
                if octopus > 9:
                    octopus_grid[v][h] = 0
        # Check if all octopuses flashed this step
        if len(already_flashed) == 100:
            return i


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
