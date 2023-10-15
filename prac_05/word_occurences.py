"""
CP1404 Prac 5 - Word Occurences
Estimate: 10 minutes
Actual: 11 minutes
"""

text = input("Text: ")
words = text.strip().split(' ')

word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

words = list(word_to_count.keys())
words.sort()
max_word_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
