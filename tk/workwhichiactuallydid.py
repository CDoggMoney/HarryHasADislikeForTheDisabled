from tkinter import*
from tkinter import ttk

root = Tk()
choices = ["A", "B", "C", "D"]#Store options in list
chosen = StringVar()#Initialise the variable which stores user input
default = "" #display blank when window loads
my_options = ttk.OptionMenu(root,chosen,default,*choices)
my_options.pack()
root.mainloop()