# https://adventofcode.com/2024/day/2

def get_input():
    input = []
    with open("input", "r") as input_file:
        for line in input_file.readlines():
            input.append(line.strip())
    return input


class Counter:
    def __init__(self, target) -> None:
        self.count = 0
        self.target = target
        self.reverse_target = target[::-1]
        self.new_line()

    def process_char(self, char):
        # Forward
        if char == self.target[self.target_index]:
            self.target_index += 1
            if self.target_index == len(self.target):
                self.count += 1
                self.target_index = 0
        elif char == self.target[0]:
            self.target_index = 1
        else:
            self.target_index = 0

        # Backwards
        if char == self.reverse_target[self.reverse_target_index]:
            self.reverse_target_index += 1
            if self.reverse_target_index == len(self.reverse_target):
                self.count += 1
                self.reverse_target_index = 0
        elif char == self.reverse_target[0]:
            self.reverse_target_index = 1
        else:
            self.reverse_target_index = 0

    def new_line(self):
        self.target_index = 0
        self.reverse_target_index = 0


def count_vertical_occurrences(word_search, target):
    counter = Counter(target)
    for col_index in range(len(word_search[0])):
        for row in word_search:
            char = row[col_index]
            counter.process_char(char)
        counter.new_line()
    return counter.count


def count_horizontal_occurrences(word_search, target):
    counter = Counter(target)
    for row in word_search:
        for char in row:
            counter.process_char(char)
        counter.new_line()
    return counter.count


def diags_from_grid(grid, rev=False):
    # Source: https://stackoverflow.com/a/53035453
    def rotate(row, n):
        return row[n:] + row[:n]

    n = len(grid)
    _grid = [list(row) + [None]*(n-1) for row in grid]  # pad for rotation
    for diag in zip(*(rotate(_grid[i], (i, -i)[rev]) for i in range(n))):
        d = ''.join(filter(None, diag))
        yield d
    if not rev:
        yield from diags_from_grid(grid, rev=True)


def count_diagonal_occurrences(word_search, target):
    counter = Counter(target)
    for diagonal in diags_from_grid(word_search):
        for char in diagonal:
            counter.process_char(char)
        counter.new_line()
    return counter.count


def main():
    word_search = get_input()
    xmas_count = 0
    xmas_count += count_vertical_occurrences(word_search, "XMAS")
    xmas_count += count_horizontal_occurrences(word_search, "XMAS")
    xmas_count += count_diagonal_occurrences(word_search, "XMAS")
    print(xmas_count)


if __name__ == "__main__":
    main()
