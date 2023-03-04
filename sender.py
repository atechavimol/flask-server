# sender.py
# experimenting with serial communication between main computer (my laptop for now,
# have not tried raspberry pi yet) and a pico board
import time
import serial
import subprocess

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
  picos[ser1] = (ser1_name, None)
  picos[ser2] = (ser2_name, None)
  picos[ser3] = (ser3_name, None)
  picos[ser4] = (ser4_name, None)
  

  """
  listen for when jobs are finished
  """
  def start_listening(self):
    while True:
      bytes_to_read1 = self.ser1.inWaiting()
      bytes_to_read2 = self.ser2.inWaiting()
      bytes_to_read3 = self.ser3.inWaiting()
      bytes_to_read4 = self.ser4.inWaiting()

      if (bytes_to_read1 > 0):
        result = self.ser1.read(bytes_to_read1)
        if result == 'done':
          self.picos[self.ser1] = None

      if (bytes_to_read2 > 0):
        result = self.ser2.read(bytes_to_read2)
        if result == 'done':
          self.picos[self.ser2] = None

      if (bytes_to_read3 > 0):
        result = self.ser3.read(bytes_to_read3)
        if result == 'done':
          self.picos[self.ser3] = None

      if (bytes_to_read4 > 0):
        result = self.ser4.read(bytes_to_read4)
        if result == 'done':
          self.picos[self.ser4] = None


  """
  send the job to one of the available picos
  params
  job needs to be the filename of a python file
  """
  def new_job(self, job):
    # send the job to one of the available ones
    for pico in self.picos:
      if job not in self.picos.values():
        if self.picos[pico][1] == None:
          self.picos[pico] = job
          self.picos[pico].write("new job".encode('utf-8')'))
          cmd_str = f'rshell connect {self.picos[pico][0]}'
          subprocess.run(cmd_str, shell=True)
          cmd_str = f'rshell cp {job} /pyboard'
          subprocess.run(cmd_str, shell=True)
          return None
        else:
          return "pico is busy"
      else:
        break