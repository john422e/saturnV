import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
pwm.start(0) # Initialization

pwm.ChangeDutyCycle(5) # left -90 deg position
time.sleep(1)
pwm.ChangeDutyCycle(0)
time.sleep(1)

pwm.ChangeDutyCycle(7.5) # neutral position
time.sleep(1)
pwm.ChangeDutyCycle(0)
time.sleep(1)

pwm.ChangeDutyCycle(10) # right +90 deg position
time.sleep(1)
pwm.ChangeDutyCycle(0)
time.sleep(1)

pwm.stop()
GPIO.cleanup()
