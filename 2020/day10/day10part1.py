# https://adventofcode.com/2020/day/10
# Given a list of power adapters, find the cumulative "joltage" difference between subsequent adapters.
# An adapter is identified by it's joltage output.
# All adapters must be used an each adapter can only accept inputs within 3 "jolts" of it's output.

with open("input.txt", "r") as adapter_outputs:
    adapter_outputs = adapter_outputs.read().splitlines()
adapter_outputs = sorted([int(joltage) for joltage in adapter_outputs])
adapter_outputs.insert(0, 0) # Account for socket voltage
jolt_diffs = {1: 0, 3: 1}   # Always an additional gap of 3 between final adapter and device
for index, adapter in enumerate(adapter_outputs[:-1]):
    next_adapter = adapter_outputs[index+1]
    next_difference = next_adapter - adapter
    if next_difference == 1:
        jolt_diffs[1] += 1
    elif next_difference == 3:
        jolt_diffs[3] += 1

print(jolt_diffs[1] * jolt_diffs[3])
