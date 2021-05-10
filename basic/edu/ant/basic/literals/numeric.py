# no size limit for int
# limit for float value
# Decimal data type is used for more than 52 digits of precision

a = 64
b = 1992
print(a / b)  # result is float
print(type(b / a))

# integer division -> round down (or take the floor, or round towards minus infinity) (not truncates!)
print(3 / 2)
print(b // a)
