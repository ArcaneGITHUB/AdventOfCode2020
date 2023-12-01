# https://adventofcode.com/2021/day/3

# Input numbers into list
numbers = []
with open("input", "r") as input_file:
    for number in input_file:
        numbers.append(number.strip())

# Total the amount of "1"s in each position for all numbers in the list
positions_counter = [0] * len(numbers[0])
for number in numbers:
    for position in range(len(positions_counter)):
        if number[position] == "1":
            positions_counter[position] += 1

# Calculate the gamma and epsilon rates.
# If more 1s than 0s, gamma = 1 & epsilon = 0
# If more 0s than 1s, gamma = 0 & epsilon = 1
gamma_rate = ""
epsilon_rate = ""
for position in positions_counter:
    if position > (len(numbers)/2):
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

# Convert binary to int
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

# Find and display power consumption
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
