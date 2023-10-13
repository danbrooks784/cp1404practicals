"""
CP1404 Prac 5 - Word Occurences
Estimate: 10 minutes
Actual:
"""

text = input("Text: ")
words = text.strip().split(' ')
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
