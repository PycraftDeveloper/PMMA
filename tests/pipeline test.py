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

compute_pipeline = pmma.ComputePipeline(num_threads=1)

class BasicDrawOperation:
    def __init__(self):
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.position = [0, 0]
        self.id = 0

    def render(self):
        draw.circle(self.color, self.position, 20)

    def compute(self):
        self.position = [random.randint(0, 1280), random.randint(0, 720)]
        time.sleep(random.random()*0.001)

objects = []
N = 10
for _ in range(N):
    for _ in range(N):
        inst = BasicDrawOperation()
        compute_pipeline.add(inst, parallel=True)
        objects.append(inst)

    inst = BasicDrawOperation()
    compute_pipeline.add(inst.compute, parallel=False)
    objects.append(inst)
objects[0].id = 1

compute_pipeline.train()
x = []
y = []
Y = []
while registry.running:
    events.handle()

    compute_pipeline.execute()

    canvas.clear()
    for obj in objects:
        obj.render()

    canvas.refresh(refresh_rate=60000)
    n += 1