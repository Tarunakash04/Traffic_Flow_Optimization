from flask import Blueprint, request, jsonify
import logging
from utils.helper import load_json, save_json

emergency_bp = Blueprint('emergency', __name__)

@emergency_bp.route('/emergency', methods=['POST'])
def detect_emergency():
    data = request.get_json()
    if not data or 'vehicle_type' not in data or 'location' not in data:
        return jsonify({"error": "Invalid emergency data"}), 400
    
    if data['vehicle_type'].lower() in ['ambulance', 'firetruck', 'police']:
        emergency_data = load_json('./data/emergency_queue.json') or []
        emergency_data.append(data)
        save_json('./data/emergency_queue.json', emergency_data)
        logging.info("Emergency detected and logged.")
        return jsonify({"message": "Emergency vehicle detected and logged."}), 200
    else:
        return jsonify({"message": "No emergency detected."}), 200

@emergency_bp.route('/monitor/emergency', methods=['GET'])
def monitor_emergency():
    data = load_json('./data/emergency_queue.json')
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "No emergency data available"}), 404
