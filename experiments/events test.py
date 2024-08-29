import pygame
import time

pygame.init()

display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joystick in joysticks:
    joystick.init()

while True:
    for event in pygame.event.get():
        print(event)

    time.sleep(1/30)