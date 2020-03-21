import numpy as np

with open("input.txt", "r") as input_file:
    wires = input_file.read().splitlines()
    wire_one = wires[0].split(",")
    wire_two = wires[1].split(",")
    print(wire_one)
    print(wire_two)

wire_map = np.full((10000, 10000), 0)
print(type(wire_map))

twodarraytest = np.array([[1, 2, 3], [4, 5, 6]])
print(twodarraytest[0:2])
