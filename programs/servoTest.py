import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

# store the current angle
currentAngle = 0
stepWait = 0.05 # time to wait in between steps


def setAngle(newAngle):
    global currentAngle

    if newAngle > currentAngle:
        step = 1
    else:
        step = -1

    # step between currentAngle and newAngle by steps of 1
    for angle in range(currentAngle, newAngle, step):
        duty = angle / 18 + 3
        GPIO.output(servoPIN, True)
        pwm.ChangeDutyCycle(duty)

        print(angle)
        time.sleep(stepWait)

        GPIO.output(servoPIN, False)
        pwm.ChangeDutyCycle(duty)

    # now update currentAngle
    currentAngle = newAngle
    # stop motor
    pwm.ChangeDutyCycle(0)

pwm.start(0) # Initialization

setting = True

while setting:
    angle = input("SET ANGLE ('q' to quit): ")
    if angle == 'q':
        setting = False
        break
    else:
        try:
            setAngle(int(angle))
        except:
            print("INPUT INTEGERS ONLY")
            continue
\
pwm.stop()
GPIO.cleanup()
