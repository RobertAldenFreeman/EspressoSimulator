import ttkbootstrap as tk
from tkinter import *
import ttkbootstrap as ttk
from ui_components import setup_ui, add_row
import ui_components

def main():
    root = ttk.Window(themename="superhero")
    root.geometry("950x350")
    root.iconbitmap("../../images/logo.ico")
    root.title("Agresso Simulator")

    scrollable_frame, canvas, write_to_file_var = setup_ui(root)

    # Add Row Button
    add_button_frame = ttk.Frame(scrollable_frame)
    add_button_frame.pack(fill='x', side='bottom', pady=10, padx=16)
    add_button = ttk.Button(add_button_frame, text="Add Row", command=lambda: add_row(scrollable_frame, canvas), bootstyle="success")
    add_button.pack(side='right')

    # Initial Row
    add_row(scrollable_frame, canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
