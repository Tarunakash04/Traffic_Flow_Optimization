from flask import Flask, render_template, jsonify, request
from routes.traffic_routes import traffic_bp
from routes.emergency_routes import emergency_bp  # You might need to create this
from routes.monitor_routes import monitor_bp
from routes.festival_routes import festival_bp  # You might need to create this
from routes.accident_routes import accident_bp
from routes.green_corridor_routes import green_corridor_bp
from services.logging_services import setup_logging
import config

app = Flask(__name__)

# Registering Blueprints
app.register_blueprint(traffic_bp, url_prefix='/traffic')
app.register_blueprint(emergency_bp, url_prefix='/emergency')
app.register_blueprint(monitor_bp, url_prefix='/monitor')
app.register_blueprint(festival_bp, url_prefix='/festival')
app.register_blueprint(accident_bp, url_prefix='/accident')
app.register_blueprint(green_corridor_bp, url_prefix='/green_corridor')

setup_logging()

# Global variables to manage state
festival_mode = False
emergency_lane = None

# Updated Home Route to Render UI
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/junction')
def junction_ui():
    return render_template('junction.html')

@app.route('/toggle_festival', methods=['POST'])
def toggle_festival():
    global festival_mode
    festival_mode = not festival_mode
    return jsonify(festival_mode=festival_mode)

@app.route('/set_emergency_lane', methods=['POST'])
def set_emergency_lane():
    global emergency_lane
    data = request.get_json()
    lane = data.get('lane')
    if lane in ["Lane_1", "Lane_2", "Lane_3", "Lane_4", "off"]:
        emergency_lane = lane if lane != "off" else None
        return jsonify(emergency_lane=emergency_lane)
    return jsonify(error="Invalid lane"), 400

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)