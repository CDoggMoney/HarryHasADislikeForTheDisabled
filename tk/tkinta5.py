import os
from tkinter import *
os.chdir("N:/13PRG/st21033-Ciaran/Programming/tk")

def quit():
    """Close the window"""
    root.destroy()

def print_text():
    """Print your text in the entry box"""
    print(box.get())

def print_sum():
    """Print the sum of both entry boxes"""
    try:
        num1 = float(box.get())
        num2 = float(box2.get())
        result = num1 + num2
        sum_label.config(text=result)
    except ValueError:
        print("Please enter valid numbers")

def reset_entries():
    """Clear both entry boxes"""
    box.delete(0, END)
    box2.delete(0, END)
    sum_label.config(text="")

#main program
root = Tk()
root.title("Exercise 5")
root.resizable(0,0)

#create entry box
box = Entry(root, justify = CENTER)
box.pack(fill = X, ipady = 10)

x = Label(root,text = "+",
          bg = "grey", fg = "black",
          font = "Arial 30 bold")
x.pack(fill=X,ipady=20)

box2 = Entry(root, justify = CENTER)
box2.pack(fill = X, ipady = 10)

# label to show the sum
sum_label = Label(root, text="", font="Arial 14")
sum_label.pack(pady=10)

#create two buttons
button_print = Button(root, text = "Print", width = 10, command = print_sum)
button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

button_print = Button(root, text = "Reset", width = 10, command = reset_entries)
button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

button_quit = Button(root, text = "Quit", width = 10, command = quit)
button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

root.mainloop()