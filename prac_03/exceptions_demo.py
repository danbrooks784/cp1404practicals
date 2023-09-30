"""
CP1404 Prac 3 - Exceptions Demo
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


# Questions:
# 1. When anything other than an integer is input
# 2. When 0 is input as the denominator
# 3. Add a loop that asks for denominator input until it is not 0
