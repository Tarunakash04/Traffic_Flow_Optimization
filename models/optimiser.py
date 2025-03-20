import logging

def calculate_green_time(vehicle_count):
    """
    Calculate green light time based on vehicle count.
    """
    if vehicle_count > 100:
        green_time = 120
    elif 40 <= vehicle_count <= 100:
        green_time = 75
    else:
        green_time = 60

    logging.info(f"Vehicle Count: {vehicle_count}, Assigned Green Time: {green_time}s")
    return green_time

def optimize_traffic(vehicle_counts):
    """
    Optimize traffic lights based on lane-wise vehicle count.
    """
    green_times = {}
    for lane, count in vehicle_counts.items():
        green_times[lane] = calculate_green_time(count)
    
    logging.info(f"Optimized Green Times: {green_times}")
    return green_times
