# https://adventofcode.com/2021/day/2

with open("input", "r") as input_file:
    instruction_list = []
    for instruction in input_file:
        instruction = instruction.split()
        instruction[1] = int(instruction[1])
        instruction_list.append(instruction)


# Test input
# instruction_list = [("forward", 5),
#                     ("down", 5),
#                     ("forward", 8),
#                     ("up", 3),
#                     ("down", 8),
#                     ("forward", 2)]

horizontal = 0
depth = 0
aim = 0

for instruction in instruction_list:
    if instruction[0] == "forward":
        horizontal += instruction[1]
        depth += aim * instruction[1]
    elif instruction[0] == "down":
        aim += instruction[1]
    elif instruction[0] == "up":
        aim -= instruction[1]

print(horizontal * depth)
