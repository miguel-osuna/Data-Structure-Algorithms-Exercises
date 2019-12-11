import timeit
import random

print("Size", "List time", "Dictionary time")
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" %
                     i, "from __main__ import random, x")

    # List duration
    x = list(range(i))
    list_time = t.timeit(number=1000)

    # Dictionary duration
    x = {j: None for j in range(i)}
    dictionary_time = t.timeit(number=1000)

    print("%d, %10.3f, %10.3f" % (i, list_time, dictionary_time))
