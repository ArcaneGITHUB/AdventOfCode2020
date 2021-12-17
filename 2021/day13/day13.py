# https://adventofcode.com/2021/day/13
# Given a list of dots on a "transparent sheet". The sheet will be folded along given horizontal and vertical lines.
# Any overlapping dots are considered as a single dot.
# Part 1: Fold the sheet about a given line and return the number of visible dots.
# Part 2: Execute all the given folds and take the answer from the resulting matrix.


# Inputs, parses and returns a list of dots and list of fold instructions from file.
def get_input() -> tuple[list[tuple], list[tuple]]:
    with open("input", "r") as input_file:
        instructions = input_file.read().strip().split("\n\n")
        # Dot locations
        dot_locations = instructions[0].split("\n")
        dot_locations = [tuple(int(coord) for coord in coord_pair.split(",")) for coord_pair in dot_locations]
        # Fold Instructions
        fold_instructions = [instruction[11:] for instruction in instructions[1].split("\n")]
        fold_instructions = [tuple(instruction.split("=")) for instruction in fold_instructions]
        fold_instructions = [tuple([instruction[0], int(instruction[1])]) for instruction in fold_instructions]
    return dot_locations, fold_instructions


# Execute the first fold and return the number of dots in the result.
def part_one():
    dot_locations, fold_instructions = get_input()
    # Do the first fold
    fold_line = fold_instructions[0][1]
    locations_after_fold = set([dot for dot in dot_locations if dot[0] < fold_line])
    locations_to_be_folded = set(dot_locations) - locations_after_fold

    for location in locations_to_be_folded:
        locations_after_fold.add((fold_line - (location[0] - fold_line), location[1]))
    return len(locations_after_fold)


# Executes all folds and returns a 2d matrix populated with the resulting dots.
def part_two():
    dot_locations, fold_instructions = get_input()

    for fold in fold_instructions:
        fold_direction = fold[0]
        fold_line = fold[1]

        # Takes all points after the fold and mirrors them about the fold line.
        # Horizontal fold
        if fold_direction == "x":
            locations_after_fold = set([dot for dot in dot_locations if dot[0] < fold_line])
            locations_to_be_folded = set(dot_locations) - locations_after_fold
            for location in locations_to_be_folded:
                locations_after_fold.add((fold_line - (location[0] - fold_line), location[1]))
        # Vertical fold
        else:
            locations_after_fold = set([dot for dot in dot_locations if dot[1] < fold_line])
            locations_to_be_folded = set(dot_locations) - locations_after_fold
            for location in locations_to_be_folded:
                locations_after_fold.add((location[0], fold_line - (location[1] - fold_line)))
        dot_locations = locations_after_fold

    # Create finished, folded matrix
    x_size = max([coord[0] for coord in dot_locations]) + 1
    y_size = max([coord[1] for coord in dot_locations]) + 1
    matrix = [["." for i in range(x_size)] for j in range(y_size)]
    # Populate it with the required dots
    for dot in dot_locations:
        matrix[dot[1]][dot[0]] = "#"
    return matrix


print("Part 1: " + str(part_one()))
print("Part 2:")
for line in part_two():
    for element in line:
        print(element, end=" ")
    print()
