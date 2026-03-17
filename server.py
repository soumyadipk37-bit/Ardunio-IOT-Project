from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI()

# Allow web browsers to read the data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup Database
def init_db():
    conn = sqlite3.connect('telemetry.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sensor_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, device_id TEXT, temperature REAL, moisture REAL, gas_ppm INTEGER)''')
    conn.commit()
    conn.close()

init_db()

class SensorData(BaseModel):
    device_id: str
    temperature: float
    moisture: float
    gas_ppm: int

# Route to RECEIVE data
@app.post("/api/telemetry")
async def receive_data(data: SensorData):
    conn = sqlite3.connect('telemetry.db')
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO sensor_data (timestamp, device_id, temperature, moisture, gas_ppm) VALUES (?, ?, ?, ?, ?)",
              (timestamp, data.device_id, data.temperature, data.moisture, data.gas_ppm))
    conn.commit()
    conn.close()
    return {"status": "Success", "message": "Data saved to database!"}

# Route to SEND data to the graph
@app.get("/api/telemetry")
async def get_data():
    conn = sqlite3.connect('telemetry.db')
    c = conn.cursor()
    c.execute("SELECT timestamp, device_id, temperature, moisture, gas_ppm FROM sensor_data ORDER BY id DESC LIMIT 15")
    rows = c.fetchall()
    conn.close()
    
    result = []
    for row in rows:
        result.append({"timestamp": row[0], "device_id": row[1], "temperature": row[2], "moisture": row[3], "gas_ppm": row[4]})
    return result