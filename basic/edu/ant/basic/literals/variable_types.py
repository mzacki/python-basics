# dynamically typed
# changing var type is not possible in Java
sth = 23
print("Initial type: ", type(sth))  # int
sth = "23"
print("Current type: ", type(sth))  # string

# strongly typed
# e.g. no automatic type conversion
# explicit conversion is always needed
# print(sth + 23) ---> type error

# None - constant shows that something does not have a value
# roughly equivalent to null in C or Java
found_at = None
