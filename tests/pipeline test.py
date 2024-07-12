import pmma
import random
import time

canvas = pmma.Display()
canvas.create(1280, 720)

draw = pmma.Draw()

events = pmma.Events()

compute_pipeline = pmma.ComputePipeline()

class BasicDrawOperation:
    def __init__(self):
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.position = [random.randint(0, 1280), random.randint(0, 720)]

    def render(self):
        draw.circle(self.color, self.position, 20)

    def compute(self):
        self.position = [random.randint(0, 1280), random.randint(0, 720)]

objects = []
N = 1000
for _ in range(N):
    inst = BasicDrawOperation()
    compute_pipeline.add_compute_function(inst.compute, parallel=True)
    objects.append(inst)

n = 0
while True:
    #print(canvas.get_fps())
    if n == 500:
        compute_pipeline.request_experimental_thread_evaluation()

    events.handle()

    start = time.perf_counter()
    compute_pipeline.execute()
    end = time.perf_counter()
    print(compute_pipeline.experiment_using_threads, n, compute_pipeline.num_threads, end-start)

    canvas.clear()
    for obj in objects:
        obj.render()

    canvas.refresh()
    n += 1