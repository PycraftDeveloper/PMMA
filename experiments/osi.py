import pmma
import time

pmma.init()

pl = pmma.PriorityQueue()
pl.enqueue("a", 1)
pl.enqueue("b", 1)
print(pl.dequeue())

pmma.quit()