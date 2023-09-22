# CP1404 Prac 1 - Loops

# a. Count in 10s from 0 to 100:
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Count down from 20 to 1:
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print n stars:
stars = int(input("Number of stars: "))
for i in range(stars):
    print("*", end='')
print()

# d. Print n lines of increasing stars:
lines = int(input("Number of lines: "))
for i in range(1, lines + 1):
    print("*" * i)
print()
