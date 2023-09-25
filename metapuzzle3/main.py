from copy import deepcopy

tab = [
  ["START", "C", "L", "I", "H", "W", "I", "T", "H"],
  ["G", "Y", "F", "X", "F", "L", "U", "X", "C"],
  ["V", "Z", "G", "E", "N", "D", "S", None, "E"],
  ["M", "V", "E", "R", "B", "T", "J", "A", "L"],
  ["L", "D", "U", "Z", "O", "M", "O", "D", "E"],
  ["J", None, "P", "U", "C", "K", "Y", "U", "G"],
  ["N", "F", "M", "K", "Q", "A", "W", "R", "Y"],
  ["*", "*", "*", "*", "V", "K", "Y", "P", "END"],
]

counts = {}
for line in tab:
  for case in line:
    if case not in counts.keys():
      counts[case] = 0

    counts[case] += 1

print(counts)


def remove_letter(case_value, case):
  for i in range(8):
    for j in range(9):
      if tab[i][j] == case_value and (i, j) != case:
        tab[i][j] = None


def try_case(current_case, case_to_switch, path, temp_tab):
  case_y, case_x = case_to_switch
  current_case_y, current_case_x = current_case

  if (case_y > 7 or case_x > 8) or (case_y < 0 or case_x < 0) or len(path) > 26 or not temp_tab[case_y][case_x]:
    return False

  if case_to_switch == "END":
    if len(path) == 26:
      print(path)
      print("true path ! ")
      raise Exception("found")
    else:
      return False

  case_value = temp_tab[case_y][case_x]
  path += case_value

  if case_value != '*':
    remove_letter(case_value, case_to_switch)

  temp_tab[current_case_y][current_case_x] = None

  next_cases = [(case_y + 1, case_x), (case_y, case_x + 1), (case_y - 1, case_x), (case_y, case_x - 1)]

  for next_case in next_cases:
    try_case(case_to_switch, next_case, path, deepcopy(temp_tab))


try_case((0, 0), (0, 1), '', deepcopy(tab))
try_case((0, 0), (1, 0), '', deepcopy(tab))

