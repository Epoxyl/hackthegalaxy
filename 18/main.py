import json
import re


def rearrange_words(dictionnary):
    with open(dictionnary) as d:
        dictionnary_json = json.loads(d.read())


    words_by_number = {}

    for i in range(4, 9, 1):
        words_by_number[i] = {}

    print(words_by_number)
    pattern = r'[^A-Za-z]+'
    words_letter_number = words_by_number.keys()
    for word, desc in dictionnary_json.items():
        new_word = re.sub(r'[^A-Za-z]+', '', word)
        if len(new_word) in words_letter_number:
            words_by_number[len(new_word)][word] = desc

    with open('words_and_desc.json', 'w') as f:
        json.dump(words_by_number, f)


def find_word(length, letters_to_remove):
    words_clue = ["begin"]

    for word in words_by_letter_number[str(length)].keys():
        new_word = ""
        for letter_index in range(len(word)):
            if letter_index not in letters_to_remove:
                new_word += word[letter_index]
        # print("{} {}".format(word, new_word))
        if new_word in words_clue:
            print("{} {} found : {}".format(word, new_word, words_by_letter_number[str(length)][word]))

with open("words.json") as d:
    words_by_letter_number = json.loads(d.read())

all_positions = [
    [0, [4, 6]],
    [0, [0, 1, 4]],
    [0, [0, 2, 3]],

    [0, [3, 5, 6]],
    [0, [4, 6]],
    [8, [1, 6, 7]],

    [7, [2, 5]],
    [6, [2, 5]],
    [8, [0, 1, 3]],

    [8, [0, 4, 6]],
    [0, [2, 3, 6]],
    [0, [0, 4, 6]],

    [7, [0, 2, 3]],
    [7, [1, 3, 4]],
    [8, [2, 3, 5]],
]


i = 0
for [length, position] in all_positions:
    print("try {} !".format(i))
    if length == 0:
        i += 1
        continue
    find_word(length, position)

    i += 1
