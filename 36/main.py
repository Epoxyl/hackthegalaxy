import json
import string

import enchant
from english_words import english_words_set

from deep_translator import GoogleTranslator
import trie

d = enchant.Dict("en_US")
tr = GoogleTranslator(source='en', target='fr')

def first_poem(word):
    found_words = []
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]

        if d.check(new_word):
            letter_removed = word[i]
            found_words.append((new_word, letter_removed))
    return found_words

def second_poem(word):
    skipped_words = ["imbrue"]
    found_words = []
    for letter in string.ascii_lowercase:
        new_word = letter + word[1:]

        if new_word != word and new_word not in skipped_words and d.check(new_word):
            letter_removed = word[0]
            found_words.append((new_word, letter_removed))
    return found_words

def third_poem(word):
    skipped_words = ["bondsmen"]
    found_words = []
    for letter in string.ascii_lowercase:
        new_word = word[0] + letter + word[2:]

        if new_word != word and new_word not in skipped_words and d.check(new_word):
            letter_removed = word[1]
            found_words.append((new_word, letter_removed))
    return found_words

def fourth_poem(word):
    skipped_words = ["oncology"]
    found_words = set()
    for i in range(len(word)):
        letter = word[i]
        if word.count(letter) == 2:
            new_word = word.replace(letter, "")
            if new_word not in skipped_words and d.check(new_word):
                letter_removed = letter
                found_words.add((new_word, letter_removed))
    return list(found_words)

def guess_words():
    found_words = [{}, {}, {}, {}]
    skipped_words = [
        [],
        ["imbrue", "around"],
        ["bondsmen"],
        ["oncology"]
    ]
    skipped_changed_words = [
        [],
        ["argent"],
        [],
        ["prince"]
    ]

    skipped_final_words = [
        "lyra"
    ]

    # ret = ("grave", 'l')
    # found_words[0]["gravel"] = [ret]
    # for word in english_words_set:
    #     if word[0].isupper():
    #         continue
    #
    #     if len(word) == 6:
    #
    #         ret = second_poem(word)
    #         if ret:
    #             found_words[1][word] = ret
    #
    #     if len(word) == 8:
    #         ret = third_poem(word)
    #         if ret:
    #             found_words[2][word] = ret
    #
    #         ret = fourth_poem(word)
    #         if ret:
    #             found_words[3][word] = ret
    # print("here ! ")
    # print(found_words)
    #
    # with open('found_words.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(found_words))

    with open('found_words.json', 'r', encoding='utf-8') as f:
      found_words = json.loads(f.read())

    print("here")
    print(found_words)

    answers = set()
    node = T.root
    for word_0, changed_word_0, in found_words[0].items():
        for (changed_word_0, letter_0) in changed_word_0:
            if letter_0 not in node.children or word_0 in skipped_words[0] or changed_word_0 in skipped_changed_words[0]:
                continue
            node_0 = node.children[letter_0]

            for word_1, changed_word_1, in found_words[1].items():
                for (changed_word_1, letter_1) in changed_word_1:
                    if letter_1 not in node_0.children or word_1 in skipped_words[1] or changed_word_1 in skipped_changed_words[1]:
                        continue
                    node_1 = node_0.children[letter_1]

                    for word_2, changed_word_2, in found_words[2].items():
                        for (changed_word_2, letter_2) in changed_word_2:
                            if letter_2 not in node_1.children or word_2 in skipped_words[2] or changed_word_2 in skipped_changed_words[2]:
                                continue
                            node_2 = node_1.children[letter_2]

                            for word_3, changed_word_3, in found_words[3].items():
                                for (changed_word_3, letter_3) in changed_word_3:
                                    if letter_3 not in node_2.children or word_3 in skipped_words[3] or changed_word_3 in skipped_changed_words[3]:
                                        continue
                                    node_3 = node_2.children[letter_3]
                                    if node_3.is_end:
                                        final_word = letter_0+letter_1+letter_2+letter_3
                                        if final_word in skipped_final_words:
                                            continue
                                        answers.add(final_word)
                                        print("word found : "+final_word)
                                        print("     {} ({})".format(word_0, changed_word_0))
                                        print("     {} ({})".format(word_1, changed_word_1))
                                        print("     {} ({})".format(word_2, changed_word_2))
                                        print("     {} ({})".format(word_3, changed_word_3))
    print(answers)
T = trie.Trie()
for word in english_words_set:
    if len(word) == 4:
        T.insert(word.lower())

# guess_words()

found_words = {}
for word in english_words_set:
    if len(word) != 8:
        continue
    ret = fourth_poem(word)
    if ret:
        found_words[word] = ret

for word, change_words in found_words.items():
    try:
        translated_word = tr.translate(word)
    except:
        print("error translating word "+ word)
        continue
    print("{} ({}):".format(word, translated_word))
    for (change_word, letter) in change_words:
        translated_change_word = tr.translate("{} {}".format(word, change_word))
        print("       {} {} ({})".format(word, change_word, translated_change_word))

