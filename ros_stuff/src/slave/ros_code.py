#!/usr/bin/env python3

import numpy as np
import rospy
import gpiozero

from gpiozero.pins.pigpio import PiGPIOFactory
from my_message.msg import my_message

factory = PiGPIOFactory()

servo_R = gpiozero.AngularServo(12, min_pulse_width=0.81/1000, max_pulse_width=2.18/1000,min_angle=0, max_angle=180 ,pin_factory=factory)
servo_L = gpiozero.AngularServo(13, min_pulse_width=0.735/1000, max_pulse_width=2.13/1000,min_angle=0, max_angle=180 ,pin_factory=factory)

sol1_pin = gpiozero.DigitalOutputDevice(5, pin_factory=factory)
sol2_pin = gpiozero.DigitalOutputDevice(6, pin_factory=factory)
sol3_pin = gpiozero.DigitalOutputDevice(19, pin_factory=factory)
sol4_pin = gpiozero.DigitalOutputDevice(26, pin_factory=factory)

servo_right    = 0.0
servo_left     = 0.0
solenoid_right = 0.0
solenoid_left  = 0.0

ser_R = []
ser_L = []
sol_R = []
sol_L = []

# def duty_cycle(alpha, n):
#     if n == 1:
#         pw = alpha*(2-0.65)/np.pi + 0.65
#     if n == 2:
#         pw = alpha*(2.1-0.75)/np.pi + 0.75
#     T = 1/freq * 1000
#     dc = pw/T*100
#     return dc
#     # pwm.ChangeDutyCycle(dc)

def destroy():
    servo_R.angle = None
    servo_L.angle = None
    sol1_pin.value = None
    sol2_pin.value = None 
    sol3_pin.value = None
    sol4_pin.value = None 

def callback(data):
    global servo_right, servo_left, solenoid_right, solenoid_left
    global ser_R, ser_L, sol_R, sol_L
    servo_right    = data.some_floats[0]
    servo_left     = data.some_floats[1]
    solenoid_right = data.some_floats[2]
    solenoid_left  = data.some_floats[3]
    
    if(servo_right==-10 and servo_left==-10 and solenoid_right==-10 and solenoid_left==-10):
        for i in range(0, len(ser_R)):         
            servo_R.angle = ser_R[i]
            servo_L.angle = ser_L[i]

            if(sol_R[i] == -1):
                sol1_pin.off()
                sol2_pin.on()
            if(sol_R[i] == 0):
                sol1_pin.on()
                sol2_pin.on()
            if(sol_R[i] == 1):
                sol1_pin.on()
                sol2_pin.off()                

            if(sol_L[i] == -1):
                sol3_pin.off()
                sol4_pin.on()                
            if(sol_L[i] == 0):
                sol3_pin.on()
                sol4_pin.on()                
            if(sol_L[i] == 1):
                sol3_pin.on()
                sol4_pin.off()                 

            rate.sleep()

            print(ser_R[i])
            # print(servo_left)
            # print(solenoid_right)
            # print(solenoid_left)

        ser_R.clear()
        ser_L.clear()
        sol_R.clear()
        sol_L.clear()

    else:
        # ser_R.append(duty_cycle(servo_right, 1))
        ser_R.append(servo_right * 180/np.pi)
        servo_left = abs(np.pi-servo_left)
        # ser_L.append(duty_cycle(servo_left, 2))
        ser_L.append(servo_left * 180/np.pi)
        sol_R.append(solenoid_right)
        sol_L.append(solenoid_left)

def listener():
    global rate

    try:
        rospy.init_node('slave', disable_signals=True)
        ans = 10/1000
        rate = rospy.Rate(1/ans)
        rospy.Subscriber("chatter", my_message, callback)
        # rospy.spin()
        while not rospy.core.is_shutdown():
            rospy.rostime.wallsleep(0.5)
    except KeyboardInterrupt:
        destroy()
        print('Bye')
        

if __name__ == '__main__':
    listener()
