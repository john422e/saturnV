currentAngle = 0

def stepper(angle):
    global currentAngle
    if angle > currentAngle:
        step = 1
    else:
        step = -1
    for i in range(currentAngle, angle, step):
        print(i)

    currentAngle = angle


stepper(10)

stepper(0)
