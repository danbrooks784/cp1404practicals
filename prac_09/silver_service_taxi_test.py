"""
CP1404 Prac 9 - Silver Service Taxi tests
"""

from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Test", 100, 2)
taxi.drive(18)
print(f"Taxi details: {taxi}")
print(f"Current fare: ${taxi.get_fare():.2f}")
