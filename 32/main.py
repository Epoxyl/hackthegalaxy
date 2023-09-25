import json

from english_words import english_words_set

from trie import Trie


#rivers = []
#with open("../27/rivers.json") as f:
#    file = json.loads(f.read())
#    for river in file["rivers"]:
#        print(river)
#        rivers.append(river['name'])

elements = []
with open("elements") as f:
    lines = f.readlines()
    for line in lines:
        elements.append(line.lower())


t = Trie()
for word in elements:
    print(word)
    t.insert(word.lower())

grid1 = [
    ['d', 'ge', 'o', 'm', 'hi'],
    ['ar', 'r', 'af', 'r', 'bi'],
    ['s', 'c', 'ic', 'an', 'f'],
    ['hi', 'go', 'iu', 'cu', 'od'],
    ['il', 'm', 's', 'd', 'ld']
]

grid2 = [
    ['g', 'to', 'i', 'ch', 'cr'],
    ['am', 'oc', 'r', 'g', 'e'],
    ['t', 'el', 'ci', 'u', 'o'],
    ['e', 'k', 'an', 'di', 'oi'],
    ['on', 'o', 'se', 'a', 'le']
]

grid3 = [
    ['f', 'a', 'ta', 'h', 'ba'],
    ['ek', 'e', 'dm', 'oc', 'r'],
    ['in', 'wo', 'nc', 'c', 'k'],
    ['nd', 'in', 'e', 'he', 't'],
    ['ry', 'y', 'og', 'on', 'o']
]

grid4 = [
    ['l', 'o', 'mo', 'st', 's'],
    ['x', 'on', 'i', 'c', 'ne'],
    ['ca', 'af', 'a', 'fo', 'l'],
    ['et', 'si', 'r', 'k', 'e'],
    ['r', 'er', 'n', 'd', 'to']
]

grid5 = [
    ['g', 'ya', 'e', 'na', 'mi'],
    ['n', 'up', 'ma', 's', 'a'],
    ['hr', 'g', 'so', 'ng', 'z'],
    ['o', 'at', 'e', 'ur', 't'],
    ['es', 'n', 'i', 'ze', 's']
]

grid6 = [
    ['r', 'ca', 'c', 'o', 'pe'],
    ['in', 'os', 're', 'r', 'a'],
    ['pr', 'na', 'da', 'g', 'em'],
    ['ar', 'ik', 'm', 'mo', 'an'],
    ['a', 'on', 'y', 'o', 'm']
]

grid7 = [
    ['ma', 'b', 'm', 'ba', 'cu'],
    ['p', 'ca', 'o', 'ro', 'k'],
    ['c', 'ro', 'ca', 'w', 'la'],
    ['v', 'th', 'k', 'o', 'n'],
    ['e', 'n', 'ie', 'a', 'i']
]

grid8 = [
    ['t', 'c', 'ch', 'ni', 'm'],
    ['ro', 'un', 'o', 'er', 'tr'],
    ['b', 'm', 'g', 'cu', 'o'],
    ['r', 'al', 'iu', 'ge', 'rt'],
    ['m', 'tr', 'o', 'st', 'm']
]

grid9 = [
    ['su', 'wo', 'sp', 'h', 'da'],
    ['id', 'l', 'pe', 're', 'el'],
    ['rg', 'e', 'l', 'ad', 've'],
    ['ri', 'ir', 'ev', 'rm', 'bo'],
    ['an', 'y', 'ne', 'l', 'il']
]

t.find_words(grid8, t.root, '', 0, 0)
