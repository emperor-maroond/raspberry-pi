import numpy as np
import rospy as rp
import serial
import gpiozero

from gpiozero.pins.pigpio import PiGPIOFactory
from my_message.msg import my_message

# Set-up ROS and serial connection and PINS_____________________________________________________________________
rp.init_node('some_data')
pub_time = 10/1000
rate = rp.Rate(1/pub_time)

ser = serial.Serial('/dev/ttyACM5', 19200)
# ser = serial.Serial('/dev/ttyACM0', 19200)
ser.flush()

pub = rp.Publisher('sensor_data', my_message, queue_size=10)

message = my_message()
message.some_floats = []

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

# Functions_____________________________________________________________________________________________________
msg_arr = []

def destroy():
    servo_R.angle = None
    servo_L.angle = None
    sol1_pin.off()
    sol2_pin.off() 
    sol3_pin.off()
    sol4_pin.off() 

def send_message(data):
    for i in range(0, len(data)):
        message.some_floats.append(data[i])
    
    rp.loginfo(message)
    pub.publish(message)
    message.some_floats.clear()

    # rate.sleep()

# Callback ______________________________________________________________________________________________________
def callback(data):
    line = ser.readline().rstrip()
    if line:
        line = line.decode("utf-8").rstrip('\r')
        if line[0] == 'a':
            tmp1 = float(line[1:])
        if line[0] == 'b':
            tmp2 = float(line[1:])
        if line[0] == 'c':
            tmp3 = float(line[1:])
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

    servo_right    = data.some_floats[0]
    servo_left     = data.some_floats[1]
    solenoid_right = data.some_floats[2]
    solenoid_left  = data.some_floats[3]

    servo_R.angle = servo_right
    servo_L.angle = servo_left

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

    rate.sleep()
    print(servo_right)


def listener():
    global rate
    try:
        rp.init_node('slave', disable_signals=True)
        # ans = 10/1000
        # rate = rp.Rate(1/ans)
        rp.Subscriber("chatter", my_message, callback)
        # rp.spin()
        while not rp.core.is_shutdown():
            rp.rostime.wallsleep(0.5)
    except KeyboardInterrupt:
        destroy()
        rp.signal_shutdown("Adios")
        print('Bye')

if __name__ == '__main__':
    listener()      