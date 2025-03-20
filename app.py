import os
from flask import Flask
from routes.traffic_routes import traffic_bp
from routes.emergency_routes import emergency_bp
from routes.monitor_routes import monitor_bp
from services.logging_services import setup_logging
import config

app = Flask(__name__)
app.register_blueprint(traffic_bp, url_prefix='/traffic')
app.register_blueprint(emergency_bp, url_prefix='/emergency')
app.register_blueprint(monitor_bp, url_prefix='/monitor')

setup_logging()

@app.route('/')
def home():
    return "Traffic Flow Optimizer API is running!"

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
