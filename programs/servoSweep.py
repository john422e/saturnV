from gpiozero import Servo
import math, os
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

print("Starting pigpiod")
returnedSysCall = os.system("sudo pigpiod")
sleep(2)

factory = PiGPIOFactory()
sPin = 17
servo = Servo(sPin, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

while True:
    for i in range(0, 360):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)
    # reverse it?
    for i in range(360, 0, -1):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)
