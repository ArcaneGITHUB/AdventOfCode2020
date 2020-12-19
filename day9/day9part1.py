# https://adventofcode.com/2020/day/9
# Given a list of numbers, find out which number is not the sum of 2 of the previous 25 numbers.

with open("input.txt", "r") as num_list:
    num_list = num_list.read().splitlines()
    num_list = [int(num) for num in num_list]
    preamble = 25

    for position, num in enumerate(num_list[preamble:]):
        previous_25 = num_list[position: position+preamble]
        sum_found = False
        for first_sum_num in previous_25:
            if (num - first_sum_num) in previous_25:
                sum_found = True
        if not sum_found:
            print("Num without sum: ", num)
