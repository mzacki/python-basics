string = "String"

for char in string:
    print(char)

# first argument inclusive
# last argument exclusive
# no start index defaults to 0
for i in range(1, 5):
    print(i)

# counts to zero step -1
for i in range(10, -1, -1):
    print(i)

# nested for loops
print('Chess coordinates:')
for letter in range(ord('a'), ord('h') + 1):
    for number in range(1, 9):
        # end parameter prints without new line
        print(chr(letter) + str(number), end=' ')

# print new line
print()
# continue # break
wish_list = ["ant", "cat", "books", "beer", "toys"]
for item in wish_list:
    if item == "toys":
        continue
    print(item)
