from tkinter import *

def centigrade():
    first_frame.pack_forget()
    centigrade_frame.pack(fill="both", expand=True)

def farenheit():
    first_frame.pack_forget()
    farenheit_frame.pack(fill="both", expand=True)

def backtomain():
    centigrade_frame.pack_forget()
    farenheit_frame.pack_forget()
    first_frame.pack(fill="both", expand=True)

def calcfaren():
    try:
        num1 = float(EnterTemp2.get())
        result = num1*9/5
        resultant = result+32
        Calc2.config(text=f"{resultant}°F")
    except ValueError:
        print("Please enter valid numbers")

def calccent():
    try:
        num1 = float(EnterTemp.get())
        result = num1 - 32
        resultant = result*5/9
        Calc.config(text=f"{resultant}°C")
    except ValueError:
        print("Please enter valid numbers")

def resett():
    num = 0
    Calc.config(text=num)
    Calc2.config(text=num)

root = Tk()
root.title("Temperature Converter")

#Label for the top text "Temperature Converter"
first_frame = Frame(root)
first_frame.pack(fill="both", expand=True)

Label1 = Label(first_frame,text = "Temperature Converter", font = "Arial 20 bold")
Label1.grid(row = 0, column = 0, columnspan = 2)
#button for centigrade and farenheit
CentigradeButton = Button(first_frame, text = "to Centigrade", width = 10, height = 2,
                          command = centigrade, bg = "yellow")
CentigradeButton.grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)

FarenheitButton = Button(first_frame, text = "to Farenheit", width = 10, height = 2,
                          command = farenheit, bg = "pink")
FarenheitButton.grid(row = 1, column = 1, sticky = "nsew", padx = 5, pady = 5)



#Centrigrade from farenheit
centigrade_frame = Frame(root)
Label2 = Label(centigrade_frame,text = "Enter the temperature in Farenheit", font = "Arial 15 bold")
Label2.grid(row = 0, column = 0, columnspan = 3)

EnterTemp = Entry(centigrade_frame, justify = CENTER, font = "Arial 15")
EnterTemp.grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5, columnspan = 3)

FarenheitCalculate = Button(centigrade_frame, text = "calculate", width = 10, height = 2,
                          command = calccent)
FarenheitCalculate.grid(row = 2, column = 0, sticky = "nsew", padx = 5, pady = 5)

FarenheitButton = Button(centigrade_frame, text = "back", width = 10, height = 2,
                          command = backtomain)
FarenheitButton.grid(row = 2, column = 1, sticky = "nsew", padx = 5, pady = 5)

ResetFarenheitButton = Button(centigrade_frame, text = "reset", width = 10, height = 2,
                          command = resett)
ResetFarenheitButton.grid(row = 2, column = 2, sticky = "nsew", padx = 5, pady = 5)

Calc = Label(centigrade_frame, text = "Calculated temp goes here.")
Calc.grid(row = 3, column = 0, sticky = "nsew")

#Farenheit to centigrade
farenheit_frame = Frame(root)
Label3 = Label(farenheit_frame,text = "Enter the temperature in Centigrade", font = "Arial 15 bold")
Label3.grid(row = 0, column = 0, columnspan = 3)

EnterTemp2 = Entry(farenheit_frame, justify = CENTER, font = "Arial 15")
EnterTemp2.grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5, columnspan = 3)

FarenheitCalculate = Button(farenheit_frame, text = "calculate", width = 10, height = 2,
                          command = calcfaren)
FarenheitCalculate.grid(row = 2, column = 0, sticky = "nsew", padx = 5, pady = 5)

FarenheitButton = Button(farenheit_frame, text = "back", width = 10, height = 2,
                          command = backtomain)
FarenheitButton.grid(row = 2, column = 1, sticky = "nsew", padx = 5, pady = 5)

ResetFarenheitButton = Button(farenheit_frame, text = "reset", width = 10, height = 2,
                          command = resett)
ResetFarenheitButton.grid(row = 2, column = 2, sticky = "nsew", padx = 5, pady = 5)

Calc2 = Label(farenheit_frame, text = "Calculated temp goes here.")
Calc2.grid(row = 3, column = 0, sticky = "nsew", columnspan = 3)


root.mainloop()
