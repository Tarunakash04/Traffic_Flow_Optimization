from flask import Blueprint, request, jsonify
import json
import config

monitor_bp = Blueprint('monitor', __name__)

@monitor_bp.route('/traffic', methods=['GET'])
def get_traffic_data():
    try:
        with open('./data/traffic_data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No traffic data available"}), 404

@monitor_bp.route('/emergency', methods=['GET'])
def get_emergency_data():
    try:
        with open('./data/emergency_queue.json', 'r') as f:
            data = f.readlines()
            return jsonify([json.loads(line) for line in data])
    except FileNotFoundError:
        return jsonify({"error": "No emergency data available"}), 404

@monitor_bp.route('/toggle_festival', methods=['POST'])
def toggle_festival():
    try:
        data = request.get_json()
        if data is None or 'festival_mode' not in data:
            return jsonify({"error": "Invalid data. Please provide 'festival_mode'."}), 400

        festival_mode = data['festival_mode']
        config.FESTIVAL_MODE = festival_mode
        return jsonify({"message": f"Festival mode {'enabled' if festival_mode else 'disabled'}."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
