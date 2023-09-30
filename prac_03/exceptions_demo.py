"""
CP1404 Prac 3 - Exceptions Demo
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# Questions:
# 1. When anything other than an integer is input
# 2. When 0 is input as the denominator
