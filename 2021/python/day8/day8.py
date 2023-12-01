# https://adventofcode.com/2021/day/8
# Given a list of unique segments combinations from a scrambled seven digit display and a set of output values from
# that display.
# Part 1: Find the count of all digits that have unique segment counts when displayed.
# Part 2: Unscramble each set of signal patterns and sum all the decoded output values.
#
# Example of digit 8 on seven segment display:
#
#     ####
#    #    #
#    #    #
#     ####
#    #    #
#    #    #
#    #    #
#     ####
#
# 0, 6, 9 = 6 segments
# 1 = 2 segments
# 2, 3, 5 = 5 segments
# 4 = 4 segments
# 0, 6, 9 = 6 segments
# 7 = 3 segments
# 8 = 7 segments

def get_display_data():
    with open("input", "r") as input_file:
        display_data_list = input_file.read().strip().split("\n")
        signal_patterns_list = [x.split(" | ")[0].split(" ") for x in display_data_list]
        output_values = [x.split(" | ")[1].split(" ") for x in display_data_list]
    return signal_patterns_list, output_values


def part_one():
    # Simple segments = segment counts that correspond to only one number on a seven digit display
    simple_segment_counts = [2, 3, 4, 7]
    simple_digit_counter = 0
    signal_patterns_list, output_values_list = get_display_data()
    for output_values in output_values_list:
        for digit in output_values:
            if len(digit) in simple_segment_counts:
                simple_digit_counter += 1
    return simple_digit_counter


def part_two():
    signal_patterns_list, output_values_list = get_display_data()
    total = 0
    for index, signal_patterns in enumerate(signal_patterns_list):
        # Possible outputs of a seven segment display.
        digits = {
            "0": [],
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": []
        }

        # Adds the segments of simple digits to their corresponding digit
        for signal_pattern in signal_patterns:
            signal_pattern = list(signal_pattern)
            if len(signal_pattern) == 2:
                digits["1"].extend(signal_pattern)
            elif len(signal_pattern) == 4:
                digits["4"].extend(signal_pattern)
            elif len(signal_pattern) == 3:
                digits["7"].extend(signal_pattern)
            elif len(signal_pattern) == 7:
                digits["8"].extend(signal_pattern)

        # Adds the segments of the more complex digits to their corresponding digit
        for signal_pattern in signal_patterns:
            signal_pattern = list(signal_pattern)
            if len(signal_pattern) == 6:    # 0, 6, 9 have six segments
                # 9 = 8 - (a segment not in 4)
                if all(segment in signal_pattern for segment in digits["4"]):
                    digits["9"] = signal_pattern
                # Only 6 shares a single segment with 1
                elif not all(segment in signal_pattern for segment in digits["1"]):
                    digits["6"] = signal_pattern
                else:
                    digits["0"] = signal_pattern
            # 2, 3, 5 have 5 segments
            if len(signal_pattern) == 5:
                # Only 3 has both segments of 1
                if all(segment in signal_pattern for segment in digits["1"]):
                    digits["3"] = signal_pattern
                # Only 5 has the L shape from 4
                elif all(segment in signal_pattern for segment in list(set(digits["4"]) - set(digits["1"]))):
                    digits["5"] = signal_pattern
                else:
                    digits["2"] = signal_pattern
        # Use decoded digits to get the output value of the entry
        output_value = ""
        for number in output_values_list[index]:
            for key, value in digits.items():
                if set(number) == set(value):
                    output_value += key
        total += int(output_value)
    return total


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
