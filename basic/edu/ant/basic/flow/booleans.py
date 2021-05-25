flag = True
anotherFlag = False

# not (!something)
print(not flag)
print(not anotherFlag)

if flag:
    print("Flag is true")

if not anotherFlag:
    print("Not another flag")

# truthy values - sth evaluates to true:

# Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
# Numeric values that are not zero.
# True

# falsy values - sth evaluates to false:

# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ""
# Empty ranges range(0)
# # # Numbers
# Zero of any numeric type.
# Integer: 0
# Float: 0.0
# Complex: 0j
# # # Constants
# None
# False


# empty string evaluates to false
givenString = ""

if not givenString:
    print("Empty string")

# not empty string evaluates to true
notEmptyString = "This string is not empty"

if notEmptyString:
    print(notEmptyString)

if 1:
    print("One is true")

if not 0:
    print("0 is false, so not zero is true")

