with open("input.txt", "r") as input_file:
    correct_passwords = 0

    for line in input_file:
        line = line.replace(": ", " ").replace("-", " ")    # Converts gaps between data to spaces
        line = line.split(" ")  # Splits string into a list of the data in string form

        first_position = int(line[0])
        second_position = int(line[1])
        target_char = line[2]
        password = line[3]

        first_char = password[(first_position - 1)]
        second_char = password[(second_position - 1)]

        if first_char == target_char or second_char == target_char:
            if first_char != second_char:
                correct_passwords += 1

    print(correct_passwords)
