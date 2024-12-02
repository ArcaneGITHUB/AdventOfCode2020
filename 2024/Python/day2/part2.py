# https://adventofcode.com/2024/day/2#part2

def get_input():
    input = []
    with open("input", "r") as input_file:
        for line in input_file:
            levels = list(map(int, line.split()))
            input.append(levels)
    return input


def is_valid_diff(current, previous, ascending):
    diff = current - previous
    if not 1 <= abs(diff) <= 3:
        return False
    if ascending == True and not diff > 0:
        return False
    elif ascending == False and not diff < 0:
        return False
    return True


def is_safe(report):
    ascending = True if (report[1] - report[0] > 0) else False
    for i in range(1, len(report)):
        if not is_valid_diff(report[i], report[i-1], ascending):
            return False
    return True


def is_safe_with_tolerance(report):
    for i in range(len(report)):  # ew sorry
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False


def main():
    safe = 0
    for report in get_input():
        if is_safe_with_tolerance(report):
            safe += 1
    print(safe)


if __name__ == "__main__":
    main()
