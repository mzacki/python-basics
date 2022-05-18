def string_match(a, b):
    counter = 0
    if len(a) >= len(b):
        for i in range(len(b) - 1):
            if a[i] == b[i] and a[i+1] == b[i+1]:
                counter = counter + 1
    else:
        for i in range(len(a) - 1):
            if a[i] == b[i] and a[i+1] == b[i+1]:
                counter = counter + 1

    return counter
