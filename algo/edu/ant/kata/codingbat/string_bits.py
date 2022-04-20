# Given a string, return a new string made of every other char starting with the first
# the key is to use step as third parameter of slice:
# https://stackoverflow.com/questions/509211/understanding-slicing
def string_bits(str_input):
    return str_input[::2]
