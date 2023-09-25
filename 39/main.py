from copy import copy

import nltk
from english_words import english_words_set

from trie import Trie


def search_words(line, node_1, node_2, word1, word2):
    if not node_1:
        node_1 = t.root
        node_2 = copy(t.root)
    if not len(line) and node_1.is_end and node_2.is_end:
        print("answer : {} {}".format(word1, word2))
        return True
    elif not len(line):
        return False

    case = line[0]
    ret = False
    if not case:
        new_nodes = set(node_1.children).intersection(set(node_2.children))
        for child in new_nodes:
            ret = search_words(line[1:], node_1.children[child], node_2.children[child], word1 + child, word2 + child)
    elif isinstance(case, str):
        if case not in node_1.children or case not in node_2.children:
            return False
        ret = search_words(line[1:], node_1.children[case], node_2.children[case], word1 + case, word2 + case)
    else:
        if case[0] in node_1.children and case[1] in node_2.children:
            ret = search_words(line[1:], node_1.children[case[0]], node_2.children[case[1]], word1 + case[0],
                               word2 + case[1])
        elif not case[0] and case[1] in node_2.children:
            for child in node_1.children:
                ret = search_words(line[1:], node_1.children[child], node_2.children[case[1]], word1 + child,
                                   word2 + case[1])
        elif not case[1] and case[0] in node_1.children:
            for child in node_2.children:
                ret = search_words(line[1:], node_1.children[case[0]], node_2.children[child], word1 + case[0],
                                   word2 + child)
    return ret


t = Trie()

# nltk.download('words')

with open("../words.txt") as f:
    words = f.readlines()

for word in words:
    if len(words) > 3:
        t.insert(word.lower())

# line_to_guess = [["b", "f"], ['l', 'r'], None, None]
# line_to_guess = [None, ['o','a'], ['h','v'], None, None, None]
# line_to_guess = [None, None, ['m','d'], ['i','e'], None]
# line_to_guess = ['c', [None, 'e'], ['c', 'l'], None, None ,None, None]
# line_to_guess = [['c','d'], ['a','u'], None, 't']
# line_to_guess = ['s', None, [None, 'x'], ['m','t'], None, None]
# line_to_guess = [['s', 'y'], ['i', 'o'], None, None]
# line_to_guess = [['c', 'd'], ['a', 'u'], None, None]
line_to_guess = ['c', None, None, ['m', None], ['a', 'y']]
# line_to_guess = ['m', None, 'n', ['s', None], ['t', 'k'], None, None]
# line_to_guess = ['s', ['p','y'], ['e','n'], None]
# line_to_guess = ['c', None, ['m', 's'], ['p','h'], None, None, 'r']
# line_to_guess = ['a', None, None, ['e', None], ['x', 'y'], None, None, None]
# line_to_guess = [None, 'n', ['s', 't'], [None, 'l'], None, None]
# line_to_guess = ['i', None, ['q', 's'], ['u', 'p'], None, None, 'e']
# line_to_guess = [None, 'i', ['d', None], ['a', 'e'], None, 't']
# line_to_guess = ['e', None, None, ['c', None], ['h', 'y']]
# line_to_guess = [None, 'o', None, None, [None, 'e'], ['p','c'], None]
# line_to_guess = ['r', None, [None, 'f'], ['g','l'], None]
# line_to_guess = ['i', [None, 'n'], ['l', 's'], None, None]
# line_to_guess = [None, 'e', ['n', 'r'], ['c','t'], None]
# line_to_guess = [None, 'h', ['i', 'o'], ['f', 'r'], None]
# line_to_guess = ['s', ['a', 'i'], [None, 'x'], 't', None]
# line_to_guess = [None, None, 's', ['i', 'h'], ['c', 'y']]
# line_to_guess = [None, ['c', 'o'], ['a', None], None, None, 'e']
# line_to_guess = [None, 'r', [None, 'e'], ['t', 's'], 'h']
# line_to_guess = [None, None, None, ['u', 'i'], ['s', 'f'], None]

print(search_words(line_to_guess, None, None, "", ""))
