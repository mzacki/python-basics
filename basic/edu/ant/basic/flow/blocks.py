# nested loop
for i in range(0, 9):
    print("The storm is coming...")
    for j in range(5, 0, -1):
        print(f"Achtung! {j}")

# if statement
name = input("What is your name? ")
if (len(name) % 2) != 0:
    print("You're odd!")
else:
    print("You're even!")
