# three number types in Python: int, float and complex

# float division
division = [2 / 3, 1 / 2, 1 / 1]

for result in division:
    print(result)

# note limited accuracy of floating-point result when dividing...
division3 = 10 / 3
print(division3)
# ...but it gets back to normal when multiplied again:
print(division3 * 3)

# integer division and modulo example
print([10 % 3, 10 // 3])

# power
print(2 ** 10)

# there is no root operator - workaround is to power using fractional exponent
# example: square root equals power to 1/2
sqr_root = 4 ** (1/2)
print(sqr_root)
cube_root = 8 ** (1/3)
print(cube_root)
quad_root = 81 ** (1/4)
print(quad_root)

# dynamic typing
a = 2 + 2  # int
print(type(a))
a = 4 / 3  # float
print(type(a))

# complex numbers
# complex number contain real number plus so-called imaginary unit, denoted in Python as "j"
# example: square root of -1
a = (-1) ** (1/2)
print(a)
# Vorsicht! limited accuracy again!
print(type(a))

# in REPL we can use underscore _ as a wildcard for recently counted value
# also for better readibility
a = 2_000_000
print(type(a))  # it is a valid int!


