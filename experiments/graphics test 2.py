import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 100, 100)

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    s = time.perf_counter()
    for i in range(1_000_000):
        pygame.draw.rect(screen, (0, 255, 0), rect)
    e = time.perf_counter()
    print((1/(e-s)))

    pygame.display.update()