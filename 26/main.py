import time
from copy import copy, deepcopy
from tkinter import *
from TabIHM import TabIHM

digits = [i for i in range(1, 10)]

# poss = get_possibilities(26, [0, 9, 8, 0, 0])


root = Tk()
root.geometry("700x700")

tabIHM = TabIHM(root, True)


nb = 0
while nb < 10:
    for y in range(13):
        for x in range(13):
            case = tabIHM.tab[y][x]
            print("trying {} {}".format(y, x))
            if case and isinstance(case[0], int) and not case[0]:
                ret = tabIHM.set_case_possibilities((y, x), nb > 5)
    nb += 1
    tabIHM.saveTab()
    time.sleep(1)

tabIHM.pack()
root.update_idletasks()
root.update()
root.mainloop()
print("plus de résultats.")
