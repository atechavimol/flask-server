import time
import serial
import subprocess

cmd_str = f'rshell connect /dev/ttyAMC0'
subprocess.run(cmd_str, shell=True)
cmd_str = f'rshell cp test3.py /pyboard'
subprocess.run(cmd_str, shell=True)