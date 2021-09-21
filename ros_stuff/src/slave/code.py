#!/usr/bin/env python3

import numpy as np
import rospy
import RPi.GPIO as GPIO

from my_message.msg import my_message

freq = 200
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

ser_R = []
ser_L = []
sol_R = []
sol_L = []

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

def duty_cycle(alpha, n):
    if n == 1:
        pw = alpha*(2-0.65)/np.pi + 0.65
    if n == 2:
        pw = alpha*(2.1-0.75)/np.pi + 0.75
    T = 1/freq * 1000
    dc = pw/T*100
    return dc
    # pwm.ChangeDutyCycle(dc)

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
    global ser_R, ser_L, sol_R, sol_L
    servo_right    = data.some_floats[0]
    servo_left     = data.some_floats[1]
    solenoid_right = data.some_floats[2]
    solenoid_left  = data.some_floats[3]
    
    if(servo_right==-10 and servo_left==-10 and solenoid_right==-10 and solenoid_left==-10):
        for i in range(0, len(ser_R)):
            pwm1.ChangeDutyCycle(ser_R[i])
            pwm2.ChangeDutyCycle(ser_L[i])
            # ser_L[i] = abs(np.pi-ser_L[i])
            # duty_cycle(ser_R[i], pwm1, 1)
            # duty_cycle(ser_L[i], pwm2, 2)   

            if(sol_R[i] == -1):
                GPIO.output(sol1_pin, 0)
                GPIO.output(sol2_pin, 1)
            if(sol_R[i] == 0):
                GPIO.output(sol1_pin, 1)
                GPIO.output(sol2_pin, 1)
            if(sol_R[i] == 1):
                GPIO.output(sol1_pin, 1)
                GPIO.output(sol2_pin, 0)

            if(sol_L[i] == -1):
                GPIO.output(sol3_pin, 0)
                GPIO.output(sol4_pin, 1)
            if(sol_L[i] == 0):
                GPIO.output(sol3_pin, 1)
                GPIO.output(sol4_pin, 1)
            if(sol_L[i] == 1):
                GPIO.output(sol3_pin, 1)
                GPIO.output(sol4_pin, 0)

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
        ser_R.append(duty_cycle(servo_right, 1))
        servo_left = abs(np.pi-servo_left)
        ser_L.append(duty_cycle(servo_left, 2))
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
    start_pwm()
    listener()
