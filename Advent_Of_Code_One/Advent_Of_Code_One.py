

def fuel_requirement(mass):
    extra_fuel = (mass // 3) - 2
    if extra_fuel > 0:
        extra_fuel += fuel_requirement(extra_fuel)
    else:
        return 0
    return extra_fuel


input_file = open("input.txt", "r")
module_list = input_file.read().splitlines()
fuel = 0

for module in module_list:
    fuel += fuel_requirement(int(module))

print(fuel)