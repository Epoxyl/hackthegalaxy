from collections import Counter
from tkinter import Tk

import english_words

from TabIHM import *

def common_chars(word, words):
    list_word = Counter(word)
    letters = {}
    for other_word in words:
        list_other_word = Counter(other_word)

        common = list_word & list_other_word
        for letter in common:
            if letter not in letters.keys():
                letters[letter] = 1
            else:
                letters[letter] += 1
        print("{}/{}     {}".format(word, other_word, ",".join(common)))
    for letter in letters.keys():
        if letters[letter] == 1:
            print("only one letter for {}".format(letter))



word = "nets"
words = [
    "micron", "sweeter", "strands"
]

common_chars(word, words)


for word in english_words.english_words_set:
    if len(word) != 4:
        continue

    if word[3] == 'y' and word[2] in ['c','r','u','x'] and word[1] in ['w', 'e', 'l', 'l'] and word[0] in ['o', 'p', 'a', 'l']:
        print(word)