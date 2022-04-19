def front_times(str_input, n):
    if len(str_input) <= 3:
        return str_input * n

    return str_input[:3] * n
