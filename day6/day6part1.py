# https://adventofcode.com/2020/day/6
# Given a list of groups' responses to a form, find the no. of unique questions answered per group
# and calculate the sum of all groups answers.

from functools import reduce

with open("input.txt", "r") as groups:
    groups = groups.read().split("\n\n")
    total_answers = []
    for group in groups:
        group_answers = set()
        for person in group.split():
            person = person.strip()
            for answer in person:
                group_answers.add(answer)
        total_answers.append(len(group_answers))
    total_answers = reduce(lambda a, b: a + b, total_answers)
    print(total_answers)
