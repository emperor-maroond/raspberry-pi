#!/usr/bin/env python3

from gpiozero.pins import Factory
import numpy as np
import time
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo_R = gpiozero.AngularServo(12, min_pulse_width=0.785/1000, max_pulse_width=2.095/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
# 0.81 2.18
servo_L = gpiozero.AngularServo(13, min_pulse_width=0.72/1000, max_pulse_width=2.09/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)


sol1_pin = gpiozero.DigitalOutputDevice(5, pin_factory=factory)
sol2_pin = gpiozero.DigitalOutputDevice(6, pin_factory=factory)
sol3_pin = gpiozero.DigitalOutputDevice(19, pin_factory=factory)
sol4_pin = gpiozero.DigitalOutputDevice(26, pin_factory=factory)
     
if  __name__ == '__main__':
    try:

        for i in range(0,180):  
            a = np.random.rand()
            if a < 0.3:
                sol1_pin.on()
                sol2_pin.on()
                sol3_pin.on()
                sol4_pin.on()
            if 0.3<=a and a<0.6:
                sol1_pin.off()
                sol2_pin.on()
                sol3_pin.off()
                sol4_pin.on()
            if 0.6<=a and a<1:
                sol1_pin.on()
                sol2_pin.off()
                sol3_pin.on()
                sol4_pin.off()                                              
            servo_R.angle = i
            servo_L.angle = i
            print(i)
            time.sleep(0.01)
        servo_R.angle = None 
        servo_L.angle = None
    except KeyboardInterrupt:
        # pass
        servo_R.angle = None
        servo_L.angle = None
        pass