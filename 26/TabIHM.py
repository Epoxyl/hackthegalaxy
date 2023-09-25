"""
Widget de map
"""
import json
import time
from copy import deepcopy
from tkinter import *


class TabIHM(Frame):
    tab = []
    digits = [i for i in range(1, 10)]

    txt_variables = []

    def __init__(self, root, load_from_json=False):
        """
        Widget de map
        :param root: Parent de la map
        :param tab:
        """
        Frame.__init__(self, root)

        max_hauteur = 9
        max_largeur = 9
        if load_from_json:
            with open('tab.json') as f:
                self.tab=json.loads(f.read())
            for line in self.tab:
                for case in line:
                    if case and isinstance(case[1], list):
                        case[1] = set(case[1])
        else:
            self.tab = [
                [[0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], ['A', self.digits], [0, self.digits], ['B', self.digits], [0, self.digits], ['C', self.digits]],
                [['D', self.digits], [0, self.digits], ['E', self.digits], [0, self.digits], ['F', self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits]],
                [[0, self.digits], [0, self.digits], [0, self.digits], ['G', self.digits], [0, self.digits], [0, self.digits], [0, self.digits], ['H', self.digits], [0, self.digits]],
                [[0, self.digits], ['I', self.digits], [0, self.digits], [0, self.digits], [0, self.digits], ['J', self.digits], [0, self.digits], [0, self.digits], ['K', self.digits]],
                [[0, self.digits], [0, self.digits], ['L', self.digits], [0, self.digits], [0, self.digits], [0, self.digits], ['M', self.digits], [0, self.digits], [0, self.digits]],
                [['N', self.digits], [0, self.digits], [0, self.digits], [, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits]],
                [[0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits]],
                [[0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits]],
                [[0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits], [0, self.digits]],
            ]
        for tab_y in range(max_hauteur):
            txt_variables_line = []
            for tab_x in range(max_largeur):
                var = StringVar()

                case = self.tab[tab_y][tab_x]
                case_frame = Frame(self, borderwidth=0.5, relief=RAISED)
                if case == None:
                    case_widget = Label(case_frame, text="X", bg="black")
                else:
                    if case[0] == "tot":
                        txt = "{}\\{}".format(case[1] if case[1] else ' ', case[2] if case[2] else ' ')
                        case_widget = Frame(case_frame)  # border
                        case_label = Label(case_widget, text=txt, bg="grey")
                        case_label.pack(fill=BOTH, expand=YES)
                    else:

                        if case[0] == 0:
                            # txt = ','.join([str(x) for x in list(case[1])])
                            txt = ''
                        else:
                            txt = case[0]

                        fontsize = 15
                        var.set(txt)

                        case_widget = Frame(case_frame)  # border
                        case_label = Label(case_widget, textvariable=var, font=('Helvatical bold', fontsize))
                        case_label.pack(fill=BOTH, expand=YES)

                txt_variables_line.append(var)
                case_widget.pack(fill=BOTH, expand=YES)
                case_frame.grid(row=tab_y, column=tab_x, sticky="nsew")

            self.txt_variables.append(txt_variables_line)

        for i in range(max_hauteur):
            self.grid_rowconfigure(i, weight=1)
        for i in range(max_largeur):
            self.grid_columnconfigure(i, weight=1)

    def updateTab(self, tab):
        max_hauteur = 13
        max_largeur = 13
        for tab_y in range(max_hauteur):
            for tab_x in range(max_largeur):
                case = tab[tab_y][tab_x]

                if case and isinstance(case[0], int) and case[0] != 0:
                    txt = case[0]
                elif case and isinstance(case[0], int) and case[0] == 0 and len(case[1]) <= 2:
                    txt = ",".join(case[1])
                else:
                    txt = ""

                self.txt_variables[tab_y][tab_x].set(txt)

        self.update_idletasks()

    def get_line(self, case):
        pos_y, pos_x = case
        x = pos_x
        line = []
        case_x = self.tab[pos_y][x]
        while x > 0 and case_x[0] != "tot":
            x -= 1
            case_x = self.tab[pos_y][x]
        tot = case_x[2]
        tot_pos = x

        x += 1
        case_x = self.tab[pos_y][x]
        while case_x and isinstance(case_x[0], int) and x < 13:
            case_x = self.tab[pos_y][x]
            if case_x and isinstance(case_x[0], int):
                line.append(case_x)

            x += 1

        pos_in_line = pos_x - 1 - tot_pos
        return line, tot, pos_in_line

    def get_column(self, case):
        pos_y, pos_x = case
        y = pos_y
        col = []
        case_y = self.tab[y][pos_x]
        while y > 0 and case_y[0] != "tot":
            y -= 1
            case_y = self.tab[y][pos_x]
        tot = case_y[1]
        tot_pos = y

        y += 1
        case_y = self.tab[y][pos_x]
        while case_y and isinstance(case_y[0], int) and y < 13:
            case_y = self.tab[y][pos_x]
            if case_y and isinstance(case_y[0], int):
                col.append(case_y)

            y += 1

        pos_in_col = pos_y - 1 - tot_pos
        return col, tot, pos_in_col

    def set_case_possibilities(self, case, not_skipping_long=False):
        y, x = case

        line, total_x, pos_x = self.get_line(case)
        col, total_y, pos_y = self.get_column(case)

        if x == 12 and y == 2:
            print("here")

        possibilities_case_x = set()
        if [l[0] for l in line].count(0) < 4 or not_skipping_long:
            poss_x = self.get_case_possibilities(total_x, line, possibilities_case_x, pos_x)
        else:
            possibilities_case_x = line[pos_x][1]
            for l in line:
                if l[0] and l[0] in possibilities_case_x:
                    possibilities_case_x.remove(l[0])

        possibilities_case_y = set()
        if [c[0] for c in col].count(0) < 4 or not_skipping_long:
            poss_y = self.get_case_possibilities(total_y, col, possibilities_case_y, pos_y)
        else:
            possibilities_case_y = col[pos_y][1]
            for c in col:
                if c[0] and c[0] in possibilities_case_y:
                    possibilities_case_y.remove(c[0])
        possibilities_case = []
        if possibilities_case_y and possibilities_case_x:
            possibilities_case = possibilities_case_x.intersection(possibilities_case_y)
            if not len(possibilities_case):
                raise Exception("possibilities introuvables pour {} {}".format(y, x))
        elif possibilities_case_x:
            possibilities_case = possibilities_case_x
        elif possibilities_case_y:
            possibilities_case = possibilities_case_y

        if len(possibilities_case):
            self.tab[y][x][1] = set(possibilities_case)

        if len(possibilities_case) == 1:
            print("found ! {} {}".format(y, x))
            self.tab[y][x][0] = list(possibilities_case)[0]
            self.txt_variables[y][x].set(self.tab[y][x][0])
            return True
        else:
            if len(self.tab[y][x][1]) <= 2:
                txt = ",".join([str(x) for x in self.tab[y][x][1]])
                self.txt_variables[y][x].set(txt)
                return True
            return False

    def get_case_possibilities(self, total, filled_cases, possibilities_case, position_case, position_filled_case=0,
                               use_cases_possibilities=False):
        # todo : adapter filled_cases fixe
        filled_digits = [i[0] for i in filled_cases]
        remaining_total = total - sum(filled_digits)
        remaining_cases_count = filled_digits.count(0)

        if remaining_total == 0 and remaining_cases_count == 0:
            possibilities_case.add(filled_digits[position_case])
            return [filled_cases]
        elif not remaining_cases_count:
            return None

        remaining_digits = set()
        for i in self.digits:
            if i not in filled_digits:
                remaining_digits.add(i)

        new_filled_cases = deepcopy(filled_cases)
        while new_filled_cases[position_filled_case][0] != 0:
            #if remaining_cases_count > 4:
            #    for poss in new_filled_cases[position_filled_case][1]:
            #        possibilities_case.add(poss)
            position_filled_case += 1

        if remaining_cases_count > 4:
            for poss in new_filled_cases[position_case][1]:
                possibilities_case.add(poss)

        if position_filled_case > len(new_filled_cases) or remaining_cases_count > 3:
            return False

        possibilities_tmp_case = new_filled_cases[position_filled_case][1]
        for i in remaining_digits.intersection(possibilities_tmp_case):
            new_filled_cases[position_filled_case][0] = i
            self.get_case_possibilities(total, new_filled_cases, possibilities_case, position_case,
                                        position_filled_case)


        return filled_cases

    def set_all_cases_possibilities(self):
        for y in range(13):
            for x in range(13):
                case = self.tab[y][x]
                if case and isinstance(case[0], int):
                    ret = self.set_case_possibilities((y, x))
                    if ret:
                        self.update_idletasks()

    def saveTab(self):
        new_tab = deepcopy(self.tab)
        open('tab.json', 'w').close()

        for line in new_tab:
            for case in line:
                if case and isinstance(case[0], int) and isinstance(case[1], set):
                    case[1] = list(case[1])
        with open('tab.json', 'a') as f:
            f.write(json.dumps(new_tab))
