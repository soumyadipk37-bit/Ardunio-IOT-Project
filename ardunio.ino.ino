// --- TIMING VARIABLES ---
unsigned long lastTime = 0;
const long timerDelay = 3000; // Send data every 3000 milliseconds (3 seconds)

void setup() {
  // Turn on the serial port at the exact speed Python is listening (9600)
  Serial.begin(9600);
}

void loop() {
  // Check if 3 seconds have passed
  if ((millis() - lastTime) > timerDelay) {
    
    // 1. Generate realistic dummy sensor data
    float temperature = 22.0 + (random(-20, 20) / 10.0);
    float moisture = 45.0 + (random(-50, 50) / 10.0);
    int gas_ppm = random(300, 400);

    // 2. Send the data to Python! 
    // Format must be: TELEMETRY,temp,moisture,gas
    Serial.print("TELEMETRY,");
    Serial.print(temperature);
    Serial.print(",");
    Serial.print(moisture);
    Serial.print(",");
    
    // CRITICAL: This last one MUST be println so Python knows the line is finished!
    Serial.println(gas_ppm); 

    // Reset the timer
    lastTime = millis();
  }
}