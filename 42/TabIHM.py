"""
Widget de map
"""
import json
import string
import time
from collections import Counter
from copy import deepcopy
from tkinter import *

case_by_number = {}
across_numbers = {
  1: "male",
  5: "tate",
  9: "calm",
  13: "dined",
  15: "dens",
  16: "taco",
  17: "adage",
  18: "herd",
  19: "opal",
  20: "suspenders",
  22: "dali",
  23: "windows",
  27: "oreos",
  30: "numerous",
  34: "octane",
  35: "drives",
  37: "castor",
  38: "trumpets",
  40: "condo",
  41: "slow",
  42: "crux",
  44: "aquaman",
  48: "yoke",
  50: "signatures",
  53: "mist",
  54: "bids",
  55: "vegas",
  56: "chin",
  57: "nato",
  58: "pixar",
  59: "gems",
  60: "army",
  61: "taro",
}
down_numbers = {
  1: "plea",
  3: "denim",
  4: "naiad",
  5: "sweeter",
  6: "strands",
  8: "swede",
  11: "data",
  12: "lama",
  21: "micron",
  25: "squareroot",
  29: "pony",
  30: "nova",
  31: "dues",
  32: "stockings",
  33: "crescendo",
  38: "melanin",
  39: "daytona",
  43: "taxis",
  45: "pours",
  47: "exams",
  48: "myth",
  49: "miso",
  51: "borg",
}


def get_word_line(case):
  pass


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

    max_hauteur = 15
    max_largeur = 15

    if load_from_json:
      with open('tab.txt') as f:
        self.tab = json.loads(f.read())
    else:
      self.tab = [
        [[set(string.ascii_lowercase), 1, 1], [set(string.ascii_lowercase), None, 2],
         [set(string.ascii_lowercase), None, 3], [set(string.ascii_lowercase), None, 4], [None, None, None],
         [None, None, None], [set(string.ascii_lowercase), None, 5], [set(string.ascii_lowercase), None, 6],
         [set(string.ascii_lowercase), None, 7], [set(string.ascii_lowercase), None, 8], [None, None, None],
         [set(string.ascii_lowercase), None, 9], [set(string.ascii_lowercase), None, 10],
         [set(string.ascii_lowercase), None, 11], [set(string.ascii_lowercase), None, 12]],
        [[set(string.ascii_lowercase), 13, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), 14, None], [None, None, None], [set(string.ascii_lowercase), 15, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), 16, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), 17, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), 18, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), 19, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), 20, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), 21, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None],
         [set(string.ascii_lowercase), 22, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None]],
        [[None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [None, None, None], [None, None, None]],
        [[None, None, None], [None, None, None], [None, None, None], [None, None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None],
         [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None],
         [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [None, None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
        [[None, None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None]],
        [[set('y'), None, None], [set('o'), None, None], [set('k'), None, None], [set('e'), None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None]],
        [[set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [None, None, None], [None, None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None], [set(string.ascii_lowercase), None, None]],
      ]

    number = 0
    is_start_line = False
    is_start_col = False
    for tab_y in range(max_hauteur):
      txt_variables_line = []
      for tab_x in range(max_largeur):
        var = StringVar()

        # print("{} {}".format(tab_x, tab_y))
        case = self.tab[tab_y][tab_x]

        number_line = 0
        number_col = 0
        if tab_y > 0:
          case_au_dessus = self.tab[tab_y - 1][tab_x][0]
        else:
          case_au_dessus = None

        if tab_x > 0:
          case_avant = self.tab[tab_y][tab_x - 1][0]
        else:
          case_avant = None

        if (not case_au_dessus or not case_avant) and case[0]:
          number += 1

        if not case_avant and case[0]:
          case[1] = number
          if number not in case_by_number.keys():
            case_by_number[number] = case

        if not case_au_dessus and case[0]:
          case[2] = number
          if number not in case_by_number.keys():
            case_by_number[number] = case

        case.append(tab_y)
        case.append(tab_x)
        if (tab_y, tab_x) == (11, 2):
          case[0] = {"k"}
        if (tab_y, tab_x) == (6, 1):
          case[0] = {"u"}
        case_frame = Frame(self, borderwidth=0.5, relief=RAISED)
        if not case[0]:
          case_widget = Label(case_frame, text="X", bg="black")
        else:
          case_widget = Frame(case_frame)  # border

          if case[1] or case[2]:
            case_number = Label(case_widget, text=number, bg="grey", font=("Arial", 9))
            case_number.pack(anchor=NW)

          if len(case[0]) == 2:

            txt = "{}\\{}".format(list(case[0])[0], list(case[0])[1])

            fontsize = 12

            # case_label = Label(case_widget, text=txt, bg="grey")
            # case_label.pack(fill=BOTH, expand=YES)
          elif len(case[0]) == 1:
            txt = list(case[0])[0]

            fontsize = 15
          else:
            txt = '   '
            fontsize = 15

          var.set(txt)

          case_label = Label(case_widget, textvariable=var, font=('Helvatical bold', fontsize))
          case_label.pack(fill=BOTH, expand=YES)

        txt_variables_line.append(var)
        case_widget.pack(fill=BOTH, expand=YES)
        case_frame.grid(row=tab_y, column=tab_x, sticky="nsew")

      self.txt_variables.append(txt_variables_line)

    self.saveTab()
    for i in range(max_hauteur):
      self.grid_rowconfigure(i, weight=1)
    for i in range(max_largeur):
      self.grid_columnconfigure(i, weight=1)

  def updateTab(self):
    max_hauteur = 15
    max_largeur = 15
    for tab_y in range(max_hauteur):
      for tab_x in range(max_largeur):
        case = self.tab[tab_y][tab_x]

        if not case[0]:
          continue

        if 3 >= len(case[0]) >= 2:
          txt = "".join(["{}/".format(list(case[0])[x]) for x in range(len(case[0]))])

          fontsize = 12

          # case_label = Label(case_widget, text=txt, bg="grey")
          # case_label.pack(fill=BOTH, expand=YES)
        elif len(case[0]) == 1:
          txt = list(case[0])[0]

          fontsize = 15
        else:
          txt = ' '
          fontsize = 15

        self.txt_variables[tab_y][tab_x].set(txt)

    self.update_idletasks()
    self.update()

  def line_first_case(self, case):
    new_case = case
    while not new_case[1] and new_case[0] and new_case[4] > 0:
      new_case = self.tab[new_case[3]][new_case[4] - 1]

    return new_case

  def col_first_case(self, case):
    new_case = case
    while not new_case[2] and new_case[0] and new_case[3] >= 0:
      new_case = self.tab[new_case[3] - 1][new_case[4]]

    return new_case

  def get_poss_line(self, case):
    line_first_case = self.line_first_case(case)
    word_str = self.get_line(case)
    if not word_str:
      return []
    word = list(word_str)
    letters_count = {}
    for letter in word:
      letters_count[letter] = 0

    new_case = line_first_case
    while (new_case[0] and new_case[3] < 14):
      for letter in new_case[0].intersection(letters_count.keys()):
        letters_count[letter] += 1

      new_case = self.tab[new_case[3]+1][new_case[4]]

    if new_case[3] == 14 and new_case[0]:
      for letter in new_case[0].intersection(letters_count.keys()):
        letters_count[letter] += 1

    for letter in letters_count.keys():
      word.remove(letter)

    return word

  def get_poss_col(self, case):
    col_first_case = self.col_first_case(case)
    word_str = self.get_column(case)
    if not word_str:
      return []
    word = list(word_str)

    letters_count = {}
    for letter in word:
      letters_count[letter] = 0

    new_case = col_first_case
    while (new_case[0] and new_case[4] < 14):
      for letter in new_case[0].intersection(letters_count.keys()):
        letters_count[letter] += 1

      new_case = self.tab[new_case[3]][new_case[4]+1]

    if new_case[4] == 14 and new_case[0]:
      for letter in new_case[0].intersection(letters_count.keys()):
        letters_count[letter] += 1

    for letter in letters_count.keys():
      word.remove(letter)

    return word

  def get_line(self, case):
    first_case = self.line_first_case(case)

    if first_case[1] in across_numbers.keys():
      return across_numbers[first_case[1]]

  def get_column(self, case):
    first_case = self.col_first_case(case)

    if first_case[2] in down_numbers.keys():
      return down_numbers[first_case[2]]

  def common_chars(self, word1, word2):
    if not word1 and not word2:
      return None

    if not word1:
      return set(word2)
    elif not word2:
      return set(word1)


    list_word1 = Counter(word1)
    list_word2 = Counter(word2)
    letters = {}
    common = list_word1 & list_word2
    for letter in common:
      if letter not in letters.keys():
        letters[letter] = 1
      else:
        letters[letter] += 1

    return common

  def check_word_line(self, case, word2):
    word1 = self.get_line(case)

    return self.common_chars(word1, word2)

  def check_word_col(self, case, word1):
    word2 = self.get_column(case)

    return self.common_chars(word1, word2)

  def set_case_possibilities_2(self, case):
    poss_line = self.get_poss_line(case)
    poss_col = self.get_poss_col(case)

    modified = False
    for letter in poss_line:
      if letter in case[0]:
        case[0].remove(letter)
        modified = True
    for letter in poss_col:
      if letter in case[0]:
        case[0].remove(letter)
        modified = True

    return modified

  def set_case_possibilities(self, case):
    if not case or not case[0] or len(case[0]) == 1:
      return

    if case[3] == 2 and case[4] == 1:
      print("here")

    modified = False
    word_line = self.get_line(case)
    word_col = self.get_column(case)
    print(word_col)

    common_chars = self.common_chars(word_line, word_col)
    if not common_chars:
      print("-------Erreur sur {} {} : {} {} - {}".format(case[3], case[4], word_line, word_col, None))
      return False
    possibilities = set(common_chars)

    print("{} {} : {} {} - {}".format(case[3], case[4], word_line, word_col, "".join(list(possibilities))))
    found_length = len(case[0])
    print(case[0])
    print(possibilities)
    case[0] = case[0].intersection(possibilities)
    print(case[0])

    self.tab[case[3]][case[4]] = case
    if found_length != len(case[0]):
      modified = True

    return modified

  def resolve(self):
    keep = True
    while keep:
      keep = False

      for line in self.tab:
        for case in line:
          ret = self.set_case_possibilities(case)

          if ret:
            keep = True

          ret = self.set_case_possibilities_2(case)
          if ret:
            keep = True

      time.sleep(1)
      self.updateTab()

      # for line_number in across_numbers.keys():
      #   if line_number in case_by_number.keys():
      #     case = case_by_number[line_number]
      #   else:
      #     case = None
      #   ret = self.set_case_possibilities_2(case)
      #
      #   if ret:
      #     keep = True

      time.sleep(1)

      self.updateTab()
    self.mainloop()

  def saveTab(self):
    new_tab = deepcopy(self.tab)
    open('tab.txt', 'w').close()

    for line in new_tab:
      for case in line:
        if case and case[0]:
          case[0] = list(case[0])
    print(new_tab)
    with open('tab.txt', 'a') as f:
      f.write(json.dumps(new_tab))


