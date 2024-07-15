import pmma
import random
import time

pmma.init()

canvas = pmma.Display()
canvas.create(1280, 720)

draw = pmma.Draw()

events = pmma.Events()

registry = pmma.Registry

compute_pipeline = pmma.ComputePipeline(num_threads=None)

class BasicDrawOperation:
    def __init__(self):
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.position = [random.randint(0, 1280), random.randint(0, 720)]

    def render(self):
        draw.circle(self.color, self.position, 20)

    def compute(self):
        self.position = [random.randint(0, 1280), random.randint(0, 720)]

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

#compute_pipeline.train()
n = 0
x = []
y = []
while registry.running:
    y.append(canvas.get_fps())
    x.append(n)

    events.handle()

    compute_pipeline.execute()

    canvas.clear()
    for obj in objects:
        obj.render()

    canvas.refresh(refresh_rate=60000)
    n += 1


# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

plt.plot(x, y)  # Plot the chart
plt.show()  # display