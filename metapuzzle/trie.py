import array
import copy
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

    def dfs(self, node, prefix, only_end=False):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
            return

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
        if only_end:
            self.dfs(node, x, only_end)
        else:
            self.dfs(node, x[:-1])

# Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def find_word(self, tried_words, words, node, not_positions, char_positions, tried_word):
        char_i, original_words_position = words.pop(0)


        char_positions.append(original_words_position)
        if char_i in node.children and char_positions not in not_positions:
            node = node.children[char_i]
            char_positions += original_words_position
            if node.is_end:
                tried_words.append([tried_word + char_i, char_positions])
                if len(tried_words) == 2:
                    third_word = "".join([i[0] for i in words])
                    if third_word in english_words_set:
                        tried_words.append([third_word, char_positions])
                        return tried_words
                    else:
                        return False
        elif not len(words):
            return False


        ret = self.find_word(tried_words, words, node, not_positions, char_positions, tried_word)



    def find_words(self, original_words):
        node = self.root
        i = 0

        found_words = [["", []], ["", []], ["", []]]
        not_positions = [[], [], []]

        current_word_number = 0
        current_word, chars_positions = found_words[current_word_number]
        original_words_position = 0
        words = [[original_words[i], i] for i in range(len(original_words))]
        while current_word_number < len(found_words):
            print(current_word)
            char_i, original_words_position = words[i]

            if chars_positions + [original_words_position] in not_positions[current_word_number]:
                i += 1
                continue

            if char_i in node.children:
                node = node.children[char_i]
                words.pop(i)
                current_word += char_i
                chars_positions.append(original_words_position)
                if node.is_end:
                    # On a trouvé un mot. On l'ajoute dans les mots trouvés
                    found_words[current_word_number] = [current_word, chars_positions]
                    chars_positions = []
                    print("word found ! {}".format(found_words))
                    print(current_word_number)
                    current_word_number += 1
                    current_word = ""
                    node = self.root
                    i = 0

                    if current_word_number == 2 and "".join(word) in english_words_set:
                        return True
                    elif current_word_number == 2:
                        print("res {}".format(found_words))
                        not_positions[1].append(found_words[1][1])
                        found_words = [["", []], ["", []], ["", []]]
                        current_word_number = 0

            else:
                i += 1

            if original_words_position + 1 == len(original_words):
                not_positions[current_word_number].append(chars_positions)

                # On réinitialise car on a atteint le bout sans trouver de mots
                i = 0
                original_words_position = 0
                node = self.root
                words = [[original_words[i], i] for i in range(len(original_words))]
                print(current_word_number)

                if current_word_number == 1:
                    found_words[0] = ["", []]
                    current_word_number = 0

                if current_word_number == 2:
                    not_positions[current_word_number-1].append(found_words[1][1])
                    found_words[1] = ["", []]
                    for pos in sorted(found_words[0][1], reverse=True):
                        words.pop(pos)
                    current_word_number = 1

                chars_positions = []
                current_word = ""
                continue
