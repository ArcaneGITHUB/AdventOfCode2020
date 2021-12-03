# https://adventofcode.com/2021/day/3


# Determine the most common value in a position, then remove list items without that value in the position
# Recursively call until only one value remains.
def find_o2_rating(numbers, index):
    # Find most common value for current index
    count = 0
    for number in numbers:
        if number[index] == "1":
            count += 1

    # Set most common value as target
    if count >= (len(numbers) / 2):
        target = "1"
    else:
        target = "0"

    # Keep only values that have the target number at the correct index.
    # If only one value remains, return it. Otherwise, call this function with the next index.
    numbers = [num for num in numbers if num[index] == target]
    if len(numbers) == 1:
        return numbers
    else:
        return find_o2_rating(numbers, index + 1)


# Determine the least common value in a position, then remove list items without that value in the position
# Recursively call until only one value remains.
def find_co2_rating(numbers, index):
    # Find most common value for current index
    count = 0
    for number in numbers:
        if number[index] == "1":
            count += 1

    # Set least common value as target
    if count >= (len(numbers) / 2):
        target = "0"
    else:
        target = "1"

    # Keep only values that have the target number at the correct index.
    # If only one value remains, return it. Otherwise, call this function with the next index.
    numbers = [num for num in numbers if num[index] == target]
    if len(numbers) == 1:
        return numbers
    else:
        return find_co2_rating(numbers, index + 1)


def solution():
    # Input file into list
    numbers = []
    with open("input", "r") as input_file:
        for number in input_file:
            numbers.append(number.strip())

    # find ratings and convert from binary to int
    o2_rating = int(find_o2_rating(numbers, 0)[0], 2)
    co2_rating = int(find_co2_rating(numbers, 0)[0], 2)

    return o2_rating * co2_rating


print(solution())
