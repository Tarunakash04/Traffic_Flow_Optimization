import os
import json

DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

# MQTT Config
MQTT_BROKER_URL = os.getenv('MQTT_BROKER_URL', 'localhost')
MQTT_BROKER_PORT = int(os.getenv('MQTT_BROKER_PORT', 1883))
MQTT_TOPIC = os.getenv('MQTT_TOPIC', 'traffic_data')

# Database Config
DB_URI = os.getenv('DATABASE_URI', 'sqlite:///traffic_data.db')

# Logging Config
LOG_FILE = './logs/app.log'

# Festival Mode Management
def load_festival_mode():
    try:
        with open('./data/config.json', 'r') as f:
            data = json.load(f)
            return data.get("FESTIVAL_MODE", False)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

def save_festival_mode(state):
    os.makedirs('./data', exist_ok=True)
    with open('./data/config.json', 'w') as f:
        json.dump({"FESTIVAL_MODE": state}, f)

FESTIVAL_MODE = load_festival_mode()
