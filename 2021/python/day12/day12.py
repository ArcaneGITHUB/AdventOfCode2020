# https://adventofcode.com/2021/day/12
# Given a list of caves, some large(uppercase) and some small(lowercase) and connections between them. There is a
# "start" cave and an "end" cave.
# Part 1: Find the number of paths from start to end that visit small caves at most once each.
# Part 2: Find the number of paths from start to end that visit small caves at most once each, however a single small
# cave may be visited twice.


# Input the caves to a dictionary ("graph")
def get_graph_dictionary() -> dict:
    with open("input", "r") as input_file:
        graph = {}
        connections_list = [connection.split("-") for connection in input_file.read().strip().split("\n")]
        for connection in connections_list:
            # Add connection to cave, create cave if it doesn't exist yet
            if connection[0] in graph:
                graph[connection[0]].append(connection[1])
            else:
                graph[connection[0]] = [connection[1]]
            # Add connection to cave, create cave if it doesn't exist yet
            if connection[1] in graph:
                graph[connection[1]].append(connection[0])
            else:
                graph[connection[1]] = [connection[0]]
    return graph


# Find valid paths to end from given cave
def find_paths_to_end(graph_dict: dict, current_cave: str, path: list):
    path.append(current_cave)
    # Check if path is valid
    if current_cave == "end":
        return 1
    # Recursively call function for each valid option. If no valid options, reached dead end and return 0.
    valid_options = [node for node in graph_dict[current_cave] if not(node.islower() and node in path)]
    if len(valid_options):
        valid_paths = 0
        for node in valid_options:
            valid_paths += find_paths_to_end(graph_dict, node, path.copy())
        return valid_paths
    else:
        return 0


# Find valid paths to end from given node, can visit a single small cave twice.
def find_paths_to_end_with_double_visit(graph_dict: dict, current_cave: str, path: list):
    path.append(current_cave)
    # Check if path is valid
    if current_cave == "end":
        return 1
    # Find valid options from this node
    valid_options = []
    for potential_cave in graph_dict[current_cave]:
        if potential_cave != "start":
            # If cave is large or hasn't been visited yet, record it as valid
            if potential_cave.isupper() or potential_cave not in path:
                valid_options.append(potential_cave)
            # If this small cave has been visited, but no small cave has been visited twice, record it as valid.
            elif not any(True if cave.islower() and path.count(cave) > 1 else False for cave in path):
                valid_options.append(potential_cave)
    # Recursively call function for each valid option. If no valid options, reached dead end and return 0.
    if len(valid_options):
        valid_paths = 0
        for cave in valid_options:
            valid_paths += find_paths_to_end_with_double_visit(graph_dict, cave, path.copy())
        return valid_paths
    else:
        return 0


def part_one():
    return find_paths_to_end(get_graph_dictionary(), "start", [])


def part_two():
    return find_paths_to_end_with_double_visit(get_graph_dictionary(), "start", [])


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
