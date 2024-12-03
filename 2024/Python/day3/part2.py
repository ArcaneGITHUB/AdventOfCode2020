# https://adventofcode.com/2024/day/2

import re


def get_input():
    input = []
    with open("input", "r") as input_file:
        input = input_file.read().strip()
    return input


def main():
    input = get_input()
    valid_command_pattern = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
    commands = re.findall(valid_command_pattern, input)
    total = 0
    enabled = True
    for command in commands:
        if command == "do()":
            enabled = True
        elif command == "don't()":
            enabled = False
        elif enabled:
            num_pattern = r"([0-9]+),([0-9]+)"
            search = re.search(num_pattern, command)
            num_one = int(search.group(1))
            num_two = int(search.group(2))
            total += num_one * num_two
    print(total)


if __name__ == "__main__":
    main()
