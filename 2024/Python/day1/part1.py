# https://adventofcode.com/2024/day/1

def get_input():
    with open("input", "r") as input_file:
        left = []
        right = []
        for line in input_file:
            line = line.split()
            left.append(int(line[0]))
            right.append(int(line[1]))
        return left, right


def main():
    left, right = get_input()
    left.sort()
    right.sort()
    total_difference = 0
    for index in range(len(left)):
        total_difference += abs(left[index] - right[index])
    print(total_difference)


if __name__ == "__main__":
    main()
