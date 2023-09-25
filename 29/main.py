import array
import copy
import re
import enchant
import requests
from bs4 import BeautifulSoup
import gensim.downloader as api
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

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

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
        self.tostring = "Trie : "
        self.output = []

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

    def query(self, x, show=False, only_end=False):
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

    def split_word(self, rockets_1, rockets_2):
        words_possibilities = []
        node = self.root

        if not isinstance(rockets_1, list):
            rockets_1 = [rockets_1]

        if not isinstance(rockets_2, list):
            rockets_2 = [rockets_2]

        for rocket_1 in rockets_1:
            rocket_1 = rocket_1.lower()
            for rocket_2 in rockets_2:
                rocket_2 = rocket_2.lower()
                for i in range(2,len(rocket_1)):
                    rocket_1_first_word, rocket_1_second_word = rocket_1[:i], rocket_1[i:]
                    rocket_1_first_word_bis, rocket_1_second_word_bis = rocket_1[:i], rocket_1[i+1:]

                    for j in range(2, len(rocket_2)):
                        rocket_2_first_word, rocket_2_second_word = rocket_2[:j], rocket_2[j:]
                        rocket_2_first_word_bis, rocket_2_second_word_bis = rocket_2[:j], rocket_2[j + 1:]

                        old_rocket_1 = rocket_1_first_word+rocket_2_second_word_bis
                        old_rocket_2 = rocket_2_first_word_bis+rocket_1_second_word
                        if d.check(old_rocket_1) and d.check(old_rocket_2):
                            print("{} {} -> {} {} ({})".format(old_rocket_1, old_rocket_2, rocket_1, rocket_2, rocket_2[j]))
                            words_possibilities.append((old_rocket_1, old_rocket_2))

                        old_rocket_1 = rocket_1_first_word_bis+rocket_2_second_word
                        old_rocket_2 = rocket_2_first_word+rocket_1_second_word_bis


                        if d.check(old_rocket_1) and d.check(old_rocket_2):
                            print("{} {} -> {} {} ({})".format(old_rocket_1, old_rocket_2, rocket_1, rocket_2, rocket_1[i]))
                            words_possibilities.append((old_rocket_1, old_rocket_2))
                self.output.append(words_possibilities)

def get_clues(clue):
    clues = []
    with open('contents\\{}.htm'.format(clue)) as f:
        html_response = f.read()
    clue.replace(' ', '-')



    attrs = {
        'class': "clue"
    }
    #print(html_response)
    soup = BeautifulSoup(html_response, 'html.parser')
    tracks = soup.find_all('tr', attrs=attrs)
    for tr in tracks:
        div = tr.find('div', {'class':'stars'})
        if div and len(div.find_all('div')) >= 3:
            word = tr.find('a').getText()
            if len(word) > 4:
                clues.append(word)

    return clues

d = enchant.Dict('en_US')


#answer_1 = get_clues("departures counterpart")
#answer_2 = get_clues("scold") + get_clues("harshly criticize")
#answer_1 = ["lute", "oud", "pipa", "guitar", "citole", "gittern", "mandore", "rubab", "gambus"]
#answer_2 = ["interest", "interests"]

old_rockets = []
with open("rockets_words.txt") as f:
    for line in f.readlines():
        line = line.strip()
        words = line.split('/')
        old_rockets += words

print(old_rockets)
t = Trie()

answer_1 = ["oud", "pipa", "guitar", "citole", "gittern", "mandore", "rubab", "gambus"]
answer_2 = get_clues("scold") + get_clues("harshly criticize")

#answer_1 = ["starve", "starving", "starved", "famished", "fast"]

t.split_word("premium", "curvature")
#words_possibilities = []
#for old_rocket_1 in old_rockets:
#    old_rocket_1 = old_rocket_1.lower()
#    for old_rocket_2 in old_rockets:
#        old_rocket_2 = old_rocket_2.lower()
#        if old_rocket_1 == old_rocket_2:
#            continue
#
#        for i in range(2,len(old_rocket_1)-2):
#            old_rocket_1_first_part, old_rocket_1_second_part = old_rocket_1[:i], old_rocket_1[i:]
#
#
#            for j in range(2, len(old_rocket_2)-2):
#                old_rocket_2_first_part, old_rocket_2_second_part = old_rocket_2[:j], old_rocket_2[j:]
#
#                new_rocket_1 = old_rocket_1_first_part+old_rocket_2_second_part
#                new_rocket_2 = [old_rocket_2_first_part + letter + old_rocket_1_second_part for letter in string.ascii_lowercase]
#
#                if d.check(new_rocket_1):
#                    for word in new_rocket_2:
#                        if d.check(word):
#                            print("{} {} -> {} {}".format(old_rocket_1, old_rocket_2, new_rocket_1, word))
#                            words_possibilities.append((new_rocket_1, new_rocket_2))
#