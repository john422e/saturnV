import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz


def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(servoPin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servoPin, False)
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

pwm.stop()
GPIO.cleanup()
