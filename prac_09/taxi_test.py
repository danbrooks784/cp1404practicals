"""
CP1404 Prac 9 - Taxi Test
"""

from taxi import Taxi

# 1.
my_taxi = Taxi("Prius 1", 100)

# 2.
my_taxi.drive(40)

# 3.
print(f"Taxi details: {my_taxi}")
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# 4.
my_taxi.start_fare()
my_taxi.drive(100)

# 5.
print(f"Taxi details: {my_taxi}")
print(f"Current fare: ${my_taxi.get_fare():.2f}")
