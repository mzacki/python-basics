def make_out_word(out, word):
    first_half = slice(0, len(out) // 2)
    second_half = slice(len(out) // 2, len(out))

    return out[first_half] + word + out[second_half]


print(make_out_word("<<>>", "item"))


def make_out_word2(out, word):
    first_half = out[:len(out) // 2]
    second_half = out[len(out) // 2:len(out)]

    return first_half + word + second_half


print(make_out_word2("<<>>", "item"))
