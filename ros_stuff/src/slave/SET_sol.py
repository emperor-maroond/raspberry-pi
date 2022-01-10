#!/usr/bin/env python3

from gpiozero.pins import Factory
import numpy as np
import time
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

sol1_pin = gpiozero.DigitalOutputDevice(5, pin_factory=factory)
sol2_pin = gpiozero.DigitalOutputDevice(6, pin_factory=factory)
sol3_pin = gpiozero.DigitalOutputDevice(19, pin_factory=factory)
sol4_pin = gpiozero.DigitalOutputDevice(26, pin_factory=factory)
     
if  __name__ == '__main__':
    try:
        sol1_pin.off() # IN
        sol2_pin.off() # OUT
        sol3_pin.off() # IN
        sol4_pin.off() # OUT
    except KeyboardInterrupt:
        # pass
        pass
