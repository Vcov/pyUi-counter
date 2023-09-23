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

btn1 = ctk.CTkButton(app)

# App Settings
app.geometry("300x400")
app.columnconfigure(2, weight=1)
app.mainloop()    
