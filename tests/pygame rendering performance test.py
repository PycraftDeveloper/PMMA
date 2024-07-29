import pygame
import time

pygame.init()

display = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

N = 1_000_000
t = 1
points = []
while t < N+1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display.fill([0, 0, 0])

    tt = 0
    for _ in range(10):
        for _ in range(t):
            start = time.perf_counter()
            pygame.draw.rect(display, [255, 255, 255], [0, 0, 10, 10])
            end = time.perf_counter()
            tt += end-start

    print((t, 1/(tt/10)))
    points.append((t, 1/(tt/10)))

    t += 1

    #pygame.display.update()

    #clock.tick(2000)

print(points)
