# https://adventofcode.com/2020/day/1
# Find two entries from a list of numbers that sum to 2020, then multiply those together and output.

sum_goal = 2020

with open("input.txt", "r") as input_file:
    input_list = [int(num) for num in input_file]   # Convert strings to ints

success = False
while not success and input_list:
    num = input_list.pop(0)
    if (2020 - num) in input_list:
        print(num * (2020-num))
        success = True
