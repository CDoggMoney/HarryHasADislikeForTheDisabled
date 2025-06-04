import os
os.chdir("N:/13PRG/st21033-Ciaran/Programming/tk")
from tkinter import *

root = Tk()
root.title("Zandre image 2")

x = PhotoImage(file="imahe.png")
x = x.subsample(1)  # Scale down the image
root.resizable(0,0)

label = Label(root, image=x)
label.pack()

root.mainloop()