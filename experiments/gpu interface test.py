import pmma

pmma.init()

gpus = pmma.GPUs()
gpus.identify_gpus()

controllers = pmma.Controllers()
controllers.identify_controllers()