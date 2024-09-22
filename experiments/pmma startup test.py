import pprofile

p = pprofile.Profile()
p.enable()

import pmma

pmma.init()

p.disable()

p.dump_stats(r"H:\Downloads\pmma boot up profile.txt")