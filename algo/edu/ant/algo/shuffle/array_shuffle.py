import random


# for given int n
# return all int values from 1 to n (inclusive)
# in random order

def get_randomized(n):
    initial_array = [0] * n

    for i in range(0, n):
        initial_array[i] = i + 1

    # or just: list(range(1, n + 1))

    return shuffle(initial_array)


def shuffle(array):
    # shuffles with any index - even if it had been shuffled before
    for i in range(0, len(array)):
        new_index = random.randint(0, len(array) - 1)
        swap(array, i, new_index)

    return array


def swap(array, i, new_index):
    temp = array[i]
    array[i] = array[new_index]
    array[new_index] = temp

    return array


result = get_randomized(5)
print(result)

