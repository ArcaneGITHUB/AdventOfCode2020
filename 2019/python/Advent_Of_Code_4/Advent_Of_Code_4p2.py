# Advent of Code day 4
#
# David Corcoran
# Pycharm
# Python 3.7.4
# Not proud of this solution, but it works. Could have also brute forced it @juuiko ;)

valid_count = 0
for password in range(145852, 616942):
    password = str(password)
    double_digits = False
    increasing_digits = False
    matching_digit_count = 0
    for char in range(len(password[1:])):
        if password[char] == password[char + 1]:                # Checks for any pair of the same number
            matching_digit_count += 1
        elif matching_digit_count == 1:
            double_digits = True
        else:
            matching_digit_count = 0
        if int(password[char]) > int(password[char + 1]):       # Checks for any DECREASING numbers
            increasing_digits = True
    if matching_digit_count == 1:
        double_digits = True
    if double_digits and not increasing_digits:
        valid_count += 1

print(valid_count)
