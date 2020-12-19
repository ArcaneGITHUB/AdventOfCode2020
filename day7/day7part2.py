# https://adventofcode.com/2020/day/7
# Every type of bag must contain specific quantities of other specific coloured bags.
# From a list of these requirements, find out how many bags must be contained within a "shiny gold" bag.


def add_children(parent_bag):
    parent_contents = bags_dict[parent_bag]
    if parent_contents[0] == "no other":
        return
    else:
        for child in parent_contents:
            name = child[2:]
            count = int(child[0])
            if name in children_count:
                children_count[name] += count   # First char is the frequency, 2nd character onwards is the bag name
            else:
                children_count[name] = count
            for x in range(count):
                add_children(name)
        return


with open("input.txt", "r") as bags:
    bags_dict = {}
    for bag in bags.read().split(".\n")[:-1]:
        bag = bag.replace(" bags", "").replace(" bag", "")  # Remove unnecessary text
        bag = bag.split("contain ")
        bags_dict[bag[0].strip()] = bag[1].split(", ")
    children_count = {}
    add_children("shiny gold")
    print(sum(children_count.values()))
