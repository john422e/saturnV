import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

# store the current angle
currentAngle = 0

def setAngle(angle):
    if angle > currentAngle:
        step = 1
    else:
        step = -1

    for i in range(currentAngle, angle):
        duty = angle / 18 + 3
        GPIO.output(servoPIN, True)
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(servoPIN, False)
        pwm.ChangeDutyCycle(duty)


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
