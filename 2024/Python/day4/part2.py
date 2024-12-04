# https://adventofcode.com/2024/day/2

def get_input():
    input = []
    with open("input", "r") as input_file:
        for line in input_file.readlines():
            input.append(line.strip())
    return input


def get_diagonal_adjacents(grid, row_index, col_index):
    def _index_in_grid(grid, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            return True
        else:
            return False

    adjacents = []
    # Up Left
    if _index_in_grid(grid, row_index-1, col_index-1):
        adjacents.append(grid[row_index-1][col_index-1])
    # Up Right
    if _index_in_grid(grid, row_index-1, col_index+1):
        adjacents.append(grid[row_index-1][col_index+1])
    # Down Left
    if _index_in_grid(grid, row_index+1, col_index-1):
        adjacents.append(grid[row_index+1][col_index-1])
    # Down Right
    if _index_in_grid(grid, row_index+1, col_index+1):
        adjacents.append(grid[row_index+1][col_index+1])
    return adjacents


def main():
    word_search = get_input()
    xmas_count = 0
    for row_index, row in enumerate(word_search):
        for col_index, char in enumerate(row):
            if char != "A":  # A == Potential X-MAS center
                continue
            diagonal_adjacents = "".join(get_diagonal_adjacents(
                word_search, row_index, col_index))
            if diagonal_adjacents in ["MMSS", "SSMM", "MSMS", "SMSM"]:
                xmas_count += 1
    print(xmas_count)


if __name__ == "__main__":
    main()
