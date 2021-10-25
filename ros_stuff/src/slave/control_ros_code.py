#!/usr/bin/env python3

import numpy as np
import rospy
import gpiozero
import serial

from gpiozero.pins.pigpio import PiGPIOFactory
from my_message.msg import my_message

# Serial set-up_______________________________________________________
ser = serial.Serial('/dev/ttyACM5', 19200)
# ser = serial.Serial('/dev/ttyACM0', 19200)
ser.flush()

# Publisher and publish-message set-up________________________________
# pub = rospy.Publisher('sensor_data', my_message, queue_size=10)

# pub_msg = my_message()
# pub_msg.some_floats = []

# GPIO set-up_________________________________________________________
factory = PiGPIOFactory()

servo_R = gpiozero.AngularServo(12, min_pulse_width=0.785/1000, max_pulse_width=2.095/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)
servo_L = gpiozero.AngularServo(13, min_pulse_width=0.72/1000, max_pulse_width=2.09/1000,min_angle=0, max_angle=180 ,pin_factory=factory, frame_width=4/1000)

servo_R.angle = None
servo_L.angle = None

sol1_pin = gpiozero.DigitalOutputDevice(5, pin_factory=factory)
sol2_pin = gpiozero.DigitalOutputDevice(6, pin_factory=factory)
sol3_pin = gpiozero.DigitalOutputDevice(19, pin_factory=factory)
sol4_pin = gpiozero.DigitalOutputDevice(26, pin_factory=factory)

sol1_pin.off()
sol2_pin.off() 
sol3_pin.off()
sol4_pin.off() 

# Intitialize some variables__________________________________________
servo_right    = 0.0
servo_left     = 0.0
solenoid_right = 0.0
solenoid_left  = 0.0

ser_R = []
ser_L = []
sol_R = []
sol_L = []

data_arr = []

# The functions_______________________________________________________
def read_sensors():
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
            data_arr.append(tmp1)
            data_arr.append(tmp2)
            data_arr.append(tmp3)
            data_arr.append(tmp4)
    if len(data_arr) == 4:
        data_arr.clear()

def destroy():
    servo_R.angle = None
    servo_L.angle = None
    sol1_pin.off()
    sol2_pin.off() 
    sol3_pin.off()
    sol4_pin.off() 

def callback(data):
    global servo_right, servo_left, solenoid_right, solenoid_left
    global ser_R, ser_L, sol_R, sol_L

    read_sensors()

    servo_right    = data.some_floats[0]
    servo_left     = data.some_floats[1]
    solenoid_right = data.some_floats[2]
    solenoid_left  = data.some_floats[3]
    
    if(servo_right==-10 and servo_left==-10 and solenoid_right==-10 and solenoid_left==-10):
        for i in range(0, len(ser_R)):         
            servo_R.angle = ser_R[i]
            servo_L.angle = ser_L[i]

            if(sol_R[i] == -1):
                sol1_pin.on()
                sol2_pin.off()
            if(sol_R[i] == 0):
                pass
                # sol1_pin.off()
                # sol2_pin.off()
            if(sol_R[i] == 1):
                sol1_pin.off()
                sol2_pin.on()                

            if(sol_L[i] == -1):
                sol3_pin.on()
                sol4_pin.off()                
            if(sol_L[i] == 0):
                pass
                # sol3_pin.off()
                # sol4_pin.off()                
            if(sol_L[i] == 1):
                sol3_pin.off()
                sol4_pin.on()                 

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
        
# Main code___________________________________________________________
if __name__ == '__main__':
    listener()
