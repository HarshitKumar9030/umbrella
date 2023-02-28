import serial

ser = serial.Serial('/dev/ttyACM0', 9600) # Change the port name to match your Arduino's port

while True:
    try:
        data = ser.readline().strip()
        print(data)
    except serial.SerialException:
        print("Lost connection to the Arduino")
