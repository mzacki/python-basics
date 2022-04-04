def create_fibo_series(last_n):
    sequence = [0] * last_n

    sequence[0] = 0

    if last_n > 1:
        sequence[1] = 1

    for i in range(2, last_n):
        sequence[i] = sequence[i - 2] + sequence[i - 1]

    return sequence


def test_create_fibo_series():

    assert create_fibo_series(3) == [0, 1, 1]
    assert create_fibo_series(1) == [0]
    assert create_fibo_series(2) == [0, 1]
