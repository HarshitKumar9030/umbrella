from flask import Flask, render_template
import serial

app = Flask(__name__)

# Configure the serial connection
ser = serial.Serial('/dev/ttyACM0', 9600)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_rain_detection")
def start_rain_detection():
    # Send a command to start rain detection
    ser.write(b'start')
    return "Rain detection started"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
