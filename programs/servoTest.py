import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

try:
    while True:
        print("TURN")
        #p.ChangeDutyCycle(5)
        time.sleep(0.5)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
