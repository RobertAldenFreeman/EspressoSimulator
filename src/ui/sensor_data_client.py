import socket
import json
import logging

class SensorDataClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error as e:
            logging.error(f"Failed to create socket: {e}")
            raise

    def send_sensor_data(self, data_point):
        try:
            serialized_data = json.dumps(data_point).encode('utf-8')
            self.sock.sendto(serialized_data, (self.server_ip, self.server_port))
        except json.JSONEncodeError as e:
            logging.error(f"JSON encoding error: {e}")
        except socket.error as e:
            logging.error(f"Socket error occurred: {e}")

    def close(self):
        try:
            self.sock.close()
        except socket.error as e:
            logging.error(f"Error closing socket: {e}")

# Validation for the port field
def is_valid_port(value):
    try:
        port = int(value)
        return 0 <= port <= 65535
    except ValueError:
        return False