from customtkinter import *
import customtkinter as ctk

app = ctk.CTk()

# Variables
numberVar = ctk.IntVar(value=0)
operator = ctk.StringVar(value=None)
mode = ctk.StringVar(value=None)

# Functions
def add_number(num):
   operatorN = operator.get()
   if operatorN == '+':
        numberVar.set(numberVar.get() + int(num))
   elif operatorN == '-':
       numberVar.set(numberVar.get() - int(num))

def clear():
    numberVar.set(0)

def addition():
    operator.set('+') 
    mode.set("Addition") 

def substraction():
    operator.set('-')
    mode.set("Substraction")

# Main Frame for the count number
mainframe = ctk.CTkFrame(app, width=100, height=70)
mainframe.pack(pady=10)

countlabel = ctk.CTkLabel(mainframe, textvariable=numberVar, width=100, height=50, font=("Roboto", 24))
countlabel.pack(pady=10)

# Buttons
buttonsframe = ctk.CTkFrame(app, width=250, height=300)
buttonsframe.pack()

# Row 1 (0)

btn1 = ctk.CTkButton(buttonsframe, text="1", width=70, height=60, command=lambda: add_number(1))
btn1.grid(row=0, column=0, padx=10, pady=10)
btn2 = ctk.CTkButton(buttonsframe, text="2", width=70, height=60, command=lambda: add_number(2))
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3 = ctk.CTkButton(buttonsframe, text="3", width=70, height=60, command=lambda: add_number(3))
btn3.grid(row=0, column=2, padx=10, pady=10)

# Row 2 (1)

btn4 = ctk.CTkButton(buttonsframe, text="4", width=70, height=60, command=lambda: add_number(4))
btn4.grid(row=1, column=0, padx=10, pady=10)
btn5 = ctk.CTkButton(buttonsframe, text="5", width=70, height=60, command=lambda: add_number(5))
btn5.grid(row=1, column=1, padx=10, pady=10)
btn6 = ctk.CTkButton(buttonsframe, text="6", width=70, height=60, command=lambda: add_number(6))
btn6.grid(row=1, column=2, padx=10, pady=10)

# Row 3 (2)

btn7 = ctk.CTkButton(buttonsframe, text="7", width=70, height=60, command=lambda: add_number(7))
btn7.grid(row=3, column=0, padx=10, pady=10)
btn8 = ctk.CTkButton(buttonsframe, text="8", width=70, height=60, command=lambda: add_number(8))
btn8.grid(row=3, column=1, padx=10, pady=10)
btn9 = ctk.CTkButton(buttonsframe, text="9", width=70, height=60, command=lambda: add_number(9))
btn9.grid(row=3, column=2, padx=10, pady=10)

# Other buttons

clrbtn = ctk.CTkButton(buttonsframe, text="Clear", command=clear, width=70, height=40, font=("Roboto", 20))
clrbtn.grid(row=4, column=1, padx=10, pady=10)

clrbtn = ctk.CTkButton(buttonsframe, text="+", command=addition, width=50, height=40, font=("Roboto", 20))
clrbtn.grid(row=4, column=0, padx=10, pady=10)

clrbtn = ctk.CTkButton(buttonsframe, text="-", command=substraction, width=50, height=40, font=("Roboto", 20))
clrbtn.grid(row=4, column=2, padx=10, pady=10)

modeLabel = ctk.CTkLabel(app, textvariable=mode)
modeLabel.pack(pady=20)

# App Settings
app.geometry("300x450")
app.title("Counter")
app.columnconfigure(2, weight=1)
app.mainloop()    
