import os, time, threading
import opc

def startUp():
    returnedValue = serverCall = "sudo ../../fadecandy/bin/fcserver-rpi saturnVconfig.json"
    # call program here
    os.system(serverCall)
    print('returned value:', returnedValue)

x = threading.Thread(target=startUp)
x.start()

time.sleep(2)

while True:
    continue
    time.sleep(0.01)
