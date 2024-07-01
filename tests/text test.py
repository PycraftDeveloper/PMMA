import pmma

pmma.init()

display = pmma.Display()

t = pmma.Text()
print(t.render("Hello World! This is a $(RbUdz)REALLY $(s=80) cool demonstration, it cost $60 to make. :(", (0, 0)))