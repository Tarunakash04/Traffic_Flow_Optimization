import os

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
