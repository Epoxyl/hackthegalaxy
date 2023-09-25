import array
import copy
import json
import re

from english_words import english_words_set


class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char, depth_number=0):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        self.depth_number = depth_number + 1

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 1

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

    def __str__(self):
        return "[{} ({})]".format(self.char, self.counter)


class Trie(object):
    """The trie object"""
    output = []

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.removed_nodes = []
        self.root = TrieNode("")
        self.tostring = "Trie : "

    def tostring(self):
        txt = self.tostring + '\n'
        node = self.root
        for children in node.children:
            txt += children.__str__ + ' '
        txt += '\n'

    def insert(self, word):
        """Insert a word into the trie"""

        word = word.lower()
        word = re.sub(r'[^a-z]+', '', word)

        if len(word) < 3:
            return False
        node = self.root
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
                node.counter = node.counter + 1
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char, node.depth_number)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        # node.counter += 1

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x, show=False):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def find_words(self, words, original_words, found_words, node=None):
        #idée : pour chaque nouvelle lettre on ajoute sa node aux possibilités
        #autre idée : pour chaque lettre récupérer les possibles lettres suivantes/for each children
        print("trying {}".format(words))
        if not node:
            node = self.root

        if len(words) == '1':
            ## cas gagné
            return True

        temporary_word = ''
        words_removed = copy.copy(words)
        i = 0
        while i < len(original_words):
            # On avance lettre par lettre et si on trouve un mot on relance find_words avec words = words_removed
            letter = words[i]
            if letter in node.children:
                node = node.children[letter]
                temporary_word += letter
                words_removed.pop(i)
            else:
                i += 1
                continue


    def find_word(self, node, word, letter_position=0, original_word_letter_position=0, letters_position=None):
        if not node:
            node = self.root

        word = word[letter_position+1:]

        if node.is_end:
            self.output.append(letters_position)

        if not len(node.children):
            return True

        for i in range(len(word)):
            t_letter = word[i]

            if t_letter in node.children:
                new_letters_position = copy.copy(letters_position)
                new_letters_position.append(original_word_letter_position+i+1)
                self.find_word(node.children[t_letter], word, i, original_word_letter_position+i+1, new_letters_position)




def show_words(pos1, pos2, pos3, words, letter):
    str = '{} : '.format("".join(words))
    new_words = copy.copy(words)

    for pos in pos1:
        str += new_words[pos]

    for pos in sorted(pos1, reverse=True):
        new_words.pop(pos)

    str += ','


    for pos in pos2:
        str += new_words[pos]

    for pos in sorted(pos2, reverse=True):
        new_words.pop(pos)
    str += ','

    for pos in pos3:
        str += new_words[pos]

    for pos in sorted(pos3, reverse=True):
        new_words.pop(pos)

    str += '---- ({})'.format(''.join(letter))
    return str



t = Trie()

with open('words.txt') as f:
    words = f.readlines()

for word in words:
    word = re.sub(r'[^A-Za-z]+', '', word)
    if len(word) > 2:
        t.insert(word.lower())


words = [
    "papsfrutesutternet",       #past,present,future---- (t)
    "epalwrotavey",             #eat,pray,love---- (w)  ??
    "licagamchitetraison",      #light,cameras,action---- (i)
    "rafietamidrey",            #ready,aim,fire---- (t)
    "holioskinnecker",          #hook,line,sinker---- (c)
    "whildorsawen",
    "lierfictengthert",         #left, right, center (i)
    "litbigonesareress",        #lions,tigers,bears---- (e)
    "gasmarmtechet",            #game,set,match---- (r)
]
word = list("whildorsawen")

node = t.root
t.find_word(node.children[word[0]], list(word), letters_position=[0])

words_positions_list_first = copy.copy(t.output)
t.output = []
answers_list = []
for words_positions in words_positions_list_first:
    new_word = copy.copy(word)
    for words_position_first in sorted(words_positions, reverse=True):
        new_word.pop(words_position_first)

    if new_word[0] not in node.children:
        continue

    t.find_word(node.children[new_word[0]], list(new_word), letters_position=[0])
    if len(t.output):
        words_positions_list_second = copy.copy(t.output)
        t.output = []
        for words_positions_second in words_positions_list_second:
            new_second_word = copy.copy(new_word)

            for words_position_second in sorted(words_positions_second, reverse=True):
                new_second_word.pop(words_position_second)
            if new_second_word[0] not in node.children:
                continue

            t.find_word(node.children[new_second_word[0]], list(new_second_word), letters_position=[0])
            if len(t.output):
                words_positions_list_third = copy.copy(t.output)
                t.output = []
                for words_positions_third in words_positions_list_third:
                    new_third_word = copy.copy(new_second_word)

                    for words_position_third in sorted(words_positions_third, reverse=True):
                        new_third_word.pop(words_position_third)

                    if len(new_third_word) == 1:
                        answers_list.append((words_positions, words_positions_second, words_positions_third, word, new_third_word))

for words_positions, words_positions_second, words_positions_third, word, new_third_word in answers_list:
    str = show_words(words_positions, words_positions_second, words_positions_third, word, new_third_word)
    print(str)

