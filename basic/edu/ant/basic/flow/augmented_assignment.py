n = 0
while n < 10:
    print(n)
    # n = n + 1
    # in Python repeated assignment is less efficient - better use augmented assignment like below
    # Python evaluates n variable twice here
    # moreover, it creates n variable twice (n in line 4 is created regadless of its earlier declaration, then n+1 is assigned to the newly created n)
    # it's different from C++ and Java
    n += 1

array = []

x = 23
x += 1
print(x)
x -= 1
print(x)
# integer division
x //= 3
print(x)
# floating point division
x /= 3
print(x)
# after multiplication x remains float
x *= 5
print(x)
# to second power
x **= 2
print(x)
# modulo
x %= 5
print(x)
# assignment operation on strings
y = "String assignment"
y += " also possible! "
print(y)
# string multiplication
y *= 2
print(y)
