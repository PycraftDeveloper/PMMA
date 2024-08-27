import pmma

pmma.init()

gpus = pmma.GPUs()
gpus.identify_gpus()