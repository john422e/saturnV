import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

try:
    while True:
        print("TURN")
        p.ChangeDutyCycle(5)
        time.sleep(1.5)
        print("TURN")
        p.ChangeDutyCycle(7.5)
        time.sleep(1.5)
        print("TURN")
        p.ChangeDutyCycle(10)
        time.sleep(1.5)
        print("TURN")
        p.ChangeDutyCycle(12.5)
        time.sleep(1.5)
        print("TURN")
        p.ChangeDutyCycle(10)
        time.sleep(1.5)
        print("TURN")
        p.ChangeDutyCycle(7.5)
        time.sleep(1.5)
        print("TURN")
        p.ChangeDutyCycle(5)
        time.sleep(1.5)
        print("TURN")
        p.ChangeDutyCycle(2.5)
        time.sleep(1.5)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
