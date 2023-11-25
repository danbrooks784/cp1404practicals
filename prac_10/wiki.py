"""
CP1404 Prac 10 - Wikipedia API
"""

import wikipedia

query = input(">>> ")
while query != "":
    try:
        wiki_page = wikipedia.page(query, auto_suggest=False)
        print(wiki_page.title)
        print(wiki_page.summary)
        print(wiki_page.url)
    except wikipedia.exceptions.DisambiguationError:
        print("Disambiguation error.")
    except wikipedia.exceptions.PageError:
        print("Page error.")
    query = input(">>> ")
