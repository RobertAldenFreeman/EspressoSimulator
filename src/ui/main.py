import ttkbootstrap as tk
from tkinter import *
import ttkbootstrap as ttk
from ui_components import setup_ui, add_row
from data_generation import run_sim  # Ensure this is correctly imported

def main():
    # Server details (change these to your server's IP and port)
    SERVER_IP = '127.0.0.1'  # Replace with your server's IP
    SERVER_PORT = 12345       # Replace with your server's port

    root = ttk.Window(themename="superhero")
    root.geometry("950x450")
    root.iconbitmap("../../images/logo.ico")
    root.title("Agresso Simulator")

    scrollable_frame, canvas, write_to_file_var = setup_ui(root, SERVER_IP, SERVER_PORT)

    # Add Row Button
    add_button_frame = ttk.Frame(scrollable_frame)
    add_button_frame.pack(fill='x', side='bottom', pady=10, padx=16)
    add_button = ttk.Button(add_button_frame, text="Add Row", command=lambda: add_row(scrollable_frame, canvas), bootstyle="success")
    add_button.pack(side='right')

    # Initialize Run Frame
    run_frame = ttk.Frame(root)
    run_frame.pack(fill='x', side='bottom', pady=10, padx=70)

    # Run Simulation Button
    run_button = ttk.Button(run_frame, text="Run Simulator", command=lambda: run_sim(scrollable_frame, write_to_file_var, SERVER_IP, SERVER_PORT), bootstyle="primary")
    run_button.pack(side='right')

    # Initial Row
    add_row(scrollable_frame, canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
