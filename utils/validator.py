import jsonschema
from jsonschema import validate
import logging

# Schema for traffic data
traffic_schema = {
    "type": "object",
    "properties": {
        "vehicle_counts": {
            "type": "object",
            "additionalProperties": {"type": "integer"}
        },
        "timestamp": {"type": "string"}
    },
    "required": ["vehicle_counts", "timestamp"]
}

# Schema for emergency data
emergency_schema = {
    "type": "object",
    "properties": {
        "vehicle_type": {"type": "string"},
        "location": {"type": "string"},
        "timestamp": {"type": "string"}
    },
    "required": ["vehicle_type", "location", "timestamp"]
}

def validate_traffic_data(data):
    """
    Validate traffic data against the schema.
    """
    try:
        validate(instance=data, schema=traffic_schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        logging.error(f"Traffic data validation failed: {e}")
        return False

def validate_emergency_data(data):
    """
    Validate emergency data against the schema.
    """
    try:
        validate(instance=data, schema=emergency_schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        logging.error(f"Emergency data validation failed: {e}")
        return False
