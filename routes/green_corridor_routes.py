from flask import Blueprint, request, jsonify
import logging
from utils.helper import load_json, save_json
from models.optimiser import optimize_traffic

green_corridor_bp = Blueprint('green_corridor', __name__)

@green_corridor_bp.route('/activate', methods=['POST'])
def activate_green_corridor():
    try:
        data = request.get_json()

        # Check for emergency detection
        if not data or 'emergency_detected' not in data:
            return jsonify({"error": "Invalid data. Provide 'emergency_detected'."}), 400

        emergency_detected = data['emergency_detected']
        
        # Load existing traffic data
        traffic_data = load_json('./data/traffic_data.json')
        vehicle_counts = traffic_data.get('vehicle_counts', {})

        green_times = optimize_traffic(vehicle_counts, emergency_detected)

        return jsonify({"message": "Green Corridor Activated" if emergency_detected else "Normal Traffic Mode", 
                         "green_times": green_times}), 200
    except Exception as e:
        logging.error(f"Error activating Green Corridor: {e}")
        return jsonify({"error": str(e)}), 500
