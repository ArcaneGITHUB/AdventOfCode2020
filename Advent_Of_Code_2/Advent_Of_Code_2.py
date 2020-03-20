

def run_as_intcode(intlist, instruction):
    if intlist[instruction] == 1:
        intlist[intlist[instruction+3]] = intlist[intlist[instruction+1]] + intlist[intlist[instruction+2]]
    elif intlist[instruction] == 2:
        intlist[intlist[instruction + 3]] = intlist[intlist[instruction + 1]] * intlist[intlist[instruction + 2]]
    elif intlist[instruction] == 99:
        print("99 found. Program ending.")
        return 0
    else:
        print("Unknown code found. Program ending.")
        return 1

    instruction += 4
    run_as_intcode(intlist, instruction)


with open("input.txt", "r") as input_file:
    intcode_list = input_file.read().split(",")
    print(intcode_list)
run_as_intcode(intcode_list, 0)
