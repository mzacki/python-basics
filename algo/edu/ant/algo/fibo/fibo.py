def create_fibo_series(last_n):
    sequence = [0] * last_n

    sequence[0] = 0

    if last_n > 1:
        sequence[1] = 1

    for i in range(2, last_n):
        sequence[i] = sequence[i - 2] + sequence[i - 1]

    return sequence


def fibo_faster(n):
    current = 0
    one_fib_ago = 1
    two_fib_ago = 0

    for i in range(2, n + 1):
        current = two_fib_ago + one_fib_ago
        if i == 2:
            continue
        two_fib_ago = one_fib_ago
        one_fib_ago = current

    return current


def test_create_fibo_series():
    assert create_fibo_series(3) == [0, 1, 1]
    assert create_fibo_series(1) == [0]
    assert create_fibo_series(2) == [0, 1]


def test_fibo_faster():
    assert fibo_faster(1) == 0
    assert fibo_faster(2) == 1
    assert fibo_faster(3) == 1
    assert fibo_faster(4) == 2
