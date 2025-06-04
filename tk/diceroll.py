import os
import random
from tkinter import *
os.chdir("N:/13PRG/st21033-Ciaran/Programming/tk")

def quit():
    """Close the window"""
    root.destroy()

def print_randon():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    print(num1,num2)
    global count
    count += 1
    label_text.set(count)
    #update red labels with random numbers
    red1.config(text=str(num1))
    red2.config(text=str(num2))
    # Change background color if both are 6, otherwise red
    if num1 == 6 and num2 == 6:
        red1.config(bg="green")
        red2.config(bg="green")
    else:
        red1.config(bg="red")
        red2.config(bg="red")

root = Tk()

count = 0
label_text = IntVar()
label_text.set(0)
#Buttons for quit and random
button_print = Button(root, text = "Quit", width = 10, command = quit)
button_print.grid(row = 0, column = 1)

button_print = Button(root, text = "Random", width = 10, command = print_randon)
button_print.grid(row = 0, column = 0)
#Red Labels
red1 = Label(root, bg = "red")
red1.grid(row = 1, column = 0, sticky = "nsew")

red2 = Label(root, bg = "red")
red2.grid(row = 1, column = 1, sticky = "nsew")

#Roll Count
rollcountmes = Label(root,text = "Roll Count =")
rollcountmes.grid(row = 2, column = 0)

rollcount = Label(root,font = "Arial 10", textvariable = label_text)
rollcount.grid(row = 2, column = 1)

root.mainloop()