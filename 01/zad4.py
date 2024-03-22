length = int(input("Enter length: "))

for i in range(length):
    print("|....", end="")
print("|")

for i in range(1, length + 1):
    print(f"{i:5d}", end="")
print()
