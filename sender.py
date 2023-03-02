# sender.py
# experimenting with serial communication between main computer (my laptop for now,
# have not tried raspberry pi yet) and a pico board
import time
import serial

ser = serial.Serial(
  port='/dev/ttyACM0', # Change this according to connection methods, e.g. /dev/ttyUSB0
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

i = 0

while True:
    i+=1
    ser.write('hello'.encode('utf-8'))

    if i == 5:
        break

while True:
    bytes_to_read = ser.inWaiting()
    # print(f"bytes_to_read: {bytes_to_read}")
    if (bytes_to_read > 0):
      output = ser.read(bytes_to_read)
      print('there is output')
      print(output)