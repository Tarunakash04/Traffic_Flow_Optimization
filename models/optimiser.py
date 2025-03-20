import logging
import config

def optimize_traffic(vehicle_counts, emergency_detected=False):
    green_times = {}

    if emergency_detected:
        logging.info("🚨 Emergency detected. Activating Green Corridor!")
        for lane in vehicle_counts:
            green_times[lane] = 180  # Fixed Green Light for Emergency
        return green_times

    mode = "Festival Mode" if config.FESTIVAL_MODE else "Normal Mode"
    logging.info(f"Optimizing Traffic in {mode}")

    for lane, count in vehicle_counts.items():
        if config.FESTIVAL_MODE:
            green_times[lane] = 150 if count > 150 else (130 if count > 100 else (90 if count >= 40 else 70))
        else:
            green_times[lane] = 120 if count > 100 else (75 if count >= 40 else 60)

        logging.info(f"Lane: {lane}, Vehicle Count: {count}, Green Time: {green_times[lane]}s")

    return green_times
