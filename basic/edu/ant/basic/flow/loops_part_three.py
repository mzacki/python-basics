# while loop

# for i in range(10):
# print("Current value of i is {}".format(i))
# same result, but contrary to compiled languanges beneath it's different code
# in C or Java it would compile into the same bytecode

i = 0
while i < 10:
    print("Current value of i is {}".format(i))
    i += 1


directions = ["N", "S", "E", "W"]
azimuth = ""

while azimuth not in directions:
    azimuth = input("Where do you head, sage...")
    if azimuth == "quit":
        print("Quitting...")
        break

print("You've chosen your destiny!")
