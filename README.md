# Real-Time IoT Sensor Telemetry System

A full-stack IoT application designed to bridge physical hardware with web-based data visualization. This project demonstrates the integration of embedded systems, backend APIs, and frontend dashboards.

## 🚀 Features
* **Hardware Interfacing:** Reads sensor data from an Arduino Uno via UART Serial communication.
* **Backend API:** A high-performance FastAPI (Python) server to handle data ingestion and retrieval.
* **Database:** Persistent storage using SQLite to log historical sensor readings.
* **Live Dashboard:** A real-time web interface using Chart.js to visualize temperature, moisture, and gas levels.

## 🛠️ Tech Stack
* **Hardware:** Arduino Uno (C++)
* **Backend:** Python, FastAPI, Uvicorn
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, JavaScript (Chart.js)

## 📡 System Architecture
1. **Arduino:** Samples data and sends it over Serial (USB).
2. **Python Bridge:** Listens to the COM port and sends HTTP POST requests to the API.
3. **FastAPI:** Receives data, timestamps it, and saves it to the SQL database.
4. **Web Browser:** Fetches data via HTTP GET and updates the graph every 3 seconds.

---
*Developed as part of my ECE portfolio.*
