from flask import Blueprint, jsonify
import json

monitor_bp = Blueprint('monitor', __name__)

@monitor_bp.route('/monitor/traffic', methods=['GET'])
def get_traffic_data():
    try:
        with open('./data/traffic_data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No traffic data available"}), 404

@monitor_bp.route('/monitor/emergency', methods=['GET'])
def get_emergency_data():
    try:
        with open('./data/emergency_queue.json', 'r') as f:
            data = f.readlines()
            return jsonify([json.loads(line) for line in data])
    except FileNotFoundError:
        return jsonify({"error": "No emergency data available"}), 404
