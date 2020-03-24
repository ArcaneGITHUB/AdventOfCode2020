# Advent of Code day 2
#
# David Corcoran
# Pycharm
# Python 3.7.4


def run_intcode(intlist, instruction):
    if intlist[instruction] == 1:
        intlist[intlist[instruction+3]] = intlist[intlist[instruction+1]] + intlist[intlist[instruction+2]]
        return run_intcode(intlist, instruction + 4)
    elif intlist[instruction] == 2:
        intlist[intlist[instruction + 3]] = intlist[intlist[instruction + 1]] * intlist[intlist[instruction + 2]]
        return run_intcode(intlist, instruction + 4)
    elif intlist[instruction] == 99:
        return intlist[0]
    else:
        return 1


for noun in range(100):
    for verb in range(100):
        with open("input.txt", "r") as input_file:
            intcode_list = list(map(int, input_file.read().split(",")))
        intcode_list[1] = noun
        intcode_list[2] = verb
        if run_intcode(intcode_list, 0) == 19690720:
            print(noun)
            print(verb)
