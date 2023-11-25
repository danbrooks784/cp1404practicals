"""
CP1404 Prac 9 - Unreliable Car tests
"""

from unreliable_car import UnreliableCar

# Test 1: 100 fuel, 50% reliability
car = UnreliableCar("Test 1", 100, 50)
print(car)

# Attempt to drive 50 km
for i in range(5):
    car.drive(10)

# Expected odometer: 50 km * 0.5 = 20 or 30 km
print(car, "\n")


# Test 2: 500 fuel, 80% reliability
car = UnreliableCar("Test 2", 500, 80)
print(car)

# Attempt to drive 200 km
for i in range(20):
    car.drive(10)

# Expected odometer: 200 km * 0.8 = 160 km
print(car, "\n")


# Test 3: 200 fuel, 10% reliability
car = UnreliableCar("Test 3", 200, 10)
print(car)

# Attempt to drive 1000 km
for i in range(100):
    car.drive(10)

# Expected odometer: 1000 km * 0.1 = 100 km
print(car, "\n")
