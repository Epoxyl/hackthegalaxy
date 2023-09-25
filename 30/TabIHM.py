"""
Widget de map
"""
import json
import re
import time
from copy import deepcopy, copy
from tkinter import *


class TabObject():
    tab = []

    letters_positions = {'A': (4, 0), 'B': (6, 0), 'C': (8, 0), 'D': (0, 1), 'E': (2, 1), 'F': (4, 1), 'G': (3, 2),
                         'H': (7, 2),
                         'I': (1, 3), 'J': (5, 3), 'K': (8, 3), 'L': (2, 4), 'M': (6, 4), 'N': (0, 5), 'O': (3, 5),
                         'P': (7, 5),
                         'Q': (1, 6), 'R': (5, 6), 'S': (4, 7), 'T': (6, 7), 'U': (8, 7), 'V': (0, 8), 'W': (2, 8),
                         'X': (4, 8)}

    found_letters = {}
    letters_cases = {}

    def __init__(self, tab, found_letters=None):
        self.tab = tab
        if found_letters:
            self.found_letters = found_letters

        for tab_x, tab_y in self.letters_positions.values():
            case = self.tab[tab_y][tab_x]
            self.letters_cases[case[2]] = tab[tab_y][tab_x]

    def find_case(self, case, value):
        if case[0]:
            return False

        case[0] = value
        case[1] = {value}
        if case[2]:
            self.found_letters[case[2]] = value

    def routine_sudoku(self):
        cols = [[], [], [], [], [], [], [], [], []]
        for line in self.tab:
            self.routine_sudoku_line(line)
            for x in range(len(line)):
                cols[x].append(line[x])

        for col in cols:
            self.routine_sudoku_line(col)

    def routine_sudoku_line(self, line):
        modified = False
        counts = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        found_cases = set()
        for case in line:
            if case[0]:
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
                    if not case[0] and only_one in case[1]:
                        self.find_case(case, only_one)
                        modified = True

        return modified

    def routine1(self):
        case_M = self.letters_cases['M']
        modified = False
        for value in [3, 6, 9]:
            if value in case_M[1]:
                case_M[1].remove(value)
                modified = True
        return modified

    def routine2(self):
        for case in self.letters_cases.values():
            if case[2] and case[2] in self.found_letters.keys():
                self.routine2_by_case(case, case[3], case[4])

    def routine2_by_case(self, case, x, y):
        if case[0] != 4:
            return False

        cases = []
        if x > 0 and y > 0:
            cases.append(self.tab[y - 1][x - 1])

        if x < 8 and y < 8:
            cases.append(self.tab[y + 1][x + 1])

        if x > 0 and y < 8:
            cases.append(self.tab[y + 1][x - 1])

        if x < 8 and y > 0:
            cases.append(self.tab[y - 1][x + 1])
        not_a_four_number = 0
        for diagonal in cases:
            if not diagonal[2]:
                continue
            elif diagonal[0] == 4:
                return False
            elif (diagonal[0] and diagonal[0] != 4) or 4 not in diagonal[1]:
                not_a_four_number += 1
        if not_a_four_number == len(cases) - 1:
            for diagonal in cases:
                if not diagonal[0] and 4 in diagonal[1]:
                    self.find_case(diagonal, 4)
                    return True
        elif not_a_four_number == len(cases):
            raise Exception("r6_error")
        else:
            return False

    def routine3(self):
        case_B = self.letters_cases['B']
        case_R = self.letters_cases['R']

        if case_R[0] and case_B[0] and case_B[0] != case_R[0]:
            raise Exception("r3_error")
        elif case_R[0] and case_B[0]:
            return False

        intersec = case_B[1].intersection(case_R[1])
        number_possibilities = len(intersec)
        modified = False
        if number_possibilities == 1:
            self.find_case(case_B, list(intersec)[0])
            self.find_case(case_R, list(intersec)[0])
            modified = True
        if number_possibilities != len(case_R[1]) or number_possibilities != len(case_B[1]):
            case_B[1] = intersec
            case_R[1] = copy(intersec)
            modified = True

        for letter, value in self.found_letters.items():
            if letter not in ['B', 'R']:
                if value in case_B[1]:
                    case_B[1].remove(value)
                    modified = True
                if value in case_R[1]:
                    case_R[1].remove(value)
                    modified = True
        if not len(case_B) or not len(case_R):
            raise Exception("r3-2_error")

        return modified

    def routine4(self):
        case_T = self.letters_cases['T']
        case_U = self.letters_cases['U']
        case_C = self.letters_cases['C']

        T_possibilities = {case_T[0]} if case_T[0] else case_T[1]
        U_possibilities = {case_U[0]} if case_U[0] else case_U[1]
        C_possibilities = {case_C[0]} if case_C[0] else case_C[1]

        T_succeed = set()
        U_succeed = set()
        C_succeed = set()

        max_t_u = max(T_possibilities) + max(U_possibilities)

        modified = False
        for t in T_possibilities:
            for u in U_possibilities:
                for c in C_possibilities:
                    if 4 * c <= max_t_u and t + u == 4 * c:
                        T_succeed.add(t)
                        U_succeed.add(u)
                        C_succeed.add(c)

        if len(T_succeed) != len(case_T[1]) or len(U_succeed) != len(case_U[1]) or len(C_succeed) != len(case_C[1]):
            modified = True

            case_T[1] = T_succeed
            case_U[1] = U_succeed
            case_C[1] = C_succeed
        if not len(case_T[1]):
            raise Exception("r4_error")

        return modified

    def routine5(self):
        modified = False
        for letter, case in self.letters_cases.items():
            position_y = case[4]
            if position_y + 1 in case[1]:
                case[1].remove(position_y + 1)
                modified = True

        return modified

    def routine6(self):
        answers = list(self.found_letters.values())
        if len(answers) == 24:
            if not (answers.count(1) == answers.count(2) == answers.count(9)):
                raise Exception("r6_error")

            if not (answers.count(3) == answers.count(4) == answers.count(5) == answers.count(8)):
                raise Exception("r6_error")

            if not (answers.count(7) > answers.count(6)):
                raise Exception("r6_error")
        else:
            pass
            counts = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
            for letter, value in self.found_letters.items():
                counts[str(value)] += 1

        return True

    def routine7(self):
        line_5, line_7, line_6 = self.tab[4], self.tab[6], self.tab[5]

        modified = False
        max_value = 0
        for case in line_5:
            if case[2]:
                possibilities = case[1]
                for possibility in list(possibilities):
                    if possibility <= max_value:
                        possibilities.remove(possibility)
                        modified = True
                if len(possibilities):
                    max_value = min(possibilities)
                else:
                    raise Exception("r7_error")

        max_value = 0
        for case in line_7:
            if case[2]:
                possibilities = case[1]
                for possibility in list(possibilities):
                    if possibility <= max_value:
                        possibilities.remove(possibility)
                        modified = True
                if len(possibilities):
                    max_value = min(possibilities)
                else:
                    raise Exception("r7_error")

        min_value = 10
        for case in line_6:
            if case[2]:
                possibilities = case[1]
                for possibility in list(possibilities):
                    if possibility >= min_value:
                        possibilities.remove(possibility)
                        modified = True
                if len(possibilities):
                    min_value = max(possibilities)
                else:
                    raise Exception("r7_error")
        return modified

    def routine8(self):
        if 'F' in self.found_letters:
            return False

        modified = False
        others = self.found_letters.values()
        case_F = self.letters_cases['F']
        case_K = self.letters_cases['K']
        case_Q = self.letters_cases['Q']
        for other in others:
            if other in case_F[1]:
                case_F[1].remove(other)
                modified = True

        if not len(case_F[1]):
            raise Exception("r8_error")

        possibilities_F = set()
        possibilities_K = set()
        possibilities_Q = set()
        for k_possibility in case_K[1]:
            for q_possibility in case_Q[1]:
                for f_possibility in case_F[1]:
                    if q_possibility + k_possibility == f_possibility:
                        possibilities_F.add(f_possibility)
                        possibilities_K.add(k_possibility)
                        possibilities_Q.add(q_possibility)

        if not len(possibilities_F):
            raise Exception("r8-2_error")

        if len(possibilities_F) != len(case_F[1]) or len(possibilities_K) != len(case_K[1]) or len(
                possibilities_Q) != len(case_Q[1]):
            modified = True
        case_F[1] = possibilities_F
        case_K[1] = possibilities_K
        case_Q[1] = possibilities_Q

        return modified

    def routine9(self):
        modified = False
        case_T = self.letters_cases['T']
        letters = {'J', 'O', 'K', 'M', 'P', 'R', 'S', 'X', 'U'}
        if len(case_T[1]) == 1:
            value = list(case_T[1])[0]
            for letter in letters:
                case = self.letters_cases[letter]
                if value in case[1]:
                    case[1].remove(value)
                    modified = True
                if not len(case[1]):
                    raise Exception("r9_error")
            return modified

        found_letters = letters.intersection(self.found_letters.keys())
        for letter in found_letters:
            value = self.found_letters[letter]
            if value in case_T[1]:
                case_T[1].remove(value)
                modified = True

        if not len(case_T[1]):
            raise Exception("r9-2_error")
        return modified

    def routine10(self):

        sum_col = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        sum_line = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for letter, case in self.letters_cases.items():
            pos_x = case[3]
            pos_y = case[4]
            sum_col[pos_x] += case[0]
            sum_line[pos_y] += case[0]

        if 24 in sum_line and 25 in sum_col:
            return True
        else:
            raise Exception("r10_error")

    def routine11(self):
        counts = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        return False
        # for letter, value in self.found_letters.items():
        #    counts[str(value)] += 1

    #
    # if len(self.found_letters.keys()) == 24:
    #    if 1 in counts.values() and 2 in counts.values() and 3 in counts.values() and 4 in counts.values():
    #        return True
    #    else:
    #        raise Exception("r11_error")
    # elif len(self.found_letters.keys()) == 23:
    #    count_missing = []
    #    found_letters_missing = 24 - len(self.found_letters.keys)
    #    for i in [1, 2, 3, 4]
    #        if i in counts.values():
    #            count_missing.append(i)
    #    if found_letters_missing == len(count_missing):
    #        possibilities = []
    #        for value, count in counts.items():
    #            if count + 1 in count_missing:

    def all_routines(self):
        stop = False
        while not stop:
            stop = True

            ret = self.routine2()
            if ret:
                stop = False
            ret = self.routine3()
            if ret:
                stop = False
            ret = self.routine4()
            if ret:
                stop = False

            ret = self.routine7()
            if ret:
                stop = False
            ret = self.routine8()
            if ret:
                stop = False
            ret = self.routine9()
            if ret:
                stop = False

            self.search_case()

    def search_case(self):
        for tab_x, tab_y in self.letters_positions.values():
            case = self.tab[tab_y][tab_x]
            if len(case[1]) == 1 and not case[0]:
                self.find_case(case, list(case[1])[0])

    def get_fewer_possibilities(self):
        possibilities = []
        len_pos = 8
        for tab_x, tab_y in self.letters_positions.values():
            case = self.tab[tab_y][tab_x]
            if case[2] and len_pos > len(case[1]) > 1:
                len_pos = len(case[1])
                possibilities = [(tab_x, tab_y)]
            elif case[2] and len(case[1]) == len_pos:
                possibilities.append((tab_x, tab_y))
        return possibilities


class TabIHM(Frame):
    tab_object = None
    txt_variables = []
    digits = set([i for i in range(1, 10)])

    found_answers = []

    def __init__(self, root, load_from_json=False):
        """
        Widget de map
        :param root: Parent de la map
        :param tab:
        """
        Frame.__init__(self, root)

        max_hauteur = 9
        max_largeur = 9
        # if load_from_json:
        #    with open('tab.json') as f:
        #        self.tab=json.loads(f.read())
        #    for line in self.tab:
        #        for case in line:
        #            if case and isinstance(case[1], list):
        #                case[1] = set(case[1])
        # else:
        tab = [
            [[0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), None],
             [0, copy(self.digits), None], [0, copy(self.digits), 'A'], [0, copy(self.digits), None],
             [0, copy(self.digits), 'B'], [0, copy(self.digits), None], [0, copy(self.digits), 'C']],
            [[0, copy(self.digits), 'D'], [0, copy(self.digits), None], [0, copy(self.digits), 'E'],
             [0, copy(self.digits), None], [0, copy(self.digits), 'F'], [0, copy(self.digits), None],
             [0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), None]],
            [[0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), None],
             [0, copy(self.digits), 'G'], [0, copy(self.digits), None], [0, copy(self.digits), None],
             [0, copy(self.digits), None], [0, copy(self.digits), 'H'], [0, copy(self.digits), None]],
            [[0, copy(self.digits), None], [0, copy(self.digits), 'I'], [0, copy(self.digits), None],
             [0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), 'J'],
             [0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), 'K']],
            [[0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), 'L'],
             [0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), None],
             [0, copy(self.digits), 'M'], [0, copy(self.digits), None], [0, copy(self.digits), None]],
            [[0, copy(self.digits), 'N'], [0, copy(self.digits), None], [0, copy(self.digits), None],
             [0, copy(self.digits), 'O'], [0, copy(self.digits), None], [0, copy(self.digits), None],
             [0, copy(self.digits), None], [0, copy(self.digits), 'P'], [0, copy(self.digits), None]],
            [[0, copy(self.digits), None], [0, copy(self.digits), 'Q'], [0, copy(self.digits), None],
             [0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), 'R'],
             [0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), None]],
            [[0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), None],
             [0, copy(self.digits), None], [0, copy(self.digits), 'S'], [0, copy(self.digits), None],
             [0, copy(self.digits), 'T'], [0, copy(self.digits), None], [0, copy(self.digits), 'U']],
            [[0, copy(self.digits), 'V'], [0, copy(self.digits), None], [0, copy(self.digits), 'W'],
             [0, copy(self.digits), None], [0, copy(self.digits), 'X'], [0, copy(self.digits), None],
             [0, copy(self.digits), None], [0, copy(self.digits), None], [0, copy(self.digits), None]]
        ]
        letters_positions = {}
        letters_line = {}
        for tab_y in range(max_hauteur):
            txt_variables_line = []
            for tab_x in range(max_largeur):
                var = StringVar()

                case = tab[tab_y][tab_x]
                case.append(tab_x)
                case.append(tab_y)

                case_frame = Frame(self, borderwidth=0.5, relief=RAISED)

                case_label = ""
                if case[2]:
                    print("{}: {}".format(case[2], case[1]))

                    case_label += str(case[2]) + ':'
                    letters_positions[case[2]] = (tab_x, tab_y)
                    if tab_y not in letters_line.keys():
                        letters_line[tab_y] = []

                if case[0] == 0:
                    if len(case[1]) > 3:
                        case_label += ' '
                    else:
                        for possibility in case[1]:
                            case_label += str(possibility) + ','
                else:
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
        self.tab_object = TabObject(tab)
        for i in range(max_hauteur):
            self.grid_rowconfigure(i, weight=1)
        for i in range(max_largeur):
            self.grid_columnconfigure(i, weight=1)

    def resolve(self, tab_object=None):
        if not tab_object:
            tab_object = self.tab_object
            tab_object.routine1()
            tab_object.routine5()

        try:
            tab_object.all_routines()
            self.update_tab(tab_object.tab)
            self.mainloop()
            return
            if len(tab_object.found_letters.keys()) == 24:
                self.end_routines(tab_object)
                return True
            cases = tab_object.get_fewer_possibilities()
            for x, y in cases:
                case = tab_object.tab[y][x]
                i = 0
                while i < len(case[1]):
                    possibility = list(case[1])[i]
                    new_tab = deepcopy(tab_object.tab)
                    new_found_letters = deepcopy(tab_object.found_letters)
                    new_found_letters[case[2]] = possibility
                    new_tab[y][x][0] = possibility
                    new_tab[y][x][1] = {possibility}
                    new_tab_object = TabObject(new_tab, new_found_letters)
                    ret = self.resolve(new_tab_object)
                    if not ret:
                        case[1].remove(possibility)
                    else:
                        i += 1
            return False
        except Exception as e:
            if re.match("r.*_error$", e.__str__()):
                return False
            else:
                raise e

    def update_tab(self, tab=None, full_mode=False):
        if not tab:
            tab = self.tab_object.tab

        max_hauteur = 9
        max_largeur = 9
        for tab_y in range(max_hauteur):
            for tab_x in range(max_largeur):
                case = tab[tab_y][tab_x]

                case_label = ""
                if case[2]:
                    case_label += str(case[2]) + ':'

                if case[0] == 0:
                    if len(case[1]) > 5 and not case[2] and not full_mode:
                        case_label += ' '
                    else:
                        for possibility in case[1]:
                            case_label += str(possibility) + ','
                else:
                    case_label += str(case[0])

                self.txt_variables[tab_y][tab_x].set(case_label)

        self.update_idletasks()
        self.update()

    def saveTab(self):
        new_tab = deepcopy(self.tab)
        open('tab.json', 'w').close()

        for line in new_tab:
            for case in line:
                if case and isinstance(case[0], int) and isinstance(case[1], set):
                    case[1] = list(case[1])
        with open('tab.json', 'a') as f:
            f.write(json.dumps(new_tab))

    def end_routines(self, tab_object):
        ret = self.tab_object.routine6()
        if not ret:
            return False
        ret = self.tab_object.routine10()
        if not ret:
            return False
        print(tab_object.found_letters)

        print("routine7 ok")
        ret = self.tab_object.routine11()
        if not ret:
            return False

        self.tab_object.routine_sudoku()

        self.found_answers.append(tab_object.found_letters)
        raise Exception("tab found !")
