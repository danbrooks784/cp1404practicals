"""
CP1404 Prac 6 - Guitar Testing
Estimated time: 5 minutes
Actual time: 5 minutes
"""

from guitar import Guitar

guitar_gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_another = Guitar("Another Guitar", 2013, 825.99)

print(f"{guitar_gibson.name} get_age() - Expected {2023 - 1922}. Got {guitar_gibson.get_age()}")
print(f"{guitar_another.name} get_age() - Expected {2023 - 2013}. Got {guitar_another.get_age()}")

print(f"{guitar_gibson.name} is_vintage() - Expected True. Got {guitar_gibson.is_vintage()}")
print(f"{guitar_another.name} is_vintage() - Expected False. Got {guitar_another.is_vintage()}")
