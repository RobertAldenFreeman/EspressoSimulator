import ttkbootstrap as ttk
from tkinter import *
from data_generation import sensor_data
from sensor_data_client import is_valid_port

def setup_ui(root, server_ip, server_port):
    # Main frame
    main_frame = ttk.Frame(root)
    main_frame.pack(fill='both', expand=True)

    # Server Connection Frame
    server_conn_frame = ttk.Frame(root)
    server_conn_frame.pack(fill='x', side='top', pady=10, padx=70)

    # Server IP Entry
    ttk.Label(server_conn_frame, text="Server IP:").pack(side='left', padx=(0, 10))
    server_ip_var = StringVar(value='127.0.0.1')  # Default IP
    server_ip_entry = ttk.Entry(server_conn_frame, textvariable=server_ip_var)
    server_ip_entry.pack(side='left')

    # Server Port Entry
    ttk.Label(server_conn_frame, text="Port:").pack(side='left', padx=(10, 10))
    server_port_var = StringVar(value='12345')  # Default Port
    server_port_entry = ttk.Entry(server_conn_frame, textvariable=server_port_var)
    server_port_entry.pack(side='left')

    # Scrollable area setup
    canvas = Canvas(main_frame)
    v_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=v_scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    v_scrollbar.pack(side="right", fill="y")

    # Scrollable frame inside the canvas
    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Checkbox for enabling file writing
    write_to_file_var = BooleanVar(value=False)
    write_checkbox_frame = ttk.Frame(root)
    write_checkbox_frame.pack(fill='x', side='bottom', pady=10, padx=70)
    write_checkbox = ttk.Checkbutton(write_checkbox_frame, text="Write to file", variable=write_to_file_var, bootstyle="primary")
    write_checkbox.pack(side='right')

    return scrollable_frame, canvas, write_to_file_var

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

def add_row(parent, canvas):
    row_frame, widgets = create_row_with_widgets(parent)
    sensor_data.append(widgets)
    row_frame.pack(padx=10, pady=5, fill='x')
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Validate the input fields
    for key, entry in widgets.items():
        if key in ['min_value', 'max_value', 'frequency', 'duration']:
            entry.config(validate="key", validatecommand=(entry.register(is_valid_number), '%P'))
            
    
def is_valid_number(value):
    try:
        # Check if it's a non-negative number or empty
        return value.isdigit() or value == "" or (value.replace('.', '', 1).isdigit() and float(value) >= 0)
    except ValueError:
        return False
