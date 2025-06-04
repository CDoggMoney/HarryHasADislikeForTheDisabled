import os
from tkinter import *
os.chdir("N:/13PRG/st21033-Ciaran/Programming/tk")

root = Tk()
root.title("Exercise 2")

# load an image file to and object (x)
x = PhotoImage(file="image.png")

#downsizes image to 1/4 original size
x= x.subsample(4)

#instead of text, assign image to label
label = Label(root,image=x)
label.pack()

root.mainloop()