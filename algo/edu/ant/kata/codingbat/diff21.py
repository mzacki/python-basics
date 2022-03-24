def diff21(n):
    abs_diff = abs(n - 21)

    if n > 21:
        return 2 * abs_diff
    else:
        return abs_diff
