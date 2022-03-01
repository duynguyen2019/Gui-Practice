import tkinter as tk
from tkinter import ttk


try:
    from ctypes import windll
    windll.shcore.SetProcessDPIAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Widget Examples")

label = ttk.Label(root)    

root.mainloop()


