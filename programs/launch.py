import pygame, threading, os, time

def startUp():
    returnedValue = serverCall = "sudo ../../fadecandy/bin/fcserver-rpi saturnVconfig.json"
    # call program here
    os.system(serverCall)
    print('returned value:', returnedValue)

x = threading.Thread(target=startUp)
x.start()

time.sleep(2)


print("RUNNING LIGHTS")
# Light each LED in sequence, and repeat.
numLEDs = 50
client = opc.Client('localhost:7890')

sfName = "../apollo11launch.wav"
pygame.mixer.init(frequency=48000)
pygame.mixer.music.load(sfName)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    for i in range(numLEDs):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[i] = (255, 255, 255)
        client.put_pixels(pixels)
        time.sleep(0.01)
    continue
