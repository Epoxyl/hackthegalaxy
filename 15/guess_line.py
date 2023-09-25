import itertools, enchant
import csv
import json
import re

from os.path import exists


words_couples = [
    ["imported", "dealer"],
    ["biter", "aortic"],
    ["sunday", "manger"],

    ["auteurs", "sari"],
    ["morose", "orca"],
    ["crashed", "tome"],
    ["holier", "steam"],
    ["overlit", "genoa"],
    ["meshier", "snooped"],
    ["eruption", "hydrogen"],

]




def json_to_text(file_name):
    open("{}.txt".format(file_name), "w").close()
    print(file_name)
    pattern = r'[^A-Za-z]+'

    with open("{}.json".format(file_name), encoding='utf-8') as f:
        data = json.load(f)

    open("{}.txt".format(file_name)).close()
    with open("{}.txt".format(file_name), 'a', encoding='utf-8') as f:
        for line in data[file_name]:
            new_line = line.lower()
            new_line = re.sub(pattern, '', new_line)
            f.write(new_line+'\n')

def get_dictionnaries():
    dicts = {}
    for dict_name in ["cheeses", "dogs", "birthstones", "astrological_signs", "countries", "greek_gods", "santas_reindeers", "colors", "nato_alphabet"]:
        if exists("{}.txt".format(dict_name)):
            dicts[dict_name] = enchant.request_pwl_dict("{}.txt".format(dict_name))
        else:
            if exists("{}.json".format(dict_name)):
                json_to_text(dict_name)
                dicts[dict_name] = enchant.request_pwl_dict("{}.txt".format(dict_name))
            else:
                print("{} not exists".format(dict_name))
    return dicts

def merge_disctionnaries():
    open("merge.txt").close()

    with open('merge.txt', 'w') as outfile:
        for dict_name in ["cheeses", "dogs", "birthstones", "astrological_signs", "countries", "greek_gods", "santas_reindeers", "colors", "nato_alphabet"]:
            print(dict_name)
            if exists("{}.txt".format(dict_name)):
                #json_to_text(dict_name)
                with open("{}.txt".format(dict_name), 'r', encoding='utf-8') as infile:
                    for line in infile:
                        outfile.write(line)
            else:
                print("{} not exists".format(dict_name))


def search_in_dicts(word):
    #for dict in dictionnaries.items():
    #    if dict[1].check(word):
    #        return dict
    if d.check(word):
        return True
    return False

def return_left_words_by_dictionnary(left_word, right_word):

    tested_letters = []
    words_found = []
    for letter in left_word:
        if letter in tested_letters:
            continue

        letters = right_word + letter
        print("testing letter {}".format(letter))
        for word in ["".join(perm) for perm in itertools.permutations(letters)]:
            if word in words_found:
                continue
            ret = search_in_dicts(word)
            if ret:
                print("{} trouvé dans le dict".format(word))
                words_found.append([letter, word])
                #if try_letters([left_word, letter, word, right_word]):
                #    return True
            tested_letters.append(letter)

    return words_found

def try_letters(ok_letter):
    print(ok_letter)
    left_word = ok_letter[0]
    letter = ok_letter[1]
    found_word = ok_letter[2]
    right_word = ok_letter[3]
    letters = left_word + letter
    print(letters)
    for word in ["".join(perm) for perm in itertools.permutations(letters)]:
        if search_in_dicts(word):
            print("found : {}, {}, {}, {}, {}".format(left_word, word, letter, found_word, right_word))
            with open("reponses.txt", 'a') as f:
                f.write("found : {}, {}, {}, {}, {}".format(left_word, word, letter, found_word, right_word))
                return True
    print("lettre {} ne fonctionne pas avec {}".format(letter, left_word))


#dictionnaries = get_dictionnaries()
#merge_disctionnaries()
#print(dictionnaries)
d = enchant.request_pwl_dict("merge.txt")
print(d)
for words_couple in words_couples:
    print(return_left_words_by_dictionnary(words_couple[0], words_couple[1]))



#ok_letters = [['dogs', 'eruption', 't', 'greyhound', 'hydrogen']]
