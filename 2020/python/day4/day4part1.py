# https://adventofcode.com/2020/day/4
# Import a set of passports and check which ones are valid.
# Must include 7 valid fields plus an optional 8th.

with open("input.txt", "r") as input_file:
    passport_list = input_file.read().split("\n\n")
valid_passports = 0

for passport in passport_list:
    fields = passport.count(":")
    if fields == 8 or (fields == 7 and "cid" not in passport):
        valid_passports += 1

print(valid_passports)
