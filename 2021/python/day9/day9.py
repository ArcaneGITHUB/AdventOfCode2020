# https://adventofcode.com/2021/day/9
# Given a list of "cave floors" consisting of a list of heights 0-9.
#
# Part 1: For each height value, compare it to adjacent values and count it as a low point if all adjacents are higher.
# Return the sum of the risk levels (value + 1) of all low points.
# Part 2: For all low points, recursively(depth first) consider if an adjacent is part of the same "basin" and if so,
# repeat the consideration until all values in a basin have been collected. Use these to find the size of the basin.
# Return the product of the 3 largest basins.


# Input location heights
def get_height_data():
    with open("input", "r") as input_file:
        height_map = input_file.read().strip().split("\n")
    return height_map


# Returns a list of low points described by coordinates
def get_low_points():
    floors = get_height_data()
    low_points = []
    for v, floor in enumerate(floors):  # vertical
        for h, location in enumerate(floor):  # horizontal
            adjacents = []
            if 0 <= (v-1) < len(floors):
                adjacents.append(floors[v-1][h])
            if 0 <= (v+1) < len(floors):
                adjacents.append(floors[v+1][h])
            if 0 <= (h-1) < len(floor):
                adjacents.append(floor[h-1])
            if 0 <= (h+1) < len(floor):
                adjacents.append(floor[h+1])

            if all(adjacent > location for adjacent in adjacents):
                low_points.append((v, h))
    return low_points


# Returns a list of all basin elements by recursively checking adjacent elements.
def find_basin_elements(location, basin_points):
    floors = get_height_data()
    v = location[0]
    h = location[1]
    if 0 <= (v - 1) < len(floors) and (v-1, h) not in basin_points:  # Above
        if int(floors[v-1][h]) < 9:
            basin_points.add((v-1, h))
            basin_points.union(find_basin_elements((v - 1, h), basin_points))
    if 0 <= (v + 1) < len(floors) and (v+1, h) not in basin_points:  # Below
        if int(floors[v+1][h]) < 9:
            basin_points.add((v+1, h))
            basin_points.union(find_basin_elements((v + 1, h), basin_points))
    if 0 <= (h - 1) < len(floors[0]) and (v, h-1) not in basin_points:  # Left
        if int(floors[v][h-1]) < 9:
            basin_points.add((v, h-1))
            basin_points.union(find_basin_elements((v, h - 1), basin_points))
    if 0 <= (h + 1) < len(floors[0]) and (v, h+1) not in basin_points:  # Right
        if int(floors[v][h+1]) < 9:
            basin_points.add((v, h+1))
            basin_points.union(find_basin_elements((v, h + 1), basin_points))
    return basin_points


# For each location of each floor, check if each adjacent (above, below, left, right) element exists and increase the
# risk level if the location is lower than all adjacents
def part_one():
    total_risk_level = 0
    floors = get_height_data()
    for point in get_low_points():
        total_risk_level += int(floors[point[0]][point[1]]) + 1
    return total_risk_level


# For each low point, find all elements
def part_two():
    low_points = get_low_points()
    basin_sizes = []
    for point in low_points:
        basin_sizes.append(len(find_basin_elements(point, {point})))
    basin_sizes.sort()
    return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
