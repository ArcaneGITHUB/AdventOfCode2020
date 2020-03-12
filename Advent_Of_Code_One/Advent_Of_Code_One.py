input_file = open("input.txt", "r")
module_list = input_file.read().splitlines()
fuel = 0
for module in module_list:
    fuel += (int(module)//3)-2
print(fuel)
