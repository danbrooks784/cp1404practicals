"""
CP1404 Prac 10 - Wikipedia API
"""

import wikipedia

query = input(">>> ")
while query != "":
    try:
        if query in wikipedia.search(query):
            print(wikipedia.summary(query))
    except wikipedia.exceptions.DisambiguationError:
        print("Disambiguation error.")
    except wikipedia.exceptions.PageError:
        print("Page error.")
    query = input(">>> ")
