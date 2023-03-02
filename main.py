# this was the file I was testing on the pico to figure out the serial communication
import select
import sys
import time
from machine import Pin

led = Pin(25, Pin.OUT)

serial = select.poll() #new select object
serial.register(sys.stdin) #register the stdin
TIMEOUT = 0 #0 for dont wait, -1 for wait forever, or timout in seconds
i = 0
while True:
    i += 1
    time.sleep(1) #do what you want
    if serial.poll(TIMEOUT): #is data available? .poll(0) returns an empty list if no data is available
        res = ""
        while serial.poll(TIMEOUT):
            res+=(sys.stdin.read(1))
            print(" hi from pico ")
        print("got:",res)
