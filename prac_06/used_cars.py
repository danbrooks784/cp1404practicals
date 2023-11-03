"""
CP1404 Prac 6 - Used Cars
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # 1.
    limo = Car("Limo", 100)

    # 2.
    limo.add_fuel(20)

    # 3.
    print(f"Limo has fuel: {limo.fuel}")

    # 4.
    limo.drive(115)

    # 7.
    print(my_car)
    print(limo)


main()
