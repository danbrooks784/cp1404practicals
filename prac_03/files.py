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
name = in_file.read()
in_file.close()
print(f"Your name is {name}")
