#!/usr/bin/env python3

from gpiozero.pins import Factory
import numpy as np
import time
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo_R = gpiozero.AngularServo(12, min_pulse_width=0.74/1000, max_pulse_width=2.1/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
servo_L = gpiozero.AngularServo(13, min_pulse_width=0.72/1000, max_pulse_width=2.11/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
     
if  __name__ == '__main__':
    servo_R.angle = 90
    servo_L.angle = 90
