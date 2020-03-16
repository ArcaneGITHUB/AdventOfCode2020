

def fuel_requirement(mass):
    extra_fuel = (mass // 3) - 2
    if extra_fuel > 0:
        return extra_fuel + fuel_requirement(extra_fuel)
    else:
        return 0


with open("input.txt", "r") as input_file:
    module_list = input_file.read().splitlines()
total_fuel = 0

for module in module_list:
    total_fuel += fuel_requirement(int(module))

print(total_fuel)
