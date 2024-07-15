import pmma
import random
import time

pmma.init()

canvas = pmma.Display()
canvas.create(1280, 720)

draw = pmma.Draw()

events = pmma.Events()

registry = pmma.Registry

n = 0

compute_pipeline = pmma.ComputePipeline(num_threads=None)

class BasicDrawOperation:
    def __init__(self):
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.position = [random.randint(0, 1280), random.randint(0, 720)]

    def render(self):
        draw.circle(self.color, self.position, 20)

    def compute(self):
        self.position = [random.randint(0, 1280), random.randint(0, 720)]
        if n > 130:
            time.sleep(random.random()/10)

objects = []
N = 10
for _ in range(N):
    for _ in range(N):
        inst = BasicDrawOperation()
        compute_pipeline.add(inst.compute, parallel=True)
        objects.append(inst)
    inst = BasicDrawOperation()
    compute_pipeline.add(inst.compute, parallel=False)
    objects.append(inst)

compute_pipeline.train()
x = []
y = []
Y = []
while registry.running:
    t = time.time()
    tot = 0
    for seg in range(len(compute_pipeline.optimizer)):
        tot += compute_pipeline.optimizer[seg]["threads"]
    Y.append(tot/len(compute_pipeline.optimizer))
    x.append(t)

    events.handle()

    dx = time.perf_counter()
    compute_pipeline.execute()
    dy = time.perf_counter()
    y.append(1/(dy-dx))

    canvas.clear()
    for obj in objects:
        obj.render()

    canvas.refresh(refresh_rate=60000)
    n += 1

# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

plt.plot(x, y)  # Plot the chart
plt.plot(x, Y)  # Plot the chart
plt.show()  # display