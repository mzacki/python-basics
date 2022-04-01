from edu.ant.algo.search.duplicate.one_duplicate_sorted_numbers import duplicate_search


def test():
    input1 = [1, 2, 3, 4, 5, 5]
    input2 = [1, 2, 3, 4, 5]

    assert duplicate_search(input1) == 5
    assert duplicate_search(input2) == 0
