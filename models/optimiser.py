import logging
import config

def optimize_traffic(vehicle_counts, emergency_detected=False):
    green_times = {}
    festival_mode = getattr(config, "FESTIVAL_MODE", False)

    if emergency_detected:
        logging.info("🚨 Emergency detected. Activating Green Corridor!")
        # Set all lanes to a fixed green time for the emergency vehicle
        for lane in vehicle_counts:
            green_times[lane] = 180  # 3 Minutes Green Light
        return green_times

    mode = "Festival Mode" if festival_mode else "Normal Mode"
    logging.info(f"Optimizing Traffic in {mode}")

    # Apply festival or normal logic
    for lane, count in vehicle_counts.items():
        if festival_mode:
            if count > 150:
                green_times[lane] = 150
            elif count > 100:
                green_times[lane] = 130
            elif count >= 40:
                green_times[lane] = 90
            else:
                green_times[lane] = 70
        else:
            if count > 100:
                green_times[lane] = 120
            elif count >= 40:
                green_times[lane] = 75
            else:
                green_times[lane] = 60
        
        logging.info(f"Lane: {lane}, Vehicle Count: {count}, Green Time: {green_times[lane]}s")
        
    return green_times
