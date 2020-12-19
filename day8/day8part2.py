# https://adventofcode.com/2020/day/8
# Follow boot code as given in the input file. Change a single instruction to fix an infinite loop.

import copy


def run_bootcode(bootcode):
    accumulator = 0
    ran_instructions = []
    position = 0

    while position <= len(bootcode):
        ran_instructions.append(position)
        instruction = bootcode[position][0]
        argument = int(bootcode[position][1])

        if instruction == "acc":
            accumulator += argument
        elif instruction == "jmp":
            position += argument - 1
        position += 1
        if position in ran_instructions:
            return
        elif position > len(bootcode) - 1:
            print(accumulator)
            return


with open("input.txt", "r") as instruction_file:
    instruction_list = [line.strip() for line in instruction_file]
    instruction_list = [instruction.split() for instruction in instruction_list]

    for reverse_position in range(len(instruction_list)-1, 0, -1):
        instruction = instruction_list[reverse_position][0]
        instruction_list_copy = copy.deepcopy(instruction_list)
        if instruction == "jmp":
            instruction_list_copy[reverse_position][0] = "nop"
        elif instruction == "nop":
            instruction_list_copy[reverse_position][0] = "jmp"
        run_bootcode(instruction_list_copy)
