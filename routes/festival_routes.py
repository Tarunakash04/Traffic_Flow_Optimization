from flask import Blueprint, request, jsonify

festival_bp = Blueprint('festival', __name__)

@festival_bp.route('/', methods=['GET'])
def festival_management():
    return jsonify({"message": "Festival Traffic Management active"})

