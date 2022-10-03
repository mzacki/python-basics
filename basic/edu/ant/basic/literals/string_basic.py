print(2 * 5)
print()  # prints empty line
print("Prints multiple", "args", "even ints like", 4)  # accepts numeric literals, prints like strings
print('Single or double quotes')
print("  ' '  ")  # quotes within quotes

# string vars declaration
string = "typische string"
string2 = "another string"
print(string + ' ' + string2)

# stdin input example with prompt
# text = input("Enter something and press enter....")
# print("Entered: " + text)

# stdin without prompt
# text2 = input()
# print("Without prompt: " + text2)

# escape and special chars
text3 = "New line char \n and tab \t, after which goes escaped \'"
print(text3)

# text blocks
text4 = """Python knows
when you want
to begin a new line...
(and have a text block
like in Java 13/14)"""

print(text4)

# no escape char needed but one may use it
print("single quotes 'within' a 'string'")
print('double "quotes" within a "string" plus one more quote inside a pair of quotes """')

# instead of default new line, specify how to end the line, and it may continue
print("something....", end=" ")
print("will be print in the same line if 'end' param specified.")

# print various types in one string
print("Sum of 2 and 2 is ", 2 + 2)
# print a word x times
print("Repeat " * 5)
# print documentation of print function
# print(print.__doc__)
# print function can use so-called named arguments:
print("I", "have", "a", "cat", sep=" - ", end=" $$$ \n")  # end can be \n for example

# Formatter
# print evaluates expressions in braces but with f-letter (formatter)
print(f"This is evalutation of 2 * 3. Result is {2 * 3}")
cat = "Katt"
print(f"Cat's name is {cat}")

# f - formatter and braces works also for number systems' conversion:
# 0x - hexadecimal
# 0o - octal
# 0b - binary
our_decimal_number = 16
print(
    f"Number {our_decimal_number} is binary {our_decimal_number:0b}, hexadecimal {our_decimal_number:0x}, "
    f"and octal {our_decimal_number:0o}")

# % as formatter is outdated
# .format is allowed
title = "The Moomins"
book = "book"
print("{} is my favorite {}.".format(title, book))
