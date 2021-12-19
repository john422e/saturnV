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


#!/usr/bin/env python

# Light each LED in sequence, and repeat.
numLEDs = 50
client = opc.Client('localhost:7890')

while True:
	for i in range(numLEDs):
		pixels = [ (0,0,0) ] * numLEDs
		pixels[i] = (255, 255, 255)
		client.put_pixels(pixels)
		time.sleep(0.01)
