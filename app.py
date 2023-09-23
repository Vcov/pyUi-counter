from customtkinter import *
import customtkinter as ctk

app = ctk.CTk()

# Variables
numberVar = ctk.IntVar(value=0)

# Main Frame for the count number
mainframe = ctk.CTkFrame(app, width=100, height=70)
mainframe.pack(pady=10)

countlabel = ctk.CTkLabel(mainframe, textvariable=numberVar, width=100, height=50, font=("Roboto", 24))
countlabel.pack(pady=10)

# Buttons
buttonsframe = ctk.CTkFrame(app, width=250, height=200)
buttonsframe.pack()

# Row 1 (0)

btn1 = ctk.CTkButton(buttonsframe, text="1", width=70, height=60)
btn1.grid(row=0, column=0, padx=10, pady=10)
btn2 = ctk.CTkButton(buttonsframe, text="2", width=70, height=60)
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3 = ctk.CTkButton(buttonsframe, text="3", width=70, height=60)
btn3.grid(row=0, column=2, padx=10, pady=10)

# Row 2 (1)

btn4 = ctk.CTkButton(buttonsframe, text="4", width=70, height=60)
btn4.grid(row=1, column=0, padx=10, pady=10)
btn5 = ctk.CTkButton(buttonsframe, text="5", width=70, height=60)
btn5.grid(row=1, column=1, padx=10, pady=10)
btn6 = ctk.CTkButton(buttonsframe, text="6", width=70, height=60)
btn6.grid(row=1, column=2, padx=10, pady=10)

# Row 3 (2)

btn7 = ctk.CTkButton(buttonsframe, text="7", width=70, height=60)
btn7.grid(row=3, column=0, padx=10, pady=10)
btn8 = ctk.CTkButton(buttonsframe, text="8", width=70, height=60)
btn8.grid(row=3, column=1, padx=10, pady=10)
btn9 = ctk.CTkButton(buttonsframe, text="9", width=70, height=60)
btn9.grid(row=3, column=2, padx=10, pady=10)

# App Settings
app.geometry("300x400")
app.title("Counter")
app.columnconfigure(2, weight=1)
app.mainloop()    
