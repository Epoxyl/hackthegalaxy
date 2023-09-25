import enchant

blue = ["a", "b", "n", "o"]
green = ["c", "d", "e", "p", "q", "r"]
rose = ["f", "g", "h", "s", "t", "u"]
white = ["i", "j", "k", "v", "w", "x"]
yellow = ["l", "m", "y", "z"]

def test_word(indexes, letter_colors):
    word = ""
    if (d.check(word)):
        print(word)

def find_word(letter_colors, word, position):
    if position == 8:
        if d.check(word):
            print("found ! {}".format(word))
            return True
        else:
            return False

    letters = globals()[letter_colors[position]]
    for letter in letters:
        new_word = word + letter
        find_word(letter_colors, new_word, position + 1)
    return False


d = enchant.Dict("en_US")
first_word = ["blue", "green", "green", "green", "blue", "green", "white", "white"]
second_word = ["rose", "blue", "green", "green", "rose", "green", "blue", "green"]
third_word = ["yellow", "blue", "blue", "green", "white", "blue", "yellow", "green"]
fourth_word = ["green", "blue", "blue", "green", "green", "green", "blue", "rose"]
fifth_word = ["rose", "rose", "white", "blue", "blue", "blue", "blue", "green"]
sixth_word = ["rose", "rose", "blue", "rose", "yellow", "green", "green", "green"]

indexes = [0, 0, 0, 0, 0, 0, 0, 0]
print("first word : ")
find_word(first_word, "", 0)
print("second word : ")
find_word(second_word, "", 0)
print("third word : ")
find_word(third_word, "", 0)
print("fourth word : ")
find_word(fourth_word, "", 0)
print("fifth word : ")
find_word(fifth_word, "", 0)
print("sixth word : ")
find_word(sixth_word, "", 0)
