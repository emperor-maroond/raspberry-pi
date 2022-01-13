#!/usr/bin/env python3

import numpy as np
import serial
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo_R = gpiozero.AngularServo(12, min_pulse_width=0.76/1000, max_pulse_width=2.095/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
servo_L = gpiozero.AngularServo(13, min_pulse_width=0.72/1000, max_pulse_width=2.11/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)


ser = serial.Serial('/dev/ttyACM0', 19200)
ser.flush()

offset = 0
msg_arr = []
if  __name__ == '__main__':
    try:  
        while True:       
            line = ser.readline().rstrip()
            if line:
                line = line.decode("utf-8").rstrip('\r')
                if line[0] == 'a':
                    tmp1 = float(line[1:])
                    # msg_arr.append(tmp)
                if line[0] == 'b':
                    tmp2 = float(line[1:])
                    # msg_arr.append(tmp)
                if line[0] == 'c':
                    tmp3 = float(line[1:])
                    # msg_arr.append(tmp)
                if line[0] == 'd':
                    tmp4 = float(line[1:])
                    msg_arr.append(tmp1)
                    msg_arr.append(tmp2)
                    msg_arr.append(tmp3)
                    msg_arr.append(tmp4)
                # print(line)
            if len(msg_arr)==4:
                offset = tmp3
                msg_arr.clear()

            servo_R.angle = 90 - offset
            servo_L.angle = 90 + offset
            print(offset)
    except KeyboardInterrupt:
        ser.close()
        print("Bye bye")

