"""
Widget de map
"""
import json
import re
import time
from copy import deepcopy, copy
from tkinter import *
import enchant

time_wait = 0
words = [
    "flightcrew",
    "palindrome",
    "transfixed",
    "labyrinths"
]
d = enchant.Dict("en_US")

class TabObject():
    tab = None
    sums = [17, 16, 17, 22, 13, 14, 6, 24, 27, 24]
    found_answers = None

    def __init__(self, tab, found_answers):
        self.tab = tab
        self.found_answers = found_answers

    def get_positions(self):
        found_words = {'0': "", '1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""}

        for tab_y in range(len(self.tab)):
            for tab_x in range(len(self.tab[tab_y])):
                answer = self.tab[tab_y][tab_x]
                number = answer[0]
                x = answer[2]
                y = answer[3]
                found_words[str(number)] += words[y][x]
        for number, word in found_words.items():
            print("{} : {}".format(number, word))
            if d.check(word):
                print("exists !")

    def all_routines(self):
        stop = True
        ret = self.routine_1()
        if ret:
            stop = False
            time.sleep(time_wait)

        ret = self.routine_2(self.found_answers)
        if ret:
            stop = False
            time.sleep(time_wait)

        ret = self.routine_3()
        if ret:
            stop = False
            time.sleep(time_wait)

        ret = self.search_case()
        if ret:
            stop = False
            time.sleep(time_wait)

        return stop

    def get_fewer_possibilities(self):
        possibilities = []
        len_pos = 9
        for tab_y in range(len(self.tab)):
            for tab_x in range(len(self.tab[tab_y])):
                case = self.tab[tab_y][tab_x]
                if case[2] and len_pos > len(case[1]) > 1:
                    len_pos = len(case[1])
                    possibilities = [(tab_x, tab_y)]
                elif case[2] and len(case[1]) == len_pos:
                    possibilities.append((tab_x, tab_y))
        return possibilities

    def routine_1(self):
        modified = False
        for line in self.tab:
            ret = self.routine_1_line(line)
            if ret:
                modified = True
        return modified

    def routine_1_line(self, line):
        modified = False
        counts = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        found_cases = set()
        for case in line:
            if case[0] != None:
                found_cases.add(case[0])

            for possibility in case[1]:
                counts[str(possibility)] += 1
        if min(counts.values()) != 1 and not len(found_cases):
            return False
        only_ones = []
        for possibility, count in counts.items():
            if count == 0:
                raise Exception("rsudoku_error")
            elif count == 1:
                only_ones.append(int(possibility))

        for case in line:
            if len(case[1]) > 1:
                new_possibilities = case[1].difference(found_cases)
                if len(new_possibilities) != len(case[1]):
                    case[1] = new_possibilities
                    modified = True
            else:
                for only_one in only_ones:
                    if case[0] == None and only_one in case[1]:
                        self.find_case(case, only_one)
                        modified = True

        return modified

    def routine_2(self, cases):
        modified = False
        for case in cases:
            if case[0] == None:
                continue

            cases_to_check = []
            x, y = (case[2], case[3])

            if x > 0 and y > 0:
                cases_to_check.append(self.tab[y - 1][x - 1])
                cases_to_check.append(self.tab[y - 1][x])
                cases_to_check.append(self.tab[y][x - 1])

            if x < 9 and y < 3:
                cases_to_check.append(self.tab[y + 1][x + 1])
                cases_to_check.append(self.tab[y + 1][x])
                cases_to_check.append(self.tab[y][x + 1])

            if x > 0 and y < 3:
                cases_to_check.append(self.tab[y + 1][x - 1])

            if x < 9 and y > 0:
                cases_to_check.append(self.tab[y - 1][x + 1])

            for case_to_check in cases_to_check:
                if case[0] in case_to_check[1]:
                    modified = True
                    case_to_check[1].remove(case[0])
        return modified

    def routine_3(self):
        for i in range(10):
            sum_to_get = self.sums[i]

            col = [line[i] for line in self.tab]

            self.routine_3_by_col(col, sum_to_get)

    def routine_3_by_col(self, col, sum_to_get):
        succeed = [set(), set(), set(), set()]

        for poss_0 in col[0][1]:
            for poss_1 in col[1][1]:
                for poss_2 in col[2][1]:
                    for poss_3 in col[3][1]:
                        if poss_0 + poss_1 + poss_2 + poss_3 == sum_to_get:
                            succeed[0].add(poss_0)
                            succeed[1].add(poss_1)
                            succeed[2].add(poss_2)
                            succeed[3].add(poss_3)

        if len(succeed[0]) != len(col[0][1]) or len(succeed[1]) != len(col[1][1]) or len(succeed[2]) != len(col[2][1]) or len(succeed[3]) != len(col[3][1]):
            modified = True

            col[0][1] = succeed[0]
            col[1][1] = succeed[1]
            col[2][1] = succeed[2]
            col[3][1] = succeed[3]
        if not len(col[0][1]):
            raise Exception("r3_error")


    def search_case(self):
        modified = False
        for line in self.tab:
            for case in line:
                if len(case[1]) == 1 and case[0] == None:
                    modified = True
                    self.find_case(case, list(case[1])[0])
        return modified

    def find_case(self, case, value):
        case[0] = value
        case[1] = {value}
        self.found_answers.append(case)
        self.routine_2([case])


class TabIHM(Frame):
    tab_object = None
    txt_variables = []
    digits = set([i for i in range(0, 10)])


    def __init__(self, root, load_from_json=False):
        """
        Widget de map
        :param root: Parent de la map
        :param tab:
        """
        Frame.__init__(self, root)

        max_hauteur = 4
        max_largeur = 10
        # if load_from_json:
        #    with open('tab.json') as f:
        #        self.tab=json.loads(f.read())
        #    for line in self.tab:
        #        for case in line:
        #            if case and isinstance(case[1], list):
        #                case[1] = set(case[1])
        # else:
        tab = [
            [[None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [2, {2}],               [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)]],
            [[None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [0, {0}],               [None, copy(self.digits)], [None, copy(self.digits)], [6, {6}]],
            [[None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [7, {7}],               [None, copy(self.digits)], [4, {4}]],
            [[None, copy(self.digits)], [9, {9}],               [4, {4}],               [3, {3}],               [0, {0}],               [1, {1}],               [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)], [None, copy(self.digits)]],
        ]

        found_answers = []
        for tab_y in range(max_hauteur):
            txt_variables_line = []
            for tab_x in range(max_largeur):
                var = StringVar()

                case = tab[tab_y][tab_x]
                case.append(tab_x)
                case.append(tab_y)

                case_frame = Frame(self, borderwidth=0.5, relief=RAISED)

                case_label = ""

                if case[0] == None:
                    if len(case[1]) > 3:
                        case_label += ' '
                    else:
                        for possibility in case[1]:
                            case_label += str(possibility) + ','
                else:
                    found_answers.append(case)
                    case_label += str(case[0])

                fontsize = 15
                var.set(case_label)

                case_widget = Frame(case_frame)  # border
                case_label = Label(case_widget, textvariable=var, font=('Helvatical bold', fontsize))
                case_label.pack(fill=BOTH, expand=YES)

                txt_variables_line.append(var)
                case_widget.pack(fill=BOTH, expand=YES)
                case_frame.grid(row=tab_y, column=tab_x, sticky="nsew")

            self.txt_variables.append(txt_variables_line)
        self.tab_object = TabObject(tab, found_answers)
        for i in range(max_hauteur):
            self.grid_rowconfigure(i, weight=1)
        for i in range(max_largeur):
            self.grid_columnconfigure(i, weight=1)

    def resolve(self, tab_object=None):
        if not tab_object:
            tab_object = self.tab_object

        try:
            stop = False
            while not stop:
                stop = tab_object.all_routines()
                self.update_tab(tab_object.tab, full_mode=True)
            print(len(tab_object.found_answers))
            if len(tab_object.found_answers) == 40:
                print("found ! ")
                tab_object.get_positions()
                self.mainloop()
                return True
            cases = tab_object.get_fewer_possibilities()
            for x, y in cases:
                case = tab_object.tab[y][x]
                i = 0
                while i < len(case[1]):
                    possibility = list(case[1])[i]
                    new_tab = deepcopy(tab_object.tab)
                    new_answers = deepcopy(tab_object.found_answers)

                    new_tab_object = TabObject(new_tab, new_answers)
                    new_tab_object.find_case(new_tab[y][x], possibility)
                    ret = self.resolve(new_tab_object)
                    if not ret:
                        case[1].remove(possibility)
                    else:
                        i += 1

        except Exception as e:
            if re.match("r.*_error$", e.__str__()):
                print(e.__str__())
                return False
            else:
                raise e

    def update_tab(self, tab=None, full_mode=False):
        if not tab:
            tab = self.tab_object.tab

        max_hauteur = 4
        max_largeur = 10
        for tab_y in range(max_hauteur):
            for tab_x in range(max_largeur):
                case = tab[tab_y][tab_x]

                case_label = ""

                if case[0] == None:
                    if len(case[1]) > 5 and not full_mode:
                        case_label += ' '
                    else:
                        for possibility in case[1]:
                            case_label += str(possibility) + ','
                else:
                    case_label += str(case[0])

                self.txt_variables[tab_y][tab_x].set(case_label)

        self.update_idletasks()
        self.update()

    # def saveTab(self):
    #     new_tab = deepcopy(self.tab)
    #     open('tab.json', 'w').close()
    # 
    #     for line in new_tab:
    #         for case in line:
    #             if case and isinstance(case[0], int) and isinstance(case[1], set):
    #                 case[1] = list(case[1])
    #     with open('tab.json', 'a') as f:
    #         f.write(json.dumps(new_tab))

    # def end_routines(self, tab_object):
    #     ret = self.tab_object.routine6()
    #     if not ret:
    #         return False
    #     ret = self.tab_object.routine_10()
    #     if not ret:
    #         return False
    #     print(tab_object.found_letters)
    # 
    #     print("routine7 ok")
    #     ret = self.tab_object.routine_11()
    #     if not ret:
    #         return False
    # 
    #     self.tab_object.routine_1()
    # 
    #     raise Exception("tab found !")
