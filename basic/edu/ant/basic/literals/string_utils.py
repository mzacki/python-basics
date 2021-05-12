# print given char from string (starts from 0)
title = "The Constant Gardener"
print(title[7])
# string length
print(len(title))
# negative indexing (starts from -1)
print(title[-21])
# (0-based index) - (size length) = negative index value
print(title[0 - len(title)])

# substring (slicing): start index inclusive, end index exclusive (like in Java)
print(title[0:3])
print(title[:21])
print(title[13:])
print(title[:13] + title[13:])
# or
print(title[:])

# negative index slicing
print(title[-21:-13])
# or both mixed
print(title[-21:8])

# step slicing
print(title[:21:2])  # every second char
print(title[0:21:5])  # every fifth char

# conversion to string: replacement fields (instead of str())
number = 10
print("The number equals {0}".format(number))
print("There are {0} empty slots: {1}, {2}".format(2, "one", "two"))

# f-string
print(f"An f-string formatter of {number} number")
