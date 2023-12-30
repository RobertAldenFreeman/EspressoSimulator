from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(themename="superhero")
root.geometry("500x350")
root.title("Agresso Simulator")

button = tb.Button(text="Click Me!", bootstyle="primary")
button.pack(pady=20)

root.mainloop()
