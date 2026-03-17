import serial
import time
import requests 

# --- CONFIGURATION ---
ARDUINO_PORT = 'COM3'  # <--- CHANGE THIS TO YOUR ACTUAL ARDUINO PORT!
BAUD_RATE = 9600
SERVER_URL = 'http://127.0.0.1:8000/api/telemetry'

try:
    ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    print(f"--- SENDER SCRIPT RUNNING ---")
    print(f"Connected to Arduino on {ARDUINO_PORT}")
    time.sleep(2) 

    while True:
        if ser.in_waiting > 0:
            raw_data = ser.readline().decode('utf-8').strip()
            
            if raw_data.startswith("TELEMETRY"):
                parts = raw_data.split(",")
                
                if len(parts) == 4:
                    payload = {
                        "device_id": "arduino_uno_dummy_node",
                        "temperature": float(parts[1]),
                        "moisture": float(parts[2]),
                        "gas_ppm": int(parts[3])
                    }
                    
                    # SENDING TO SERVER
                    try:
                        response = requests.post(SERVER_URL, json=payload)
                        if response.status_code == 200:
                            print(f"[SUCCESS] Sent {payload['temperature']}°C to the Database!")
                        else:
                            print(f"[ERROR] Server refused the data.")
                    except requests.exceptions.ConnectionError:
                        print("[-] Waiting for server.py to turn on...")

except serial.SerialException:
    print(f"\n[!] Error: Could not connect to {ARDUINO_PORT}. Is the Serial Monitor closed?")
except KeyboardInterrupt:
    print("\n[-] Stopped.")