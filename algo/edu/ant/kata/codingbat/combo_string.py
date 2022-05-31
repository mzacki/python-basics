def combo_string(a, b):
    if len(a) >= len(b):
        return b + a + b
    else:
        return a + b + a


def combo_string2(a, b):
    return b + a + b if len(a) >= len(b) else a + b + a

