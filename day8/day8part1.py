# https://adventofcode.com/2020/day/8
# Follow boot code as given in the input file. Print the accumulator's value before any instruction is repeated.


with open("input.txt", "r") as instruction_file:
    instruction_list = [line.strip() for line in instruction_file]
    instruction_list = [instruction.split() for instruction in instruction_list]
    accumulator = 0
    ran_instructions = []
    position = 0

    while position <= len(instruction_list):
        ran_instructions.append(position)
        instruction = instruction_list[position][0]
        argument = int(instruction_list[position][1])

        if instruction == "acc":
            accumulator += argument
        elif instruction == "jmp":
            position += argument-1
        position += 1
        if position in ran_instructions:
            print(accumulator)
            break
