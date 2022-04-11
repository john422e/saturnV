from gpiozero import Servo
import math
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
sPin = 11
servo = Servo(sPin, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

while True:
    for i in range(0, 360):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)