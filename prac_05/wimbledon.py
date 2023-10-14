"""
CP1404 Prac 5 - Wimbledon
Estimated time: 30 minutes
Actual time:
"""

FILENAME = "wimbledon.csv"


def main():
    """Read the wimbledon winners file and display processed data from it."""
    lines = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            lines.append(line.strip().split(','))
    print(lines)


main()
