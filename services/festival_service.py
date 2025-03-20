import logging

def adjust_for_festival(traffic_data):
    """
    Adjust traffic light timings based on festival traffic.
    """
    green_times = {}
    threshold = 200

    for lane, count in traffic_data.get("vehicle_counts", {}).items():
        if count > threshold:
            green_times[lane] = 150  # Set higher green time for high traffic
        else:
            green_times[lane] = 60  # Default green time

    logging.info(f"Festival Adjustment Applied: {green_times}")
    return green_times
