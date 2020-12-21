# https://adventofcode.com/2020/day/10
# Given a list of power adapters, find the cumulative "joltage" difference between subsequent adapters.
# An adapter is identified by it's joltage output.
# All adapters must be used an each adapter can only accept inputs within 3 "jolts" of it's output.

# I used help from reddit to solve this one
# https://old.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/
# I had not come across memoization or the tribonacci sequence prior to this.
# I chose the tribonacci method for this answer.


with open("input.txt", "r+") as adapters:
    adapters = adapters.read().splitlines()
adapters = sorted([int(joltage) for joltage in adapters])
adapters.append(max(adapters) + 3)

answers = {0: 1}
for adapter in adapters:
    answers[adapter] = answers.get(adapter - 1, 0) + answers.get(adapter - 2, 0) + answers.get(adapter - 3, 0)
print("Answer: ", answers[adapters[-1]])
