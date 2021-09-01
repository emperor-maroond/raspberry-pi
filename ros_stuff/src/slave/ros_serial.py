#!/usr/bin/env python3

import serial

ser = serial.Serial('/dev/ttyACM0', 19200, timeout=0.1)
# ser.flush()

if __name__ == '__main__':
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)