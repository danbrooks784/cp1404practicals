"""
CP1404 Prac 4 - Quick Picks
"""
import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    picks = []
    for number in range(NUMBERS_PER_LINE):
        pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while pick in picks:
            pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        picks.append(pick)
        picks.sort()
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*picks))
