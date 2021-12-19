variable = input("Enter string or char....")

searched_item = input("Enter what you looking for....")

# in is case-sensitive
if searched_item in variable:
    print("{} contains item: {}".format(variable, searched_item))
else:
    print("Doesn't contain.")

variable2 = input("Enter string or char again....")

searched_item2 = input("Enter something entirely else....")

# not in is case-sensitive, casefold() converts to lowercase
if searched_item2 not in variable2.casefold():
    print("Good. It's not in {}".format(variable2))
else:
    print("Not good. It's not something else, it's in {}!".format(variable2))

