import pygame

pygame.init()
pygame.joystick.init()

display = pygame.display.set_mode((800, 600))

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.init())

while True:
    for event in pygame.event.get():
        print(event)