with open("input.txt", "r") as input_file:
    wires = input_file.read().splitlines()
    wire_one = wires[0].split(",")
    wire_two = wires[1].split(",")
    print(wire_one)
    print(wire_two)

wire_map