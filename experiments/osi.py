import pmma
import time

pmma.init()

tf = pmma.TimeFormatter()
tf.set_from_microsecond(1000082375028570)
print(tf.get_in_sentence_format())

print("Done")

pmma.quit()