#!/usr/bin/env python3

import numpy as np
import rospy
import RPi.GPIO as GPIO

from my_message.msg import my_message

freq = 100
PWM1_pin = 13
PWM2_pin = 12 # GPIO 12
sol1_pin = 5
sol2_pin = 6
sol3_pin = 19
sol4_pin = 26

servo_right    = 0.0
servo_left     = 0.0
solenoid_right = 0.0
solenoid_left  = 0.0

def start_pwm():
    global pwm1, pwm2
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(PWM1_pin, GPIO.OUT)
    GPIO.output(PWM1_pin, 0)
    pwm1 = GPIO.PWM(PWM1_pin, freq)
    pwm1.start(0)

    GPIO.setup(PWM2_pin, GPIO.OUT)
    GPIO.output(PWM2_pin, 0)
    pwm2 = GPIO.PWM(PWM2_pin, freq)
    pwm2.start(0)

    GPIO.setup(sol1_pin, GPIO.OUT)
    GPIO.output(sol1_pin, 1)

    GPIO.setup(sol2_pin, GPIO.OUT)
    GPIO.output(sol2_pin, 1)
    
    GPIO.setup(sol3_pin, GPIO.OUT)
    GPIO.output(sol3_pin, 1)
    
    GPIO.setup(sol4_pin, GPIO.OUT)
    GPIO.output(sol4_pin, 1)

def duty_cycle(alpha, pwm, n):
    if n == 1:
        pw = alpha*(2-0.65)/np.pi + 0.65
    if n == 2:
        pw = alpha*(2.1-0.75)/np.pi + 0.75
    T = 1/freq * 1000
    dc = pw/T*100
    pwm.ChangeDutyCycle(dc)

def destroy():
    pwm1.stop()
    pwm2.stop()
    GPIO.output(PWM1_pin, 0)
    GPIO.output(PWM2_pin, 0)
    GPIO.output(sol1_pin, 0)
    GPIO.output(sol2_pin, 0)
    GPIO.output(sol3_pin, 0)
    GPIO.output(sol4_pin, 0)
    GPIO.cleanup()

def callback(data):
    global servo_right, servo_left, solenoid_right, solenoid_left
    servo_right    = data.some_floats[0]
    servo_left     = data.some_floats[1]
    solenoid_right = data.some_floats[2]
    solenoid_left  = data.some_floats[3]

    # duty_cycle(servo_right, pwm1, 1)
    # duty_cycle(servo_left, pwm2, 2)

    # if(solenoid_right == -1):
    #     GPIO.output(sol1_pin, 0)
    #     GPIO.output(sol2_pin, 1)
    # if(solenoid_right == 0):
    #     GPIO.output(sol1_pin, 1)
    #     GPIO.output(sol2_pin, 1)
    # if(solenoid_right == 1):
    #     GPIO.output(sol1_pin, 1)
    #     GPIO.output(sol2_pin, 0)

    # if(solenoid_left == -1):
    #     GPIO.output(sol3_pin, 0)
    #     GPIO.output(sol4_pin, 1)
    # if(solenoid_left == 0):
    #     GPIO.output(sol3_pin, 1)
    #     GPIO.output(sol4_pin, 1)
    # if(solenoid_left == 1):
    #     GPIO.output(sol3_pin, 1)
    #     GPIO.output(sol4_pin, 0)

    print(servo_right)
    print(servo_left)
    print(solenoid_right)
    print(solenoid_left)

def listener():
    try:
        rospy.init_node('slave')
        rospy.Subscriber("chatter", my_message, callback)
        rospy.spin()
    except KeyboardInterrupt:
        # destroy()
        print('Bye')

if __name__ == '__main__':
    # start_pwm()
    listener()