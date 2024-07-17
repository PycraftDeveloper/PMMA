# main.py
if __name__ == "__main__":
    import time
    import compute_module
    import pygame

    N = 100_000
    objects = []
    funcs = []

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pygame Window')

    # Populate the objects and funcs lists
    for _ in range(N):
        inst = compute_module.MyClass()
        funcs.append(inst.compute)
        objects.append(inst)

    # Main application loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Execute compute functions (this should be triggered appropriately in your application)
        start_time = time.time()
        compute_module.execute_compute_functions(funcs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")

        pygame.display.flip()

    pygame.quit()