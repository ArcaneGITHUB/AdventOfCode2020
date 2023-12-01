# https://adventofcode.com/2021/day/1

with open("input", "r") as input_file:
    sonar_list = [int(num) for num in input_file]

depth_increases = 0
sonar_sum_list = []

for index, depth in enumerate(sonar_list):
    if index < (len(sonar_list) - 2):
        sonar_sum_list.append(depth + sonar_list[index+1] + sonar_list[index+2])

for index, depth in enumerate(sonar_sum_list):
    if index > 0 and depth > sonar_sum_list[index-1]:
        depth_increases += 1

print(depth_increases)
