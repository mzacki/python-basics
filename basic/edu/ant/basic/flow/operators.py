# conjunction
if (1 < 2) and (2 < 3):  # "and" corresponds to && in Java
    print("Transitive: 1 < 3")

# alternative
if (1 < 2) or (2 > 3):
    print("At least one or both")  # "or" correponds to || in Java

# combined
value = 11
if 1 < value < 14:
    print("in between")

if 1 < value < 11:
    print("out of range")  # not printed because False
