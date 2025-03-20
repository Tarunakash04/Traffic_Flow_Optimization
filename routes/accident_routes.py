from flask import Blueprint, jsonify

accident_bp = Blueprint('accident', __name__)

@accident_bp.route('/', methods=['GET'])
def accident_alert():
    return jsonify({"message": "Accident Detection and Alert system active"})
