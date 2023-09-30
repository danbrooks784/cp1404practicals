"""
CP1404 Prac 3 - Files
"""

# 1.
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Your name is {name}")
in_file.close()

# 3.
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(f"{number1} + {number2} = {number1 + number2}")
in_file.close()
