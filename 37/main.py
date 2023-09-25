from TabIHM import *

root = Tk()
root.geometry("1000x600")

tabIHM = TabIHM(root)
tabIHM.pack(fill=BOTH, expand=YES)

tabIHM.resolve()
