import json
import time
import random
import requests
import logging

VEHICLE_TYPES = ['car', 'bus', 'truck', 'bike']
FASTAG_IDS = ['FASTAG001', 'FASTAG002', 'FASTAG003', 'FASTAG004']

def generate_vehicle_data():
    lanes = ['Lane_1', 'Lane_2', 'Lane_3', 'Lane_4']
    vehicle_data = []
    for lane in lanes:
        for _ in range(random.randint(5, 20)):  # Random vehicle count
            vehicle_data.append({
                "fastag_id": random.choice(FASTAG_IDS),
                "vehicle_type": random.choice(VEHICLE_TYPES),
                "lane": lane,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })
    return vehicle_data

def simulate_sensor_data():
    logging.info("Starting RFID sensor data simulation.")
    while True:
        vehicle_data = generate_vehicle_data()
        try:
            response = requests.post("http://localhost:5000/traffic", json={"vehicle_data": vehicle_data})
            logging.info(f"Data Sent: {vehicle_data}, Response: {response.status_code}")
        except Exception as e:
            logging.error(f"Failed to send data: {e}")
        time.sleep(10)

if __name__ == "__main__":
    simulate_sensor_data()
