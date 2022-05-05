def last2(str_input):
    last2chars = str_input[len(str_input) - 2:]
    counter = 0
    for i in range(0, len(str_input) - 2):
        if str_input[i: i + 2] == last2chars:
            counter = counter + 1
    return counter



