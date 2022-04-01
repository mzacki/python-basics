# * Constraints:
# * - data must be sorted
# * - works for integers > 0 with max one duplicate
# * - uses Gauss formula
# * - time complexity equals O(n) - even better than alternatives:
# * -- iteration within iteration: O(n) * O(n) = n^2
# * -- iteration with binary search: O(n * log n)

def duplicate_search(array):
    # from the Gauss formula
    # counting sum of numbers from 1 to n...
    last_number = array[len(array) - 1]
    expected_sum = last_number * (last_number + 1) / 2

    actual_sum = 0
    for i in range(0, len(array)):
        actual_sum = actual_sum + array[i]

    return actual_sum - expected_sum
