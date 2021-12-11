# https://adventofcode.com/2021/day/10
# Given a list of lines of paired opening and closing brackets. All lines are either corrupted ( have an
# incorrect closing char) or incomplete (all opening chars do not have a paired closing char)
#
# Part 1: Find the first corrupted character in all corrupted lines, score it and return the sum of the scores
# Part 2: Find the missing "closing" strings for each incomplete line, score them and return the middle score.


# Reads the input file and returns its lines as a list of strings.
def get_subsystem_lines():
    with open("input", "r") as input_file:
        subsystem_lines = input_file.read().strip().split("\n")
    return subsystem_lines


# If line is corrupt, returns the first corrupted characters.
# If line is incomplete, returns the unmatched characters.
def validate_line(line):
    stack = []
    opener_closer_dict = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    for char in line:
        if char in opener_closer_dict.keys():
            stack.append(char)
        else:
            if char == opener_closer_dict[stack[-1]]:
                stack.pop(-1)
            else:
                return char
    return stack


# # Takes a list of unmatched openers and returns the score of the matching closers
# def get_closers_score(openers_list):
#     score = 0
#     char_score_dict = {
#         '(': 1,
#         '[': 2,
#         '{': 3,
#         '<': 4
#     }
#     for closer in reversed(openers_list):
#         score *= 5
#         score += char_score_dict[closer]
#     return score


# For each line in a list, find the first corrupt character, if any.
# Return the sum of the "scores" of all corrupt characters.
def part_one():
    syntax_error_score = 0
    score_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    for line in get_subsystem_lines():
        result = validate_line(line)
        if type(result) is str:
            syntax_error_score += score_dict[result]
    return syntax_error_score


# Find the "closers" needed to complete each unfinished line and calculate their score. Return the middle score.
def part_two():
    scores = []
    for line in get_subsystem_lines():
        result = validate_line(line)
        if type(result) is list:
            # Add openers to stack and remove matched pairs
            stack = []
            opener_closer_dict = {
                '(': ')',
                '[': ']',
                '{': '}',
                '<': '>'
            }
            for char in line:
                if char in opener_closer_dict.keys():
                    stack.append(char)
                else:
                    stack.pop(-1)
            # Find score
            char_score_dict = {
                '(': 1,
                '[': 2,
                '{': 3,
                '<': 4
            }
            score = 0
            for closer in reversed(stack):
                score *= 5
                score += char_score_dict[closer]
            scores.append(score)
    return sorted(scores)[int(len(scores)/2)]


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
