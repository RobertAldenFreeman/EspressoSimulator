import ttkbootstrap as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")
root.geometry("950x350")
root.iconbitmap("../../images/logo.ico")
root.title("Agresso Simulator")

def is_non_negative_number(P):
    # Check if the string is a non-negative number
    return P.isdigit() or P == ""

def create_row_with_widgets(parent):
    frame = ttk.Frame(parent)

    # Label for the Combobox
    label_combobox = ttk.Label(frame, text="Sensor", anchor="center")
    label_combobox.grid(row=0, column=0, pady=5, sticky="ew")

    # Create a Combobox
    sensor_types = ["Thermistor", "Flux"]
    combobox = ttk.Combobox(frame, bootstyle="primary", values=sensor_types)
    combobox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    combobox.current(0)

    labels_text_fields = ["Pin", "Min Value", "Max Value", "Frequency", "Duration"]

    # Create labels and entries in a loop
    for i in range(5):
        # Label for each text field
        label_entry = ttk.Label(frame, text=labels_text_fields[i], anchor="center")
        label_entry.grid(row=0, column=i+1, pady=5, sticky="ew")

        # Text field (Entry widget)
        entry = ttk.Entry(frame, bootstyle="secondary")
        entry.grid(row=1, column=i+1, padx=5, pady=5, sticky="ew")

    return frame

def add_row():
    row_frame = create_row_with_widgets(scrollable_frame)
    row_frame.pack(padx=10, pady=5, fill='x')
    canvas.configure(scrollregion=canvas.bbox("all"))

def run_sim():
    print("Run Simulator function called")

# Main frame
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Scrollable area setup
canvas = tk.Canvas(main_frame)
v_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
h_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

# Positioning scrollbars
canvas.pack(side="left", fill="both", expand=True)
v_scrollbar.pack(side="right", fill="y")
h_scrollbar.pack(side="bottom", fill="x")

# Scrollable frame inside the canvas
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# Button to add new rows, outside the scrolling area
add_button_frame = ttk.Frame(scrollable_frame)
add_button_frame.pack(fill='x', side='bottom', pady=10, padx=16)
add_button = ttk.Button(add_button_frame, text="Add Row", command=add_row, bootstyle="success")
add_button.pack(side='right')

# Add a single row
add_row()

# Run frame
run_frame = ttk.Frame(root)
run_frame.pack(fill='x', side='bottom', pady=10, padx=70)
run_button = ttk.Button(run_frame, text="Run Simulator", command=run_sim, bootstyle="primary")
run_button.pack(side='right')


root.mainloop()
