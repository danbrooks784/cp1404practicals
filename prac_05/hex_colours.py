"""
CP1404 Prac 5 - Hex Colours
"""

COLOUR_TO_CODE = {"APRICOT": "#fbceb1", "CAROLINABLUE": "#56a0d3", "GHOSTWHITE": "#f8f8ff", "HARVESTGOLD": "#da9100",
                  "JAZZBERRYJAM": "#a50b5e", "LILAC": "#c8a2c8", "MINT": "#3eb489", "PEARLYPURPLE": "#b768a2",
                  "PUMPKIN": "#ff7518", "SINOPIA": "#cb410b", "VANILLA": "#f3e5ab", "YELLOWGREEN": "#9acd32"}

colour = input("Enter colour: ").upper()
while colour != "":
    try:
        print(COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour.")
    colour = input("Enter colour: ").upper()
