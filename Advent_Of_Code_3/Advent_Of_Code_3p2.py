
with open("input.txt", "r") as input_file:
    wires = input_file.read().splitlines()
    wire_one = wires[0].split(",")
    wire_two = wires[1].split(",")


# Takes vectors from a list and returns a list of all co-ordinates covered by these vectors.
def plot(wire):
    coordinate_list = []
    current_location = (0, 0)
    for section in wire:
        direction = section[0]
        section = int(section[1:])
        if direction == "U":
            for y in range(1, section+1):
                coordinate_list.append((current_location[0], current_location[1]+y))
        elif direction == "D":
            for y in range(1, section+1):
                coordinate_list.append((current_location[0], current_location[1]-y))
        elif direction == "R":
            for x in range(1, section+1):
                coordinate_list.append((current_location[0]+x, current_location[1]))
        elif direction == "L":
            for x in range(1, section+1):
                coordinate_list.append((current_location[0]-x, current_location[1]))
        current_location = coordinate_list[-1]
    return coordinate_list


def manhattan_distance(point_one, point_two):
    return abs(point_two[0] - point_one[0]) + abs(point_two[1] - point_one[1])


wire_one = plot(wire_one)
wire_two = plot(wire_two)

# Finds the lowest manhattan distance of all the wire intersections and prints the lowest.
lowest_distance = 0
for point in set(wire_one).intersection(wire_two):
    distance = manhattan_distance((0, 0), point)
    if lowest_distance == 0:
        lowest_distance = distance
    elif distance < lowest_distance:
        lowest_distance = distance
print(lowest_distance)
