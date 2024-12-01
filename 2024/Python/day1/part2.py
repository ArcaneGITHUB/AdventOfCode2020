# https://adventofcode.com/2024/day/1#part2

from collections import defaultdict


def get_input():
    with open("input", "r") as input_file:
        left = []
        right = defaultdict(int)
        for line in input_file:
            line = line.split()
            left.append(int(line[0]))
            right[int(line[1])] += 1
        return left, right


def main():
    left, right = get_input()
    similarity = 0
    for num in left:
        similarity += num * right[num]
    print(similarity)


if __name__ == "__main__":
    main()
