import json
import random
import ttkbootstrap as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")
root.geometry("950x350")
root.iconbitmap("../../images/logo.ico")
root.title("Agresso Simulator")

# TODO: Add the non-negative number inputs for the text fields
def is_non_negative_number(P):
    # Check if the string is a non-negative number
    return P.isdigit() or P == ""

def create_row_with_widgets(parent):
    frame = ttk.Frame(parent)
    widgets = {}

    # Label and Combobox for Sensor Type
    label_combobox = ttk.Label(frame, text="Sensor", anchor="center")
    label_combobox.grid(row=0, column=0, pady=5, sticky="ew")
    sensor_types = ["Thermistor", "Flux"]
    combobox = ttk.Combobox(frame, bootstyle="primary", values=sensor_types)
    combobox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    combobox.current(0)
    widgets["sensor_type"] = combobox

    # Labels and Entries for other parameters
    labels_text_fields = ["Pin", "Min Value", "Max Value", "Frequency", "Duration"]
    for i, label in enumerate(labels_text_fields):
        label_entry = ttk.Label(frame, text=label, anchor="center")
        label_entry.grid(row=0, column=i+1, pady=5, sticky="ew")
        entry = ttk.Entry(frame, bootstyle="secondary")
        entry.grid(row=1, column=i+1, padx=5, pady=5, sticky="ew")
        widgets[label.lower().replace(" ", "_")] = entry

    return frame, widgets

# Variable to hold the checkbox state
write_to_file_var = BooleanVar(value=False)
sensor_data = []

def add_row():
    row_frame, widgets = create_row_with_widgets(scrollable_frame)
    sensor_data.append(widgets)
    row_frame.pack(padx=10, pady=5, fill='x')
    canvas.configure(scrollregion=canvas.bbox("all"))

def get_data_from_ui():
    data = []
    for widgets in sensor_data:
        sensor_info = {
            "sensor_type": widgets["sensor_type"].get(),
            "pin": widgets["pin"].get(),
            "min_value": float(widgets["min_value"].get()),
            "max_value": float(widgets["max_value"].get()),
            "frequency": float(widgets["frequency"].get()),
            "duration": float(widgets["duration"].get()),
            "generated_data": []
        }
        data.append(sensor_info)
    return data

def generate_sensor_data():
    data = get_data_from_ui()

    for sensor_info in data:
        min = sensor_info["min_value"]
        max = sensor_info["max_value"]

        # TODO: Move this logic to the text field's validate function
        if min >= max:
            print("Error: min >= max, skipping this iteration")
            continue

        for _ in range(int(sensor_info["duration"] * sensor_info["frequency"])):
            value = random.uniform(min, max)
            sensor_info["generated_data"].append(value)

    return data

def run_sim():
    generated_data = generate_sensor_data()
    print(generated_data)  # Printing the generated data

    # Check if the Write to file checkbox is checked. 
    # If so, the file writing should be able to close the file handle if
    if write_to_file_var.get():
        try:
            with open('sensor_data_output.json', 'w') as file:
                json.dump(generated_data, file, indent=4)
            print("Data written to sensor_data_output.json")
        except Exception as e:
            print("An error occurred:", e)


# Main frame
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Scrollable area setup
canvas = tk.Canvas(main_frame)
v_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=v_scrollbar.set)

# Positioning scrollbars
canvas.pack(side="left", fill="both", expand=True)
v_scrollbar.pack(side="right", fill="y")

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

# Checkbox for enabling file writing
write_checkbox_frame = ttk.Frame(root)
write_checkbox_frame.pack(fill='x', side='bottom', pady=10, padx=70)
write_checkbox = ttk.Checkbutton(write_checkbox_frame, text="Write to file", variable=write_to_file_var, bootstyle="primary")
write_checkbox.pack(side='right')

root.mainloop()