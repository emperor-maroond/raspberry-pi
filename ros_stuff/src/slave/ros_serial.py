#!/usr/bin/env python3

from operator import le
import numpy as np
from genpy import message
import rospy
import serial

from my_message.msg import my_message

# Set-up ROS and serial connection___________________________________________________________________________
rospy.init_node('some_data')
# pub_time = 100/1000
# rate = rospy.Rate(1/pub_time)

ser = serial.Serial('/dev/ttyACM5', 19200)
ser.flush()

pub = rospy.Publisher('sensor_data', my_message, queue_size=10)

message = my_message()
message.some_floats = []

# The code as kids would call it______________________________________________________________________________
msg_arr = []

def send_message(data):
    for i in range(0, len(data)):
        message.some_floats.append(data[i])
    
    rospy.loginfo(message)
    pub.publish(message)
    message.some_floats.clear()

    # rate.sleep()

if __name__ == '__main__':
    try:  
        while True:       
            line = ser.readline().rstrip()
            if line:
                line = float(line.decode("utf-8"))
                msg_arr.append(line)
                # print(line)
            if len(msg_arr)==4:
                send_message(msg_arr)
                msg_arr.clear()
    except KeyboardInterrupt:
        ser.close()
        print("Bye bye")
        
