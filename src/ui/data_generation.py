from file_operations import write_to_file
from sensor_data_client import SensorDataClient
import random
import time
import threading

sensor_data = []  # This should be populated with references to UI widgets

def get_data_from_ui(scrollable_frame):
    data = []
    for widgets in sensor_data:
        try:
            sensor_info = {
                "sensor_type": widgets["sensor_type"].get(),
                "pin": widgets["pin"].get(),
                "min_value": float(widgets["min_value"].get()),
                "max_value": float(widgets["max_value"].get()),
                "frequency": float(widgets["frequency"].get()),
                "duration": float(widgets["duration"].get())
            }
            data.append(sensor_info)
        except ValueError:
            print("Invalid input detected. Please ensure all fields are correctly filled.")
    return data

def generate_sensor_data(scrollable_frame):
    data = get_data_from_ui(scrollable_frame)
    for sensor_info in data:
        sensor_info["generated_data"] = []

        # Check min and max value constraints
        if sensor_info["min_value"] >= sensor_info["max_value"]:
            print("Skipping sensor with invalid min/max values.")
            continue

        # Generate data with two decimal points
        for _ in range(int(sensor_info["duration"] * sensor_info["frequency"])):
            value = round(random.uniform(sensor_info["min_value"], sensor_info["max_value"]), 2)
            sensor_info["generated_data"].append(value)

    return data

import json
import socket

def send_sensor_data(data, server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        for sensor in data:
            serialized_data = json.dumps(sensor).encode('utf-8')
            sock.sendto(serialized_data, (server_ip, server_port))


def run_sim(scrollable_frame, write_to_file_var, server_ip, server_port):
    generated_data = generate_sensor_data(scrollable_frame)
    print(generated_data)  # Printing the generated data

    # Thread for writing to file
    if write_to_file_var.get():
        file_thread = threading.Thread(target=write_to_file, args=(generated_data,))
        file_thread.start()

    # Thread for sending data via UDP
    def send_data():
        client = SensorDataClient(server_ip, server_port)
        start_time = time.time()
        for sensor in generated_data:
            duration = sensor["duration"]
            frequency = sensor["frequency"]
            interval = 1 / frequency if frequency > 0 else 0

            for _ in range(int(duration * frequency)):
                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time > duration:
                    break

                serialized_data = json.dumps(sensor).encode('utf-8')
                client.send_sensor_data(serialized_data)
                time.sleep(interval - (time.time() - current_time))  # Adjust for processing time

        client.close()

    send_thread = threading.Thread(target=send_data)
    send_thread.start()

    # Wait for threads to finish
    if write_to_file_var.get():
        file_thread.join()
    send_thread.join()

