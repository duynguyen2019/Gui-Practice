from cgitb import text
import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from rt import *

def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres *3.28084
        feet_value.set(f"{feet} feet")
    except ValueError:
        pass

set_dpi_awareness()


#Initialize variables
metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")

# Creating frames
main = ttk.Frame(root, padding=(30,15))
main.grid()

metres_label = ttk.Label(main, text="Meters: ")
metres_input = ttk.Entry(main, width=10,textvariable=metres_value)
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main, text ="Feet shown here:",textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate:",command=calculate_feet)

metres_label.grid(column=0,row=0,sticky="W",padx=5,pady=5)
metres_input.grid(column=1,row=0,padx=5,pady=5)
metres_input.focus()

feet_label.grid(column=0, row=1,sticky="W",padx=5,pady=5)
feet_display.grid(column=1, row=1,padx=5,pady=5)

calc_button.grid(column=0,row=2,columnspan=2, sticky="EW",padx=5,pady=5)


# Key binding
root.bind("<Return>",calculate_feet)

# Run the app
root.mainloop()