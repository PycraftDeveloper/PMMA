import pmma
import time

pmma.init(log_information=True)

gpus = pmma.GPUs()
gpus.identify_gpus()

controllers = pmma.Controllers()
controllers.identify_controllers()

time.sleep(30)

pmma.quit()