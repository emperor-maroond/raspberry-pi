#!/usr/bin/env python3

import numpy as np
import serial
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory
from time import time

factory = PiGPIOFactory()

servo_R = gpiozero.AngularServo(12, min_pulse_width=0.72/1000, max_pulse_width=2.06/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
servo_L = gpiozero.AngularServo(13, min_pulse_width=0.66/1000, max_pulse_width=2.05/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
     
sol1_pin = gpiozero.DigitalOutputDevice(5, pin_factory=factory)
sol2_pin = gpiozero.DigitalOutputDevice(6, pin_factory=factory)
sol3_pin = gpiozero.DigitalOutputDevice(19, pin_factory=factory)
sol4_pin = gpiozero.DigitalOutputDevice(26, pin_factory=factory)

ser = serial.Serial('/dev/ttyACM0', 19200)
ser.flush()

offset = 0
msg_arr = []
boom = 1
a = time()
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

            servo_R.angle = 180 - (90 + offset)
            servo_L.angle = (90 + offset)

    except KeyboardInterrupt:
        ser.close()
        sol1_pin.off() # IN
        sol2_pin.off() # OUT
        sol3_pin.off() # IN
        sol4_pin.off() # OUT
        print("Bye bye")

