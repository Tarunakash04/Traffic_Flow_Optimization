# Traffic flow optimizer

This project implements a **traffic flow optimizer** using **FASTag RFID detection**. Vehicles are detected via their FASTag, and data is transmitted to a backend for processing. The system dynamically adjusts traffic signal timing based on vehicle count.

---

## 🚀 Features  
- **Vehicle Detection**: Uses FASTag data to detect vehicles in real-time.  
- **Traffic Signal Optimization**: Adjusts signal timings based on the number of vehicles per lane.  
- **Data Transmission**: Uses HTTP (POST requests) to send vehicle data.  
- **Lane-Specific Processing**: Computes green time dynamically for each lane. . 

---

## 🗂 Project Structure  

```bash
/fastag-traffic-optimizer
│── app.py                 # Main Flask application  
│── sensor_service.py      # Simulates FASTag sensor data transmission  
│── generate_traffic.py    # Generates random vehicle data for testing  
│── requirements.txt       # Dependencies  
│── README.md              # Documentation  
│  
├── config.py               # Configuration (e.g., Ports, MQTT settings)  
├── data/                   # Data storage (JSON files)  
├── logs/                   # Application logs  
├── models/                 # Traffic optimization logic  
├── routes/                 # API routes for traffic and emergency handling  
├── services/               # Sensor and notification services  
└── utils/                  # Helper functions and validators  
