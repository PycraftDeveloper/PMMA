import pmma

pmma.init(log_information=True, log_development=True)

events = pmma.Events()

while True:
    events.handle()
    #events.handle()

    pmma.compute()

pmma.quit()