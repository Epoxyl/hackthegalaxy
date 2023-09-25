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
    output = []
    words_to_skip = ["terbium"]

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

    def find_words(self, grid, node, word, x, y):
        print("##"+word)
        if y == 5:
            if node.is_end:

                if word not in self.output and word not in self.words_to_skip:
                    self.output.append(word)
                    print("############### add "+word)

                if len(self.output) == 3:
                    txt = ''

                    for word in self.output:
                        txt += word + ' '
                    print(txt)
                    return True
                return self.find_words(grid, self.root, "", x, 0)
            else:
                return False

        line = grid[y]
        print(line)
        ret = False
        for i in range(len(line)):

            case = line[i]
            if len(case) == 2:
                if case[0] in node.children and case[1] in node.children[case[0]].children:
                    new_grid = copy.deepcopy(grid)
                    new_grid[y].remove(case)
                    ret = self.find_words(new_grid, node.children[case[0]].children[case[1]], word+case, i, y+1)

            elif len(case) == 1:
                if case in node.children:
                    new_grid = copy.deepcopy(grid)
                    new_grid[y].remove(case)
                    ret = self.find_words(new_grid, node.children[case], word + case, i, y+1)

            else:
                raise Exception("Taille =/ 1 ou 2")
        return ret


