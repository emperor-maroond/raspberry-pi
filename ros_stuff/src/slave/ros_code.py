#!/usr/bin/env python3

import numpy as np
import rospy

from my_message.msg import my_message

servo_right    = 0.0
servo_left     = 0.0
solenoid_right = 0.0
solenoid_left  = 0.0

def callback(data):
    global servo_right, servo_left, solenoid_right, solenoid_left
    servo_right    = data.some_floats[0]
    servo_left     = data.some_floats[1]
    solenoid_right = data.some_floats[2]
    solenoid_left  = data.some_floats[3]
    print(servo_right)
    print(servo_left)
    print(solenoid_right)
    print(solenoid_left)

def listener():
    rospy.init_node('slave')
    rospy.Subscriber("chatter", my_message, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()