# https://adventofcode.com/2020/day/9
# Given a list of numbers, find out which number is not the sum of 2 of the previous 25 numbers.
# Then, find the contiguous set of numbers which adds to this number.
# Find the sum of the smallest and largest number of the set.

with open("input.txt", "r") as num_list:
    num_list = num_list.read().splitlines()
num_list = [int(num) for num in num_list]
preamble = 25
target_num = None

for position, num in enumerate(num_list[preamble:]):
    previous_25 = num_list[position: position+preamble]
    sum_found = False
    for first_sum_num in previous_25:
        if (num - first_sum_num) in previous_25:
            sum_found = True
    if not sum_found:
        target_num = num

for index, num in enumerate(num_list):
    total = 0
    current_position = index
    while total < target_num:
        total += num_list[current_position]
        if total == target_num and current_position > index:
            sublist = num_list[index:current_position+1]
            print(min(sublist) + max(sublist))
        current_position += 1
