import pygame

sfName = "apollo11launch.wav"
pygame.mixer.init()
pygame.mixer.music.load(sfName)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
