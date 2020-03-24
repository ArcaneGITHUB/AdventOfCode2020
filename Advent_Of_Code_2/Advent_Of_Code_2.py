# Advent of Code day 2
#
# David Corcoran
# Pycharm
# Python 3.7.4


def run_intcode(intlist, instruction):
    if intlist[instruction] == 1:
        intlist[intlist[instruction+3]] = intlist[intlist[instruction+1]] + intlist[intlist[instruction+2]]
        run_intcode(intlist, instruction + 4)
    elif intlist[instruction] == 2:
        intlist[intlist[instruction + 3]] = intlist[intlist[instruction + 1]] * intlist[intlist[instruction + 2]]
        run_intcode(intlist, instruction + 4)
    elif intlist[instruction] == 99:
        print(intlist[0])
        print("99 found. Program ending.")
        return 0
    else:
        print("Unknown code found. Program ending.")
        return 1


with open("input.txt", "r") as input_file:
    intcode_list = input_file.read().split(",")
    intcode_list = list(map(int, intcode_list))
run_intcode(intcode_list, 0)
