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

  def __init__(self, root):
    """
    Widget de map
    :param root: Parent de la map
    :param tab:
    """
    Frame.__init__(self, root)

    max_hauteur = 13
    max_largeur = 13
    self.tab = [[None, None, ["tot", 22, None], ["tot", 28, None], None, ["tot", 4, None], ["tot", 10, None], None, None, None,
     ["tot", 7, None], ["tot", 38, None], None],
    [None, ["tot", 17, 17], [9, set(self.digits)], [8, set(self.digits)], ["tot", None, 10], [0, set(self.digits)],
     [0, set(self.digits)], ["tot", 16, None], ["tot", 23, None], ["tot", 6, 8], [0, set(self.digits)], [0, set(self.digits)],
     ["tot", 4, None]],
    [["tot", None, 22], [0, set(self.digits)], [8, set(self.digits)], [0, set(self.digits)], ["tot", None, 39], [0, set(self.digits)],
     [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)],
     [0, set(self.digits)]],
    [["tot", None, 14], [0, set(self.digits)], [5, set(self.digits)], [0, set(self.digits)], ["tot", 29, None], ["tot", None, 20],
     [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], ["tot", 12, 9], [0, set(self.digits)], [0, set(self.digits)]],
    [None, None, ["tot", None, 17], [0, set(self.digits)], [0, set(self.digits)], None, ["tot", None, 4], [0, set(self.digits)],
     [0, set(self.digits)], ["tot", 19, 6], [0, set(self.digits)], [0, set(self.digits)], None],
    [None, ["tot", 11, None], ["tot", 40, 11], [0, set(self.digits)], [0, set(self.digits)], None, ["tot", 4, None],
     ["tot", 9, 14], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], ["tot", 17, None]],
    [["tot", None, 12], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], ["tot", 28, 13],
     [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], ["tot", 27, 16], [0, set(self.digits)], [0, set(self.digits)]],
    [["tot", None, 14], [0, set(self.digits)], [0, set(self.digits)], ["tot", 9, 20], [0, set(self.digits)], [0, set(self.digits)],
     [0, set(self.digits)], [0, set(self.digits)], ["tot", None, 26], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)],
     [0, set(self.digits)]],
    [None, ["tot", None, 24], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)],
     ["tot", 16, None], None, ["tot", None, 3], [0, set(self.digits)], [0, set(self.digits)], None, None],
    [None, ["tot", 14, 17], [0, set(self.digits)], [0, set(self.digits)], ["tot", 9, 6], [0, set(self.digits)], [0, set(self.digits)],
     ["tot", 20, None], ["tot", None, 7], [0, set(self.digits)], [0, set(self.digits)], ["tot", 19, None], ["tot", 7, None]],
    [["tot", None, 6], [0, set(self.digits)], [0, set(self.digits)], ["tot", 6, 29], [0, set(self.digits)], [0, set(self.digits)],
     [0, set(self.digits)], [0, set(self.digits)], ["tot", 17, None], ["tot", None, 23], [0, set(self.digits)], [0, set(self.digits)],
     [0, set(self.digits)]],
    [["tot", None, 44], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)],
     [0, set(self.digits)], [0, set(self.digits)], [0, set(self.digits)], ["tot", None, 11], [0, set(self.digits)], [0, set(self.digits)],
     [0, set(self.digits)]],
    [None, ["tot", None, 5], [0, set(self.digits)], [0, set(self.digits)], None, None, ["tot", None, 17], [0, set(self.digits)],
     [0, set(self.digits)], ["tot", None, 4], [0, set(self.digits)], [0, set(self.digits)], None]]

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
              #txt = ','.join([str(x) for x in list(case[1])])
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

    print(self.txt_variables[0])
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

        if case[0] != 0:
          txt = case[0]
        else:
          txt = ""

        self.txt_variables[max_largeur][max_largeur].set(txt)

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
      y += 1
      if case_y and isinstance(case_y[0], int):
        col.append(case_y)


    pos_in_col = pos_y - 1 - tot_pos
    return col, tot, pos_in_col

  def set_case_possibilities(self, case):
    y, x = case


    line, total_x, pos_x = self.get_line(case)
    col, total_y, pos_y = self.get_column(case)



    possibilities_case_x = set()
    poss_x = self.get_case_possibilities(total_x, line, possibilities_case_x, pos_x)

    possibilities_case_y = set()
    poss_y = self.get_case_possibilities(total_y, col, possibilities_case_y, pos_y)
    possibilities_case = possibilities_case_x.intersection(possibilities_case_y)
    self.tab[y][x][1] = list(possibilities_case)
    if len(possibilities_case) == 1:
      print("found ! {} {}".format(y, x))
      print(self.txt_variables[y])
      print(list(possibilities_case)[0])
      self.tab[y][x][0] = list(possibilities_case)[0]
      self.txt_variables[y][x].set(self.tab[y][x][0])
      print(case)
      return True
    else:
      print("return")
      return False

  def get_case_possibilities(self, total, filled_cases, possibilities_case, position_case, position_filled_case=0,
                        use_cases_possibilities=False):
    # todo : adapter filled_cases fixe
    possibilities = []
    filled_digits = [i[0] for i in filled_cases]
    remaining_total = total - sum(filled_digits)
    remaining_cases_count = filled_digits.count(0)

    if remaining_total == 0 and remaining_cases_count == 0:
      possibilities_case.add(filled_digits[position_case])
      return [filled_cases]
    elif not remaining_cases_count or remaining_cases_count > 3:
      return None

    remaining_digits = []
    for i in self.digits:
      if i not in filled_digits:
        remaining_digits.append(i)
    for i in remaining_digits:

      new_filled_cases = deepcopy(filled_cases)
      while new_filled_cases[position_filled_case][0] != 0:
        position_filled_case += 1
      new_filled_cases[position_filled_case][0] = i  # todo: use_cases_possibilities
      ret = self.get_case_possibilities(total, new_filled_cases, possibilities_case, position_case, position_filled_case)
      if ret:
        possibilities += ret

    return possibilities

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
    open('tab.txt', 'w').close()

    for line in new_tab:
      for case in line:
        if case and isinstance(case[0], int) and isinstance(case[1], set):
          case[1] = list(case[1])
    print(new_tab)
    with open('tab.txt', 'a') as f:
      f.write(json.dumps(new_tab))
