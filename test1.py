# import time
# import serial

# ser1 = serial.Serial(
#     port='/dev/ttyACM0', # this is the only correct one. This is labeled pico 1
#     baudrate = 115200,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=1
# )

# while True:
#     ser1.write("print('hello')")
#     time.sleep(1)

print('hello from test1.py')