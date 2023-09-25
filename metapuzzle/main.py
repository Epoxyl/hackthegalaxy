from english_words import english_words_set
import enchant

from trie import Trie, TrieNode

letters_possibilities = [
    "epalwrotavey",
    "whildorsawen",
    "litbigonesareress"
]

new_letter_possibilities = []
i=0
for word in letters_possibilities:
    new_letter_possibilities.append(set())
    for letter in word:
        new_letter_possibilities[i].add(letter)
    i += 1
print("here")
t = Trie()
for word in english_words_set:
    if len(word) == 5:
        t.insert(word.lower())
print("#~############################")
d = enchant.Dict('en_US')

words = set()
node = t.root
for letter0 in letters_possibilities[0]:
    if letter0 in node.children:
        node0 = node.children[letter0]
    else:
        continue
    for letter1 in letters_possibilities[1]:
        if letter1 in node0.children:
            node1 = node0.children[letter1]
        else:
            continue
        for letter2 in letters_possibilities[2]:
            if letter2 in node1.children:
                node2 = node1.children[letter2]
            else:
                continue
            word = letter0+letter1+letter2+'el'
            if d.check(word):
                words.add(word)

print(words)