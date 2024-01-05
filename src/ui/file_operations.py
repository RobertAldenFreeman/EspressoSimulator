import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def write_to_file(data, filename='sensor_data_output.json'):
    if not data:
        logging.warning("No data provided to write to file.")
        return

    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data successfully written to {filename}")
    except IOError as io_err:
        logging.error(f"IO error occurred: {io_err}")
    except TypeError as type_err:
        logging.error(f"Type error in data: {type_err}")
    except json.JSONDecodeError as json_err:
        logging.error(f"JSON decoding error: {json_err}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

