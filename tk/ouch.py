import os
from tkinter import *
os.chdir("N:/13PRG/st21033-Ciaran/Programming/tk")

def click():
    global count
    count += 1
    label_text.set(count)

root = Tk()
root.title("Exercise 3")

#Initialise
count = 0
label_text = IntVar()
label_text.set(0)

#add a label to display the count
label_1 = Label(root,font = "Arial 40 bold", textvariable = label_text)
label_1.pack()

button_1 = Button(root, text = "Click Me", bg = "black", fg = "yellow", 
                  font = ("Arial 35 bold"), command = click)
button_1.pack(fill=X)

root.mainloop()