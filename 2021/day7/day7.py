# https://adventofcode.com/2021/day/7
# Given a list of crab positions on an X axis, find the lowest amount of steps of 1 required to align them all
# on the same position.
# Part 1: Each step costs 1 fuel
# Part 2: Each additional step costs 1 extra fuel. 1, then 2, then 3, then 4 etc


# Input crab positions
def get_crab_positions():
    with open("input", "r") as input_file:
        crab_positions = [int(x) for x in input_file.read().strip().split(",")]
    return crab_positions


# For each crab, find the potential cost of moving to every position and add that to an array.
# Return the position with the lowest total cost.
def part_one():
    positions_cost = [0] * 1000
    for crab_position in get_crab_positions():
        for position, cost in enumerate(positions_cost):
            positions_cost[position] += abs(position - crab_position)
    fuel_cost = min(positions_cost)
    return fuel_cost


# For each crab, find the potential cost of moving to every position and add that to an array.
# Return the position with the lowest total cost.
def part_two():
    positions_cost = [0] * 1000
    for crab_position in get_crab_positions():
        for position, cost in enumerate(positions_cost):
            last_move_cost = abs(position - crab_position)
            # Factorial but with addition instead of multiplication
            positions_cost[position] += int(((last_move_cost*last_move_cost) + last_move_cost) / 2)
    fuel_cost = min(positions_cost)
    return fuel_cost


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
