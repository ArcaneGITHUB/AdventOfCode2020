input_file = open("input.txt", "r")
module_list = input_file.read().splitlines()
fuel_list = []
for module in module_list:
    module = int(module)
    fuel_list.append(int(module/3)-2)
print(sum(fuel_list))
