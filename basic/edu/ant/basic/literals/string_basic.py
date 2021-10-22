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
text = input("Enter something and press enter....")
print("Entered: " + text)

# stdin without prompt
text2 = input()
print("Without prompt: " + text2)

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

# no escape char needed
print("single quotes 'within' a 'string'")
print('double "quotes" within a "string" plus one more quote inside a pair of quotes """')

# instead of default new line, specify how to end the line and it may continue
print("something....", end=" ")
print("will be print in the same line if 'end' param specified.")
