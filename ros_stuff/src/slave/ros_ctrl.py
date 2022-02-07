#!/usr/bin/env python3


import numpy as np
import rospy as rp
import gpiozero

from gpiozero.pins.pigpio import PiGPIOFactory
from my_message.msg import my_message

# Set-up ROS and serial connection and PINS_____________________________________________________________________
rp.init_node('slave', disable_signals=True)
pub_time = 10/1000
rate = rp.Rate(1/pub_time)

factory = PiGPIOFactory()

servo_R = gpiozero.AngularServo(12, min_pulse_width=0.72/1000, max_pulse_width=2.06/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
servo_L = gpiozero.AngularServo(13, min_pulse_width=0.66/1000, max_pulse_width=2.05/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
     
servo_R.angle = 90
servo_L.angle = 90

sol1_pin = gpiozero.DigitalOutputDevice(5, pin_factory=factory)
sol2_pin = gpiozero.DigitalOutputDevice(6, pin_factory=factory)
sol3_pin = gpiozero.DigitalOutputDevice(19, pin_factory=factory)
sol4_pin = gpiozero.DigitalOutputDevice(26, pin_factory=factory)

sol1_pin.off()
sol2_pin.off() 
sol3_pin.off()
sol4_pin.off() 

# Functions_____________________________________________________________________________________________________
offset = 0
servo_right    = np.pi/2
servo_left     = np.pi/2
solenoid_right = 0
solenoid_left  = 0

def destroy():
    servo_R.angle = None
    servo_L.angle = None
    sol1_pin.off()
    sol2_pin.off() 
    sol3_pin.off()
    sol4_pin.off() 

def r2d(rad):
    return rad*180/np.pi

# Callback ______________________________________________________________________________________________________
def callback(data):
    global servo_right, servo_left, solenoid_right, solenoid_left
    servo_right    = data.some_floats[0]
    servo_left     = data.some_floats[1]
    solenoid_right = data.some_floats[2]
    solenoid_left  = data.some_floats[3]
    # rate.sleep()

def feedback(info):
    global offset
    offset = info.some_floats[2]

    servo_R.angle = 180 - (r2d(servo_right) + offset)
    servo_L.angle = r2d(servo_left) + offset

    if(solenoid_right == -1):
        sol1_pin.on()
        sol2_pin.off()
    if(solenoid_right == 0):
        pass
    if(solenoid_right == 1):
        sol1_pin.off()
        sol2_pin.on()  

    if(solenoid_left == -1):
        sol3_pin.on()
        sol4_pin.off()  
    if(solenoid_left == 0):
        pass               
    if(solenoid_left == 1):
        sol3_pin.off()
        sol4_pin.on()  

def listener():
    try:
        rp.Subscriber("chatter", my_message, callback)
        rp.Subscriber("sensor_data", my_message, feedback)
        while not rp.core.is_shutdown():
            rp.rostime.wallsleep(0.5)
    except KeyboardInterrupt:
        destroy()
        rp.signal_shutdown("Adios")
        print('Bye')

if __name__ == '__main__':
    listener()      