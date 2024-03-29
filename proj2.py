import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello World!")
        UserInputFrame(self).pack()

class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.user_input = tk.StringVar()
        label = ttk.Label(self, text = "Enter your name:")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self, command=self.greet)

    def greet(self):
        print(f"Hello, {self.user_input.get()}!")

myFrame = UserInputFrame(root)


root = HelloWorld()
root.mainloop()