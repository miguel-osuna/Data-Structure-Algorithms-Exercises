from queue import Queue


def hot_potato(namelist, num):
    # Populate the queue
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    # Check there's always at least 1 person
    while simqueue.size() > 1:
        for _ in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


if __name__ == "__main__":
    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    print(hot_potato(names, 7))
