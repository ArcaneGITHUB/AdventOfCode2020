sum_goal = 2020

with open("input.txt", "r") as input_file:
    input_list = [int(num) for num in input_file.read().splitlines()]     # Convert strings to ints
    input_list.sort()

    success = False
    while not success:
        num = input_list.pop(0)
        for second_num in input_list:
            sum = num + second_num
            if (2020 - sum) in input_list:
                print(num * second_num * (2020-sum))
                success = True
