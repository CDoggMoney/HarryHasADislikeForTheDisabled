import random
from tkinter import *
#Makes a function for the quit button to close the program
def quit():
    root.destroy()
#Makes the function which runs when the random button is pressed which also controls the colour of the red boxes
def print_randon():
    #Selects two random numbers from 1 to 6
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    #Uses the same click counter from Exercise 3 for the amount of rolled dice
    global count
    count += 1
    label_text.set(count)
    #Update red labels with the random numbers
    red1.config(text=str(num1))
    red2.config(text=str(num2))
    #Change background color to green if both numbers are 6, otherwise the background remains red
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
#Button for Quit as well as its formatting
button_print = Button(root, text = "Quit", width = 10, command = quit)
button_print.grid(row = 0, column = 1)
#Button for Random as well as its formatting
button_print = Button(root, text = "Random", width = 10, command = print_randon)
button_print.grid(row = 0, column = 0)
#The two red labels which will display the numbers as well as turn green when both are 6
red1 = Label(root, bg = "red")
red1.grid(row = 1, column = 0, sticky = "nsew")

red2 = Label(root, bg = "red")
red2.grid(row = 1, column = 1, sticky = "nsew")

#The roll counter
rollcountmes = Label(root,text = "Roll Count =")
rollcountmes.grid(row = 2, column = 0)

rollcount = Label(root,font = "Arial 10", textvariable = label_text)
rollcount.grid(row = 2, column = 1)

root.mainloop()