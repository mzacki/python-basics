# lists are mutable, strings are immutable

# immutable in Python
# int
# float
# bool
# str
# tuple
# frozenset
# bytes

example_list = [
    "item1",
    "item2",
    "item3",
    "item4",
    "item5"
]

# iterate through
for item in example_list:
    print(item)

# access by index
print(example_list[4])
# negative index (starts from the end, -1 is the last index of a list)
print(example_list[-1])
# access by range (returns a new list)
print(example_list[0:3])
