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
    vehicle_counts = {}
    data = {
        "vehicle_data": [],
        "vehicle_counts": {}
    }

    lane_config = {
        "Lane_1": 25,
        "Lane_2": 75,
        "Lane_3": 120,
        "Lane_4": 10
    }

    for lane, count in lane_config.items():
        vehicle_data = generate_vehicle_data(lane, count)
        data["vehicle_data"].extend(vehicle_data)
        vehicle_counts[lane] = len(vehicle_data)

    data["vehicle_counts"] = vehicle_counts

    with open('traffic_data.json', 'w') as f:
        json.dump(data, f, indent=2)

    print("Traffic data generated and saved to traffic_data.json")

if __name__ == "__main__":
    generate_traffic_data()
