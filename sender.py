# sender.py
# experimenting with serial communication between main computer (my laptop for now,
# have not tried raspberry pi yet) and a pico board
import time
import serial
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


class Sender:
  ser1 = serial.Serial(
    port='/dev/ttyACM0', # this is the only correct one. This is labeled pico 1
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
  )

  ser2 = serial.Serial(
    port='/dev/ttyACM0', # Change this according to connection methods, e.g. /dev/ttyUSB0
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
  )

  ser3 = serial.Serial(
    port='/dev/ttyACM0', # Change this according to connection methods, e.g. /dev/ttyUSB0
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
  )

  ser4 = serial.Serial(
    port='/dev/ttyACM0', # Change this according to connection methods, e.g. /dev/ttyUSB0
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
  )

  ser1_name = '/dev/ttyACMO'
  ser2_name = '/dev/ttyACM1'
  ser3_name = '/dev/ttyACM2'
  ser4_name = '/dev/ttyACM3'

  picos = {}
  picos.append(ser1)
  picos.append(ser2)
  picos.append(ser3)
  picos.append(ser4)
  

  """
  listen for when jobs are finished
  """
  def start_listening(self):
    while True:
      bytes_to_read1 = self.ser1.inWaiting()
      bytes_to_read2 = self.ser2.inWaiting()
      bytes_to_read3 = self.ser3.inWaiting()
      bytes_to_read4 = self.ser4.inWaiting()

      self.ser1.write("job".encode('utf-8'))
      if (bytes_to_read1 > 0):
        result = self.ser1.read(bytes_to_read1)
        if result == 'NO':
          # turn light off
          pass

      self.ser2.write("job".encode('utf-8'))
      if (bytes_to_read2 > 0):
        result = self.ser2.read(bytes_to_read2)
        if result == 'NO':
          # turn light off
          pass

      self.ser3.write("job".encode('utf-8'))
      if (bytes_to_read3 > 0):
        result = self.ser3.read(bytes_to_read3)
        if result == 'NO':
          # turn light off
          pass

      self.ser4.write("job".encode('utf-8'))
      if (bytes_to_read4 > 0):
        result = self.ser4.read(bytes_to_read4)
        if result == 'NO':
          # turn light off
          GPIO.output(18,GPIO.LOW)


  """
  send the job to one of the available picos
  params
  job needs to be the filename of a python file
  """
  def new_job(self, job):
    # send the job to one of the available ones
    for pico in self.picos:
        pico.write("job".encode('utf-8'))
        bytes_to_read = pico.inWaiting()
        if (bytes_to_read > 0):
          result = pico.read(bytes_to_read)
          if result == 'No':
            # turn light on
            GPIO.output(18,GPIO.HIGH)
            pico.write(job.encode('utf-8'))
        return None