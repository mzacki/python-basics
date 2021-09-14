from sympy import limit, symbols

r1, r2, r = symbols("r1 r2 r")

r = (r1 * r2) / (r1 + r2)
r1 = r2

# r1 / 2 -> 0
print(limit(r, r1, 0))
# result is 0

# 1 / x with x -> 0
x = symbols("x")
print(limit(1 / x, x, 0))
# result is infinity
