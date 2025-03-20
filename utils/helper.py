import json
import logging

def load_json(file_path):
    """
    Load data from a JSON file.
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading JSON from {file_path}: {e}")
        return None

def save_json(file_path, data):
    """
    Save data to a JSON file.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Data saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving JSON to {file_path}: {e}")
