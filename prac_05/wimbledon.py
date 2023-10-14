"""
CP1404 Prac 5 - Wimbledon
Estimated time: 30 minutes
Actual time:
"""

FILENAME = "wimbledon.csv"


def main():
    """Read the wimbledon winners file and display processed data from it."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            records.append(line.strip().split(','))
    display_champions(records)
    display_countries(records)


def display_champions(records):
    """Print the champions and how many times they have won."""
    champion_to_win_count = {}
    for record in records:
        try:
            champion_to_win_count[record[2]] += 1
        except KeyError:
            champion_to_win_count[record[2]] = 1
    for champion, win_count in champion_to_win_count.items():
        print(f"{champion} {win_count}")


def display_countries(records):
    """Print the countries of each champion in alphabetical order."""
    countries = set()
    for record in records:
        countries.add(record[1])
    print(f"\nThese {len(countries)} have won Wimbledon: ")
    print(', '.join(sorted(countries)))


main()
