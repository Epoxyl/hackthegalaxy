import re
import string

from english_words import english_words_set

import trie


def rec_find_word(first_word, second_word, third_word, fourth_word, fifth_word, word, node, statut=0, index_sec=0):
    # if node.depth_number > 4:
    #     print("found word ???? : {} \t\t-> {}".format(word, current_words))
    if first_word:
        new_letter = first_word[0]
        first_word = first_word[1::]
    elif second_word:
        index_sec += 1
        new_letter = second_word[0]
        second_word = second_word[1::]
    elif third_word:
        new_letter = third_word[0]
        third_word = third_word[1::]
    elif fourth_word:
        new_letter = fourth_word[0]
        fourth_word = fourth_word[1::]
    elif fifth_word:
        new_letter = fifth_word[0]
        fifth_word = fifth_word[1::]
    else:
        return False

    if new_letter not in node.children and statut == 1:
        return statut

    if new_letter not in node.children:
        return False
    node = node.children[new_letter]
    word += new_letter

    if statut > 0 and node.is_end and index_sec > 0:
        print("found word : {} \t\t-> {}".format(word, current_words))

    if statut == 0:
        sec_first_word = first_word
        sec_second_word = second_word
        sec_third_word = third_word
        sec_fourth_word = fourth_word
        sec_fifth_word = fifth_word
        if first_word:
            new_new_letter = sec_first_word[0]
            sec_first_word = sec_first_word[1::]
        elif second_word:
            new_new_letter = sec_second_word[0]
            sec_second_word = sec_second_word[1::]
        elif third_word:
            new_new_letter = sec_third_word[0]
            sec_third_word = sec_third_word[1::]
        elif third_word:
            new_new_letter = sec_fourth_word[0]
            sec_fourth_word = sec_fourth_word[1::]
        elif third_word:
            new_new_letter = sec_fifth_word[0]
            sec_fifth_word = sec_fifth_word[1::]
        else:
            return False

        ret1 = rec_find_word(sec_first_word, sec_second_word, sec_third_word, sec_fourth_word, sec_fifth_word, word, node, statut + 1,
                             index_sec if first_word else index_sec+1)


    return rec_find_word(first_word, second_word, third_word, fourth_word, fifth_word, word, node, statut, index_sec)


def find_word(phrase):
    global current_words

    phrase = re.sub(r'[^\w\s]', "", phrase)

    phrase_tab = phrase.split(' ')

    for i in range(len(phrase_tab) - 4):
        first_word = phrase_tab[i]
        second_word = phrase_tab[i + 1]
        third_word = phrase_tab[i + 2]
        fourth_word = phrase_tab[i + 3]
        fifth_word = phrase_tab[i + 4]
        node = T.root
        current_words = (first_word,second_word,third_word,fourth_word,fifth_word)
        for j in range(len(first_word)):
            if first_word[j:] == "aps":
                print("here")
            rec_find_word(first_word[j:], second_word, third_word, fourth_word, fifth_word, "", node)



T = trie.Trie()

fruits = [
        "apple",
        "apricot",
        "avocado",
        "banana",
        "bellpepper",
        "bilberry",
        "blackberry",
        "blackcurrant",
        "blood orange",
        "blueberry",
        "boysenberry",
        "breadfruit",
        "canary melon",
        "cantaloupe",
        "cherimoya",
        "cherry",
        "chili pepper",
        "clementine",
        "cloudberry",
        "coconut",
        "cranberry",
        "cucumber",
        "currant",
        "damson",
        "date",
        "dragonfruit",
        "durian",
        "eggplant",
        "elderberry",
        "feijoa",
        "fig",
        "goji berry",
        "gooseberry",
        "grape",
        "grapefruit",
        "guava",
        "honeydew",
        "huckleberry",
        "jackfruit",
        "jambul",
        "jujube",
        "kiwi fruit",
        "kumquat",
        "lemon",
        "lime",
        "loquat",
        "lychee",
        "mandarine",
        "mango",
        "melon",
        "mulberry",
        "nectarine",
        "nut",
        "olive",
        "orange",
        "papaya",
        "passionfruit",
        "peach",
        "pear",
        "persimmon",
        "physalis",
        "pineapple",
        "plum",
        "pomegranate",
        "pomelo",
        "purple mangosteen",
        "quince",
        "raisin",
        "rambutan",
        "raspberry",
        "redcurrant",
        "rock melon",
        "salal berry",
        "satsuma",
        "star fruit",
        "strawberry",
        "tamarillo",
        "tangerine",
        "tomato",
        "uglifruit",
        "watermelon"
    ]

vegetables = [
        "acorn squash",
        "alfalfa sprout",
        "amaranth",
        "anise",
        "artichoke",
        "arugula",
        "asparagus",
        "aubergine",
        "azuki bean",
        "banana squash",
        "basil",
        "bean sprout",
        "beet",
        "black bean",
        "black-eyed pea",
        "bok choy",
        "borlotti bean",
        "broad beans",
        "broccoflower",
        "broccoli",
        "brussels sprout",
        "butternut squash",
        "cabbage",
        "calabrese",
        "caraway",
        "carrot",
        "cauliflower",
        "cayenne pepper",
        "celeriac",
        "celery",
        "chamomile",
        "chard",
        "chayote",
        "chickpea",
        "chives",
        "cilantro",
        "collard green",
        "corn",
        "corn salad",
        "courgette",
        "cucumber",
        "daikon",
        "delicata",
        "dill",
        "eggplant",
        "endive",
        "fennel",
        "fiddlehead",
        "frisee",
        "garlic",
        "gem squash",
        "ginger",
        "green bean",
        "green pepper",
        "habanero",
        "herbs and spice",
        "horseradish",
        "hubbard squash",
        "jalapeno",
        "jerusalem artichoke",
        "jicama",
        "kale",
        "kidney bean",
        "kohlrabi",
        "lavender",
        "leek ",
        "legume",
        "lemon grass",
        "lentils",
        "lettuce",
        "lima bean",
        "mamey",
        "mangetout",
        "marjoram",
        "mung bean",
        "mushroom",
        "mustard green",
        "navy bean",
        "new zealand spinach",
        "nopale",
        "okra",
        "onion",
        "oregano",
        "paprika",
        "parsley",
        "parsnip",
        "patty pan",
        "pea",
        "pinto bean",
        "potato",
        "pumpkin",
        "radicchio",
        "radish",
        "rhubarb",
        "rosemary",
        "runner bean",
        "rutabaga",
        "sage",
        "scallion",
        "shallot",
        "skirret",
        "snap pea",
        "soy bean",
        "spaghetti squash",
        "spinach",
        "squash",
        "sweet potato",
        "tabasco pepper",
        "taro",
        "tat soi",
        "thyme",
        "topinambur",
        "tubers",
        "turnip",
        "wasabi",
        "water chestnut",
        "watercress",
        "white radish",
        "yam",
        "zucchini"
    ]

for word in fruits:
    T.insert(word.lower())
for word in vegetables:
    T.insert(word.lower())
# for word in english_words_set:
#     T.insert(word.lower())

#phrase_to_find = "for this author, an age old saying comes to mind: " \
#                 "westward ho! i made the journey without much of a " \
#                 "problem. no need for any concern. en route, i read a " \
#                 "book by sun tzu, which did shape a school of thought: " \
#                 "militarism and war, in earnest, is the last thing " \
#                 "i seek. I prefer the farmer's life, which is, one could " \
#                 "argue, a vastly easier existence. each day consists " \
#                 "of keeping barn, an acre of crops and six crows. " \
#                 "my main goals, are perhaps plenty ambitious: " \
#                 "raise individual prized heifers and plant an inordinate " \
#                 "amount of wheat. also, i've learned that for the " \
#                 "rancher, dry seasons can be costly. but i have been " \
#                 "able to grasp easily the benefits of irrigation"

phrase_to_find = "main goals, are perhaps plenty ambitious: " \
                "raise individual prized heifers and plant an inordinate " \
                "amount of wheat. also, i've learned that for the " \
                "rancher, dry seasons can be costly. but i have been " \
                "able to grasp easily the benefits of irrigation"

regex = re.compile('[^a-zA-Z]')

txt = regex.sub("", phrase_to_find)
print(txt)

for word in fruits:
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            new_word = word[:i] + letter + word[i:]
            if new_word in txt:
                print(new_word)

current_words = None

find_word(phrase_to_find)
