import os
from tkinter import *
os.chdir("N:/13PRG/st21033-Ciaran/Programming")

root = Tk()
#Gives the window a name
root.title("Exercise 1")
#Sets the windows size
root.geometry("400x400")
#stops user from resizing window
root.resizable(0,0)
#sets the background colour
root.configure(bg="#FFFF00")

#adds a label
x = Label(root,text = "Harry Fat!",
          bg = "black", fg = "lime",
          font = "Arial 30 bold")
x.pack(fill=X,ipady=20)


root.mainloop()