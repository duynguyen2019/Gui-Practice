import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDPIAwareness(1)
except:
    pass

def greet():
    print(f"Hello, {user_name.get() or 'World'}!")
 

root = tk.Tk()
root.geometry("600x400")

root.columnconfigure(0, weight=1)
input_frame = ttk.Frame(root, padding=(20,10,20,0))
input_frame.grid(row=0,column=0,sticky="EW")

user_name = tk.StringVar()
name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(row=0,column=0)
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0,column=1)
name_entry.focus()



buttons = ttk.Frame(root,padding=(20,10))
buttons.grid(sticky="EW")
buttons.columnconfigure((0,1),weight=1)

label = ttk.Label(buttons, text = f"{user_name.get() or 'Nothing has been entered'}")    
label.grid(row=0,column=0,sticky="EW")
greet_button = ttk.Button(buttons, text = "Greet", command = greet)
greet_button.grid(row=1,column=0,sticky="EW")
quit_button = ttk.Button(buttons, text = "Quit", command = root.destroy)
quit_button.grid(row=1,column=1,sticky="EW")
root.mainloop()



