# lists are mutable, strings are immutable

# immutable in Python
# int
# float
# bool
# str
# tuple
# frozenset
# bytes

# mutable objects in Python
# list
# dict
# set
# Bytearray

var_true = True
var_not_true = var_true
# id() -> identity of an object
# prints same id number for both
print(id(var_true))
print(id(var_not_true))
var_true = False
# now prints different id for var_true
print(id(var_true))
print(id(var_not_true))

example_list = [
    "item1",
    "item2",
    "item3",
    "item4",
    "item5"
]

print(id(example_list))
example_list += ["item6"]
# even after update, it prints the same id - because list is mutable
print(id(example_list))

# iterate through
for item in example_list:
    print(item)

# access by index
print(example_list[4])
# negative index (starts from the end, -1 is the last index of a list)
print(example_list[-1])
# access by range (returns a new list)
print(example_list[0:3])

example_list.append("item5")
print(example_list.count("item5"))

# for item in example list
# for loop is not very efficient iteration way
# enumerate function is much better
for index, item in enumerate(example_list):
    print(f"Index: {index}, {item}")
