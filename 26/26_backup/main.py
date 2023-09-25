import time
from copy import copy, deepcopy
from tkinter import *
from TabIHM import TabIHM

digits = [i for i in range(1, 10)]

# poss = get_possibilities(26, [0, 9, 8, 0, 0])


root = Tk()
tabIHM = TabIHM(root)
tabIHM.pack()
root.update_idletasks()
root.update()

ret = True
while ret:
    ret = None
    for y in range(13):
        for x in range(13):
            case = tabIHM.tab[y][x]
            if case and isinstance(case[0], int) and not case[0]:
                ret = tabIHM.set_case_possibilities((y, x))
                if ret:
                    tabIHM.update_idletasks()
                    time.sleep(0.5)
                    print("found")
                    print(case)

print("plus de résultats.")
tabIHM.saveTab()