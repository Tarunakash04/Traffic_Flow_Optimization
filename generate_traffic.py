import json
import random

def generate_vehicle_data(lane, vehicle_count):
    vehicle_types = ['car', 'truck', 'bus', 'bike']
    data = []
    
    for i in range(vehicle_count):
        vehicle_data = {
            "fastag_id": f"FASTAG{str(random.randint(1, 999)).zfill(3)}",
            "vehicle_type": random.choice(vehicle_types),
            "lane": lane,
            "timestamp": "2025-03-19T22:30:00"
        }
        data.append(vehicle_data)
    return data

def generate_traffic_data():
    data = {
        "vehicle_data": []
    }

    lane_config = {
        "Lane_1": 120,
        "Lane_2": 75,
        "Lane_3": 35,
        "Lane_4": 10
    }

    for lane, count in lane_config.items():
        data["vehicle_data"].extend(generate_vehicle_data(lane, count))

    with open('traffic_data.json', 'w') as f:
        json.dump(data, f, indent=2)

    print("Traffic data generated and saved to traffic_data.json")

if __name__ == "__main__":
    generate_traffic_data()
