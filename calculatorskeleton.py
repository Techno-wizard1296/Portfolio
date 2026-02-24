import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math

win = tk.Tk()
win.title('Att- Calculator')

frame = tk.Frame(win, bg= "Red", padx=10, pady=10)
frame.pack()

entry = tk.Entry(frame, relief=SUNKEN, width=30, borderwidth=3)
entry.grid(row = 0, column=0, columnspan=4, pady = 2, ipady=2)

def click(num):
    entry.insert(tk.END, num)
def log():
    try:
        value = float(entry.get())
        if value <= 0:
            tk.messagebox.showerror("Error", "Cannot calculate logarithm of non-positive numbers")
        else:
            result = str(math.log10(value))
            entry.delete(0, tk.END)
            entry.insert(0, result)
    except:
        tk.messagebox.showerror("Error", "Invalid input for logarithm")
def square_root():
    try:
        value = float(entry.get())
        if value < 0:
            tk.messagebox.showerror("Error", "Cannot calculate square root of a negative number")
        else:
            result = str(math.sqrt(value))
            entry.delete(0, tk.END)
            entry.insert(0, result) 
    except:
        tk.messagebox.showerror("Error", "Invalid input for square root")


def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        tk.messagebox.showerror("Error", "Invalid expression")
def clear():
    entry.delete(0, tk.END)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0) ]
for txt, r, c in buttons:
    tk.Button(frame, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)
tk.Button(frame, text="√", padx=15, pady=5, width=3, command=square_root).grid(row=4, column=0, pady=2)
tk.Button(frame, text="log", padx=15, pady=5, width=3, command=log).grid(row=4, column=2, pady=2)
tk.Button(frame, text='=', padx=15, pady=5, width=9, command=equal).grid(row=5, column=2, pady=2)
tk.Button(frame, text='clear', padx=15, pady=5, width=12, command=clear).grid(row=6, column=0, pady=2)
win.mainloop()