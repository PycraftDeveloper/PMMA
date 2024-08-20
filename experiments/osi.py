import pmma
import time

pmma.init()

tf = pmma.TimeFormatter()
tf.set_from_year(1)
print(tf.year, tf.month, tf.day, tf.hour, tf.minute, tf.second, tf.microsecond)
print(tf.get_in_sentence_format())

print("Done")

pmma.quit()