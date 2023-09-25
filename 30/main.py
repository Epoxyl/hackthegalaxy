import time
from tkinter import *
from TabIHM import TabIHM

root = Tk()
root.geometry("2000x1200")

tabIHM = TabIHM(root, True)

tabIHM.pack(fill=BOTH, expand=YES)

tabIHM.resolve()

