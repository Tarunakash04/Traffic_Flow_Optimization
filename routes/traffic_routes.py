from flask import Blueprint, request, jsonify
import logging
from utils.validator import validate_traffic_data
from utils.helper import load_json, save_json
from models.optimiser import optimize_traffic
from services.festival_service import adjust_for_festival
from flask import render_template
import json

traffic_bp = Blueprint('traffic', __name__)

@traffic_bp.route('/', methods=['POST'])
def receive_traffic_data():
    data = request.get_json()

    if not data or 'vehicle_data' not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Aggregate vehicle counts from FASTag data
    vehicle_counts = {}
    for entry in data['vehicle_data']:
        lane = entry['lane']
        vehicle_counts[lane] = vehicle_counts.get(lane, 0) + 1

    # Optimize Traffic Signals
    green_times = optimize_traffic(vehicle_counts)

    # Save Data
    formatted_data = {
        "vehicle_counts": vehicle_counts,
        "green_times": green_times,
        "timestamp": data['vehicle_data'][0]['timestamp']
    }
    save_json('./traffic_data.json', formatted_data)
    
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
                     
@traffic_bp.route('/', methods=['GET'])
def view_traffic_data():
    try:
        # Read the latest live traffic data
        with open('./traffic_data.json', 'r') as f:
            data = json.load(f)
        
        # Calculate green times dynamically
        green_times = optimize_traffic(data['vehicle_counts'])
        data['green_times'] = green_times
        
        return render_template('traffic_data.html', data=data)
    
    except FileNotFoundError:
        return render_template('error.html', message="Traffic data not available.")

@traffic_bp.route('/', methods=['GET'])
def display_traffic_data():
    try:
        # Load data from JSON
        data = load_json('./traffic_data.json')

        if not data or 'vehicle_counts' not in data:
            return render_template('error.html', message="No traffic data available.")

        # Extract vehicle counts and calculate green times
        vehicle_counts = data['vehicle_counts']
        green_times = optimize_traffic(vehicle_counts)

        return render_template('traffic_data.html', data={
            'vehicle_counts': vehicle_counts,
            'green_times': green_times
        })
    except FileNotFoundError:
        return render_template('error.html', message="Traffic data not found.")
    except Exception as e:
        logging.error(str(e))
        return render_template('error.html', message="An error occurred.")