# Advent of Code day 4
#
# David Corcoran
# Pycharm
# Python 3.7.4

valid_count = 0
for password in range(145852, 616942):
    password = str(password)
    adjacent_digits = False
    increasing_digits = False
    for char in range(len(password[1:])):
        if password[char] == password[char + 1]:                # Checks for any pair of the same number
            adjacent_digits = True
        if int(password[char]) > int(password[char + 1]):       # Checks for any DECREASING numbers
            increasing_digits = True
    if adjacent_digits and not increasing_digits:
        valid_count += 1

print(valid_count)
