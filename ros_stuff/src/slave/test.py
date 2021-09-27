#!/usr/bin/env python3
from gpiozero.pins import Factory
import numpy as np
import time
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo_R = gpiozero.AngularServo(12, min_pulse_width=0.81/1000, max_pulse_width=2.18/1000,min_angle=0, max_angle=180 ,pin_factory=factory)
servo_L = gpiozero.AngularServo(13, min_pulse_width=0.72/1000, max_pulse_width=2.13/1000,min_angle=0, max_angle=180 ,pin_factory=factory)
     
if  __name__ == '__main__':
    try:
        servo_R.angle = 90
        servo_L.angle = 90
        time.sleep(5)
        servo_R.angle = None 
        servo_L.angle = None
    except KeyboardInterrupt:
        pass
        servo_R.angle = None
        servo_L.angle = None