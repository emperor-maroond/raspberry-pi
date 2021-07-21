import RPi.GPIO as GPIO
import time
 
PWM_pin = 33
 
def start_pwm():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PWM_pin, GPIO.OUT)
    GPIO.output(PWM_pin, GPIO.LOW)
    pwm = GPIO.PWM(PWM_pin, 1000)
    pwm.start(0)

def loop():
    while True:
        for dc in range(0, 101, 1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
        for dc in range(100, -1, -1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)

def destroy():
    pwm.stop()
    GPIO.output(PWM_pin, GPIO.LOW)
    GPIO.cleanup()
     
if  __name__ == '__main__':
    start_pwm()
