import random


# for given int n
# return all int values from 1 to n (inclusive)
# in random order


def get_randomized(n):
    initial_array = [0] * n

    for i in range(n):
        initial_array[i] = i + 1
    # or list(array(range(1, n+1)
    return shuffle(initial_array)


def shuffle(array):

    for i in range(len(array)):
        # shuffles only with subsequent indices - which have not been shuffled before
        new_index = random.randint(i, len(array) - 1)
        swap(array, i, new_index)

    return array


def swap(array, i, new_index):
    temp = array[i]
    array[i] = array[new_index]
    array[new_index] = temp

    return array


result = get_randomized(5)
print(result)