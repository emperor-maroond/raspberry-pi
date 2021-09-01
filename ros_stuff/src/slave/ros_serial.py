#!/usr/bin/env python3

import numpy as np
from genpy import message
import rospy
import serial

from my_message.msg import my_message

# Set-up ROS and serial connection___________________________________________________________________________

rospy.init_node('some_data')
pub_time = 100/1000
rate = rospy.Rate(1/pub_time)

ser = serial.Serial('/dev/ttyACM0', 19200, timeout = pub_time)

pub = rospy.Publisher('sensor_data', my_message, queue_size=10)

message = my_message()
message.some_floats = []

# The code as kids would call it______________________________________________________________________________
def send_message(data):
    message.some_floats.append(data)
    
    rospy.loginfo(message)
    pub.publish(message)
    message.some_floats.clear()

    rate.sleep()

if __name__ == '__main__':
    try:
        while True:
            line = ser.readline().decode('utf-8').rstrip()
            send_message(line)
    except KeyboardInterrupt:
        print("Bye bye")