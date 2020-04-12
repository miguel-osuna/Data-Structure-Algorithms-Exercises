# Standard library imports
from random import randrange

# Local application imports
from queue1 import Queue1


def hot_potato(namelist, num):
    """ Hot potato simulation"""

    # Populate the queue
    simqueue = Queue1()
    for name in namelist:
        simqueue.enqueue(name)

    # Check there's always at least 1 person
    while simqueue.size() > 1:
        rand_num = randrange(1, num + 1)
        for _ in range(rand_num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


def main():
    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    print(hot_potato(names, 7))
    print(hot_potato(names, 7))
    print(hot_potato(names, 7))
    print(hot_potato(names, 7))
    print(hot_potato(names, 7))


if __name__ == "__main__":
    main()
