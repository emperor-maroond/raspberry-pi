#!/usr/bin/env python3

import numpy as np
import rospy
import serial

from my_message.msg import my_message

# Set-up ROS and serial connection___________________________________________________________________________
rospy.init_node('some_data')
pub_time = 10/1000
rate = rospy.Rate(1/pub_time)

# ser = serial.Serial('/dev/ttyACM5', 19200)
ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flush()

pub = rospy.Publisher('sensor_data', my_message, queue_size=2)

message = my_message()
message.some_floats = []

# The code as kids would call it______________________________________________________________________________
msg_arr = []

def send_message(data):
    for i in range(0, len(data)):
        message.some_floats.append(data[i])
    
    # rospy.loginfo(message)
    pub.publish(message)
    message.some_floats.clear()

    # rate.sleep()

if __name__ == '__main__':
    try:  
        while True:       
            line = ser.readline().rstrip()
            if line:
                line = line.decode("utf-8").rstrip('\r')
                if line[0] == 'a':
                    tmp1 = float(line[1:])
                    # msg_arr.append(tmp)
                if line[0] == 'b':
                    tmp2 = float(line[1:])
                    # msg_arr.append(tmp)
                if line[0] == 'c':
                    tmp3 = float(line[1:])
                    # msg_arr.append(tmp)
                if line[0] == 'd':
                    tmp4 = float(line[1:])
                    msg_arr.append(tmp1)
                    msg_arr.append(tmp2)
                    msg_arr.append(tmp3)
                    msg_arr.append(tmp4)
                # print(line)
            if len(msg_arr)==4:
                send_message(msg_arr)
                msg_arr.clear()
    except KeyboardInterrupt:
        ser.close()
        print("Bye bye")
        
