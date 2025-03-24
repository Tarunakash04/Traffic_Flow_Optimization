from flask import Flask, render_template
from routes.traffic_routes import traffic_bp
from routes.emergency_routes import emergency_bp
from routes.monitor_routes import monitor_bp
from routes.festival_routes import festival_bp
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

# Updated Home Route to Render UI
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
