def pos_neg(a, b, negative):

    if negative:
        return negative and a < 0 and b < 0

    return (a < 0 and b > 0) or (a > 0 and b < 0)

