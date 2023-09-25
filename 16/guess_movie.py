import json
import re
import time
import itertools, enchant


import requests
from bs4 import BeautifulSoup

figures = [
    ["ADELNORSY", (5, 1), (6, 1)],
    ["EEHINSTX", (5, 4), (5, 1)],
    ["RSTTYY", (5, 4), (5, 1)],
    ["ACEIRSS", (3, 3), (6, 4)],
    ["AABEMNNRRSU", (7, 3), (6, 3)],
    #["BEIILMMNOOPSSSS", (10, 7), (7, 5)],
    ["AGGHMNRDU", (5, 4), (6, 5)],
]

def get_movies_from_website():
    movie_names = []
    for year in range(1993, 2023, 1):
        print("year {}".format(year))
        response = requests.get("https://www.boxofficemojo.com/year/{}/".format(year))
        html_response = response.text

        attrs = {
            'href': re.compile(r'\/release\/rl\d{1,}\/\?ref\_\=bo_yld_table_\d{1,}'),
            'class': "a-link-normal"
        }

        soup = BeautifulSoup(html_response, 'html.parser')
        tracks = soup.find_all('a', attrs=attrs)
        movie_names_by_year = [a.getText() for a in tracks]
        movie_names.append(movie_names_by_year)
        time.sleep(1)
    print(movie_names)
    open("movies_webstite_brut.txt").close()
    with open("movies_webstite_brut.txt", 'a', encoding='utf-8') as f:
        for movies_by_year in movie_names:
            for movie in movies_by_year:
                f.write(movie+'\n')
    return movie_names


def get_movies_brut():
    open("movies_webstite.txt").close()
    with open("movies_webstite_brut.txt") as brut:
        data = brut.readlines()

    with open("movies.txt", 'a', encoding='utf-8') as f:
        f.write()
    return data

def get_movies():
    with open("movies_webstite.txt") as f:
        data = f.readlines()
    return data

#def get_movies():
#    open("movies.txt", "w").close()
#    pattern = r'(?P<name>(.*) \((?P<year>\w+)\)'
#
#    with open("movies.json", encoding='utf-8') as f:
#        data = json.load(f)
#
#    movies = []
#
#    for line in data["popular-movies"]:
#        new_line = line.lower()
#        matches = re.match(pattern, new_line)
#        movies.append(matches["name"])
#    return movies


def filter_movies():
    movies = get_movies()
    filtered_movies = []
    for movie in movies:
        movie_name = movie.lower().replace('\n', '')
        movie_name = movie_name.replace('  ', ' ')
        movie_name = movie_name.replace('  ', ' ')
        pattern = r'[^A-Za-z ]+'
        movie_name = re.sub(pattern, '', movie_name)

        print(movie_name)
        movie_words = movie_name.split(' ')
        if movie_words[0] == 'the':
            movie_words.remove(movie_words[0])


        if len(movie_words) != 2:
            continue

        lettres_en_commun = []
        for letter in movie_words[0]:
            if letter in movie_words[1]:
                lettres_en_commun.append(letter)

        if not len(lettres_en_commun):
            continue



        filtered_movies.append([movie_words, lettres_en_commun])

    return filtered_movies

def find_movies(movies):
    print(movies)
    for puzzle in figures:
        print('--------------- {} ------------------'.format(puzzle[0]))
        (length_y, pos_y) = puzzle[1]
        (length_x, pos_x) = puzzle[2]
        print(length_y, length_x)
        print(pos_y, pos_x)

        for movie_name_array in [movie[0] for movie in movies]:

            if len(movie_name_array[0]) == length_y and len(movie_name_array[1]) == length_x:
                figure_y = movie_name_array[0]
                figure_x = movie_name_array[1]
            elif len(movie_name_array[1]) == length_y and len(movie_name_array[0]) == length_x:
                figure_y = movie_name_array[1]
                figure_x = movie_name_array[0]
            else:
                continue


            letters = figure_y[:(pos_y-1)] + figure_y[(pos_y):] + figure_x[:(pos_x-1)] + figure_x[(pos_x):]

            if ''.join(sorted(letters)) == puzzle[0].lower():
                print("movie found ! {} {}".format(movie_name_array[0], movie_name_array[1]))
            #movie_full_name = movie_name_array[0]+movie_name_array[1]
            #different_letters = 0
            #movie_letters = pos_[:]



def search_in_dicts(word):
    #for dict in dictionnaries.items():
    #    if dict[1].check(word):
    #        return dict
    if d.check(word):
        return True
    return False

def guess_movie(movie_array, word_1, word_2, letter):
    if word_1 and word_2:
        return word_1+word_2
    letters = movie_array[0].lower()
    (length_y, pos_y) = movie_array[1]
    (length_x, pos_x) = movie_array[2]
    i = 0
    ret = False
    for anagram in ["".join(perm) for perm in itertools.permutations(letters)]:
        new_word_a_1 = anagram[:pos_y]


movies = filter_movies()
find_movies(movies)
