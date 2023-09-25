import array
import copy
import json
import re
import string
import enchant

from english_words import english_words_set

authorized_groups = ["dis","ffe","ted"]
autorized_letters = ['a','j']
letters = string.ascii_lowercase

class TrieNode:
    """A node in the trie structure"""

    def __init__(self, str, depth_number=0):
        # the character stored in this node
        self.str = str

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
        return "[{} ({})]".format(self.str, self.counter)


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
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

        #if len(word) != 11:
        #    return False
        node = self.root
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node

        for letter in word:
            if letter in node.children:
                node = node.children[letter]
                node.counter = node.counter + 1
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(letter, node.depth_number)
                node.children[letter] = new_node
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
            self.output.append((prefix + node.str, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.str)

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

    #def find_word(self, full_word='', word='', left_groups=authorized_groups, left_letters=autorized_letters):
    #    if len(full_word) == 11:
    #        print(full_word)
    #        return full_word
#
    #    if len(full_word) == 0 or len(full_word) == 4 or len(full_word) == 8:
    #        tab_type = 'left_groups'
    #        tab = left_groups
    #    elif len(full_word) == 3:
    #        tab_type = 'left_letters'
    #        tab = left_letters
    #    else:
    #        tab_type = 'string'
    #        tab = list(string.ascii_lowercase)
#
    #    for group in tab:
    #        word = word + group
    #        ret = t.query(word)
    #        if len(ret):
    #            new_full_word = full_word+group
    #            new_group = copy.copy(tab)
    #            new_group.remove(group)
    #            word = self.find_word(new_full_word, word, new_group if tab_type == 'left_groups' else left_groups, new_group if tab_type == 'left_letters' else left_letters)

    def check_word(self, word, original_word):
        if not word or len(word) < 3:
            return False


        node = self.root

        word_checked = []
        new_word = ''
        for i in range(len(word)):
            letter = word[i]
            if letter in node.children:
                node = node.children[letter]
                new_word += letter

                if node.is_end:
                    next_word = word[i+1:]
                    if not next_word:
                        word_checked.append(new_word)
                        return word_checked

                    ret = self.check_word(next_word, original_word)
                    if ret:
                        word_checked.append(new_word)
                        word_checked += ret
                        break
            else:
                return False

        if len(word_checked) and "".join(word_checked) == original_word:
            return word_checked
        else:
            return False

    def find_word(self):
        words = {}
        for letter in autorized_letters:
            words[letter] = []

        for first_part in authorized_groups:
            for first_letter in autorized_letters:
                for second_part in authorized_groups:
                    for second_letter in letters:
                        for third_part in authorized_groups:
                            if first_part == second_part or first_part == third_part or second_part == third_part:
                                continue
                            word = first_part+first_letter+second_part+second_letter+third_part
                            ret = self.check_word(word, word)
                            if ret:
                                words[first_letter].append(ret)
        return words

print(letters)
#with open('clues.json') as f:
#    clues = json.loads(f.read())
#
d = enchant.Dict('en_US')
t = Trie()
##todo: insert only one letter and try by group with multiple words
for mot in english_words_set:
    if len(mot) > 2:
        t.insert(mot)

print("finished insert")
words = t.find_word()
for line in words.keys():
    line_str = "ligne {} : ".format(line)
    for word in words[line]:
        line_str += '"' + ' '.join(word) + '" '
    print(line_str)