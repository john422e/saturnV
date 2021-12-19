import os, threading, time
import opc

#!/usr/bin/env python

print("RUNNING LIGHTS")
# Light each LED in sequence, and repeat.
numLEDs = 50
client = opc.Client('localhost:7890')

black = [ (0,0,0) ] * numLEDs
white = [ (255,255,255) ] * numLEDs

# Fade to white
client.put_pixels(black)
time.sleep(0.5)
