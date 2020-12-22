# https://adventofcode.com/2020/day/6
# Given a list of groups' responses to a form, find the no. of shared questions answered per group
# and calculate the sum of all groups answers.

from functools import reduce

with open("input.txt", "r") as groups:
    groups = groups.read().split("\n\n")
total_answers = []
for group in groups:
    shared_answers = set(group.split()[0])
    for person in group.split():
        shared_answers = shared_answers.intersection(set(person))
    total_answers.append(len(shared_answers))
total_answers = reduce(lambda a, b: a + b, total_answers)
print(total_answers)
