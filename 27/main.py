import csv
import json
import sys
import enchant

# with open('clues.json', encoding='utf-8') as f:
#    clues = json.loads(f.read())

inputs = [
    "ankle",
    "Congo",
    "corn",
    "hardy",
    "height",
    "olive",
    "sed"
    "standup",
    "stash"
    "trot",
]

outputs = [
    "cornea",
    "eighth",
    "hydra",
    "odie",
    "peeve","rile","rankle",
    "second",
    "pushup","sphinx","snake",
    "splash",
]


def sub_1(word):
    new_word = word[1:]
    if new_word in inputs:
        print(new_word)

def sub_2(word):
    for i in range(len(word)):
        new_word = word[:i] + 'y' + word[i] + 'u' + word[i+1:]
        if new_word in outputs or d.check(new_word):
            print("{} : {} {}".format(i+1, word, new_word))

def sub_3(word):
    if len(word) != 5:
        return

    new_word = word[::-1]
    for i in range(1, len(word)):
        new_word = new_word[:len(word)-i]
        if new_word in outputs or d.check(new_word):
            print("{} : {} {}".format(i, word, new_word))

def sub_4(word):
    if len(word) != 4:
        return

    new_word = word[::-1]
    for i in range(1, len(word)):
        new_word = new_word[:len(word)-i]
        if new_word in outputs or d.check(new_word):
            print("{} : {} {}".format(i, word, new_word))


def sub_7(word):
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:] + word[i]
        if word != new_word and (new_word in outputs or d.check(new_word)):
            print("{} : {} {}".format(i + 1, word, new_word))

def sub_9(word):
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in outputs or d.check(new_word):
            print("{} : {} {}".format(i, word, new_word))

d = enchant.Dict('en_US')


for input in inputs:
    sub_9(input)