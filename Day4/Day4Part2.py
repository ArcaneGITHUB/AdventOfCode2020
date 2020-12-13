# https://adventofcode.com/2020/day/4
# Import a set of passports and check which ones are valid.
# Must include enough valid fields and those field must contain valid data.


def validate_fields(passport):
    passport = passport.replace("\n", " ")
    passport = passport.replace(":", " ").split()
    passport = {passport[i]: passport[i+1] for i in range(len(passport)-1)}

    # Birth year check
    if len(passport["byr"]) != 4 or int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False

    # Issue year check
    if len(passport["iyr"]) != 4 or int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False

    # Expiration year check
    if len(passport["eyr"]) != 4 or int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False

    # Height check
    if passport["hgt"][-2:] == "cm":
        if int(passport["hgt"][:-2]) < 150 or int(passport["hgt"][:-2]) > 193:
            return False
    elif int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76:
        return False

    # Hair colour check
    valid_hcl_charset = {"#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}
    if len(passport["hcl"]) != 7 or "#" not in passport["hcl"] or not set(passport["hcl"]).issubset(valid_hcl_charset):
        return False
    # Eye colour check

    valid_ecl_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if passport["ecl"] not in valid_ecl_values:
        return False

    # Passport ID check
    if len(passport["pid"]) != 9:
        return False

    return True


with open("input.txt", "r") as input_file:
    passport_list = input_file.read().split("\n\n")
    valid_passports = 0

    for passport in tuple(passport_list):
        fields = passport.count(":")
        if fields == 8 or (fields == 7 and "cid" not in passport):
            if validate_fields(passport):
                valid_passports += 1

    print(valid_passports)
