# sender.py
# experimenting with serial communication between main computer (my laptop for now,
# have not tried raspberry pi yet) and a pico board
import time
import serial
import subprocess

ser1 = serial.Serial(
    port='/dev/ttyACM0', # this is the only correct one. This is labeled pico 1
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser1.write("new job".encode('utf-8'))
# cmd_str = f'rshell connect /dev/ttyAMC0'
# subprocess.run(cmd_str, shell=True)
# cmd_str = f'rshell cp test1.py /pyboard'
# subprocess.run(cmd_str, shell=True)
