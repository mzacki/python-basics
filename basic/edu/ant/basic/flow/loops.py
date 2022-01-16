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
# continue
wish_list = ["ant", "cat", "books", "beer", "toys", "carrot"]
for item in wish_list:
    if item == "toys":
        continue
    print(item)

# break
task_list = ["roof", "elevation - thermal insulation", "chimney", "beer", "furnace", "fence"]
print("Today working on....")
for task in task_list:
    if task == "beer":
        print("I am taking a break!")
        break
    print(task)
print("Let's call it a day!")
