import pygame

sfName = "../apollo11launch.wav"
pygame.mixer.init(frequency=48000)
pygame.mixer.music.load(sfName)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
