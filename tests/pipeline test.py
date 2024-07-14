import pmma
import random
import time

pmma.init()

canvas = pmma.Display()
canvas.create(1280, 720)

draw = pmma.Draw()

events = pmma.Events()

compute_pipeline = pmma.ComputePipeline(num_threads=2)

class BasicDrawOperation:
    def __init__(self):
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.position = [random.randint(0, 1280), random.randint(0, 720)]

    def render(self):
        draw.circle(self.color, self.position, 20)

    def compute(self):
        self.position = [random.randint(0, 1280), random.randint(0, 720)]

objects = []
N = 10_000
for _ in range(N):
    inst = BasicDrawOperation()
    compute_pipeline.add_compute_function(inst.compute, parallel=True)
    objects.append(inst)

n = 0
while True:
    #print(canvas.get_fps())

    events.handle()

    compute_pipeline.execute()

    canvas.clear()
    for obj in objects:
        obj.render()

    canvas.refresh(refresh_rate=60)
    n += 1