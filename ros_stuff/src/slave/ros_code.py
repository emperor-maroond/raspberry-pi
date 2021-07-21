#!/usr/bin/env python3

import numpy as np
import rospy

from std_msgs.msg import Float64

def callback(data):
    #rospy.loginfo(data.data)
    print(data.data[0])

def listener():
    rospy.init_node('slave')
    rospy.Subscriber("chatter", Float64, callback)
    rospy.sleep(1)

if __name__ == '__main__':
    listener()