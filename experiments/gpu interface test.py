import pmma

pmma.init(log_information=True)

gpus = pmma.GPUs()
gpus.identify_gpus()

controllers = pmma.Controllers()
controllers.identify_controllers()

pmma.quit()