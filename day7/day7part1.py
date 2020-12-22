# https://adventofcode.com/2020/day/7
# Every type of bag must contain specific quantities of other specific coloured bags.
# From a list of these requirements, find out how many bags allow you to carry a "shiny gold" bag at some point.


def find_parents(child_bag):
    for parent in bags_dict:
        contents = bags_dict[parent]
        if child_bag in contents:
            find_parents(parent)
            confirmed_bags.add(parent)
    return


with open("input.txt", "r") as bags:
    bags = bags.read().split(".\n")[:-1]

bags_dict = {}
for bag in bags:
    bag = bag.replace(" bags", "").replace(" bag", "")  # Remove unnecessary text
    bag = bag.split("contain ")
    bags_dict[bag[0].strip()] = bag[1]
confirmed_bags = set()
find_parents("shiny gold")
print("Total: ", len(confirmed_bags))
