# https://adventofcode.com/2024/day/2

def get_input():
    input = []
    with open("input", "r") as input_file:
        for line in input_file:
            levels = list(map(int, line.split()))
            input.append(levels)
    return input


def is_safe(report):
    previous = report[0]
    total_difference = 0
    for level in report[1:]:
        diff = level - previous
        if not 1 <= abs(diff) <= 3:
            return False
        if total_difference > 0 and not diff > 0:
            return False
        elif total_difference < 0 and not diff < 0:
            return False
        total_difference += diff
        previous = level
    return True


def main():
    safe = 0
    for report in get_input():
        safe += 1 if is_safe(report) else 0
    print(safe)


if __name__ == "__main__":
    main()
