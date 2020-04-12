""" Testing list data structure methods """

# Standard library imports
import timeit


def test1(n):
    """ Generates list using concat """
    l = []
    for num in range(n):
        l = l + [num]
    return l


def test2(n):
    """ Generates list using append method """
    l = []
    for num in range(n):
        l.append(num)
    return l


def test3(n):
    """ Generates list using comprehension """
    l = [num for num in range(n)]
    return l


def test4(n):
    """ Generates list using list typing range """
    l = list(range(n))
    return l


def test_list_creation():
    """ Timer(timed statement, setup statement, timer function)"""
    t1 = timeit.Timer("test1(1000)", "from __main__ import test1")
    print("concat", t1.timeit(number=1000), "milliseconds")

    t2 = timeit.Timer("test2(1000)", "from __main__ import test2")
    print("append", t2.timeit(number=1000), "milliseconds")

    t3 = timeit.Timer("test3(1000)", "from __main__ import test3")
    print("comprehension", t3.timeit(number=1000), "milliseconds")

    t4 = timeit.Timer("test4(1000)", "from __main__ import test4")
    print("list range", t4.timeit(number=1000), "milliseconds")


def test_push():
    """pop() is a O(1)
    # pop(i) is a O(n)"""
    popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
    popend = timeit.Timer("x.pop()", "from __main__ import x")
    print("pop(0)   pop()")

    for i in range(1000000, 100000001, 1000000):
        x = list(range(i))
        pt = popend.timeit(number=1000)
        x = list(range(i))
        pz = popzero.timeit(number=1000)
        print("%15.5f, %15.5f" % (pz, pt))


if __name__ == "__main__":
    pass
