# https://adventofcode.com/2021/day/6
# Given a list of fish, defined by the amount of days until they produce a new fish, find out how many fish there would
# be after 80 days.
# They produce new fish every 7 days, but a new fish takes 2 extra days.


# Input ages
from typing import List


def input_ages():
    with open("input", "r") as input_file:
        fish_ages = [int(age) for age in input_file.read().strip().split(",")]
    return fish_ages


class Fish:
    def __init__(self, age: int):
        self.age = age

    def get_older(self):
        if self.age == 0:
            self.age = 6
            return Fish(8)
        self.age -= 1


# Uses fish objects that produce new fish objects when they reach their "creation day"
def part_one(days: int):
    fishes = []
    for age in input_ages():
        new_fish = Fish(age)
        fishes.append(new_fish)

    for d in range(days):
        new_fishes = []
        for fish in fishes:
            new_fish = fish.get_older()
            if new_fish:
                new_fishes.append(new_fish)
        fishes.extend(new_fishes)
    return len(fishes)


# Make list of possible fish ages. Treat all fish of each age as a single value.
# Fish of age 0 get reset to age 6, and that number of "new" fish are added to day 8
def part_two(days: int):
    fishes_ages = [0] * 9
    for age in input_ages():
        fishes_ages[age] += 1

    for day in range(days):
        zero_day_count = fishes_ages[0]
        for age in range(9):
            if age != 8:
                fishes_ages[age] = fishes_ages[age + 1]
        fishes_ages[6] += zero_day_count
        fishes_ages[8] = zero_day_count
    return sum(fishes_ages)


print("Part 1: " + str(part_one(80)))
print("Part 2: " + str(part_two(256)))
