import logging
import json

def handle_emergency(data):
    logging.info("Handling emergency vehicle detection.")
    vehicle_type = data.get("vehicle_type")
    location = data.get("location")

    # Example logic to handle emergency
    if vehicle_type == "ambulance" or vehicle_type == "fire_truck" or vehicle_type == "police":
        logging.info(f"Emergency vehicle detected: {vehicle_type} at {location}")
        return {"status": "Emergency priority activated", "location": location}
    else:
        logging.info("Non-emergency vehicle detected.")
        return {"status": "No emergency detected"}
