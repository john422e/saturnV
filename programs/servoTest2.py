import os
from gpiozero import Servo
import math
from time import sleep
from decimal import Decimal
from gpiozero.pins.pigpio import PiGPIOFactory

print("Starting pigpiod")
returnedSysCall = os.system("sudo pigpiod")
sleep(2)

factory = PiGPIOFactory()
sPin = 17
servo = Servo(sPin, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

# store the current angle and initialize to 0 (middle)
defaultPos = 0
currentPos = defaultPos
servo.value = currentPos

try:
    stepSpeed = float(input("Set step speed (in seconds, 0.05 by default): ")) # time to wait in between steps
except:
    print("Invalid entry. Setting step speed to 0.05")
    stepSpeed = 0.05

def setPosition(newPos):
    # position value should be between -1 and 1, MAX 2 DECIMAL PLACES
    global currentPos

    stepInc = Decimal('0.01')

    if newPos > currentPos:
        step = 1 * stepInc
    else:
        step = -1 * stepInc

    while currentPos != newPos:
        # set new position
        print(currentPos)
        #servo.value = currentPos
        servo.value = math.sin(math.radians(currentPos))
        # increment currentPos
        currentPos += step
        #sleep
        sleep(stepSpeed)

setting = True

while setting:
    print("SET POSITION -1 to 1 (max 2 decimal places):")
    print("'q' to quit")
    userInput = input()
    if userInput == 'q':
        setting = False
        break
    else:
        try:
            setPosition(Decimal(userInput))
        except:
            print("INVALID ENTRY")
            continue

# reset servo position
servo.value = defaultPos
