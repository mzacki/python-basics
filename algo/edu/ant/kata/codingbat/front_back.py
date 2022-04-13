def front_back(str_input):
    if len(str_input) <= 1:
        return str_input
    first = str_input[0]
    last = str_input[len(str_input) - 1]
    return last + str_input[1: - 1] + first
