from flask import Blueprint, request, jsonify
import logging
from utils.validator import validate_traffic_data
from utils.helper import load_json, save_json
from models.optimiser import optimize_traffic
from services.festival_service import adjust_for_festival

traffic_bp = Blueprint('traffic', __name__)

# Existing route for traffic data
@traffic_bp.route('/', methods=['POST'])
def receive_traffic_data():
    data = request.get_json()
    logging.info(f"Received Data: {data}")

    if not data or 'vehicle_data' not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Aggregate vehicle counts from FASTag data
    vehicle_counts = {}
    for entry in data['vehicle_data']:
        lane = entry['lane']
        vehicle_counts[lane] = vehicle_counts.get(lane, 0) + 1

    # Save Data
    formatted_data = {
        "vehicle_counts": vehicle_counts,
        "timestamp": data['vehicle_data'][0]['timestamp']
    }
    save_json('./data/traffic_data.json', formatted_data)
    logging.info(f"FASTag data processed. Vehicle Counts: {vehicle_counts}")

    # Optimize Traffic Signals
    green_times = optimize_traffic(vehicle_counts)

    return jsonify({"message": "Traffic data processed successfully.", 
                     "vehicle_counts": vehicle_counts,
                     "green_times": green_times}), 200

# New route for Festival Traffic Management
@traffic_bp.route('/festival', methods=['POST'])
def festival_management():
    data = request.get_json()

    if not data or 'vehicle_counts' not in data:
        return jsonify({"error": "Invalid data"}), 400

    green_times = adjust_for_festival(data)
    return jsonify({"message": "Festival traffic management applied", 
                     "green_times": green_times}), 200
