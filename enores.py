import pygame

import fileManager

fM = fileManager.FileManager()

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(fM.mus_Static)

def play():
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

def stop():
    pygame.mixer.music.stop()