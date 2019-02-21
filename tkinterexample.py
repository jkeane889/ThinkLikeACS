# hello word through tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
my_label = ttk.Label(window, text="Hello World")
my_label.grid(row=1, column=1)

messagebox.showinfo("Information", "Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")

window.mainloop()
