#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
 
freq = 100
PWM1_pin = 13
PWM2_pin = 12 # GPIO 12
 
def start_pwm():
    global pwm1, pwm2
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(PWM1_pin, GPIO.OUT)
    GPIO.output(PWM1_pin, GPIO.LOW)
    pwm1 = GPIO.PWM(PWM1_pin, freq)
    pwm1.start(0)

    GPIO.setup(PWM2_pin, GPIO.OUT)
    GPIO.output(PWM2_pin, GPIO.LOW)
    pwm2 = GPIO.PWM(PWM2_pin, freq)
    pwm2.start(0)

def duty_cycle(alpha, pwm, n):
    if n == 1:
        pw = alpha*3/400 + 0.65
    if n == 2:
        pw = alpha*3/400 + 0.75
    T = 1/freq * 1000
    dc = pw/T*100
    pwm.ChangeDutyCycle(dc)

def destroy():
    pwm1.stop()
    pwm2.stop()
    GPIO.output(PWM1_pin, GPIO.LOW)
    GPIO.output(PWM2_pin, GPIO.LOW)
    GPIO.cleanup()
     
if  __name__ == '__main__':
    start_pwm()
    duty_cycle(90, pwm1, 1)
    duty_cycle(0, pwm2, 2)
    # pwm.ChangeDutyCycle(7.5)
    for i in range(0,3):
        # duty_cycle(90*i)
        time.sleep(1)
        print(90*i)
    destroy()