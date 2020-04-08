from binary_heap_max import BinaryHeapMax


class PriorityQueue:
    """
    Front -> Rear implementation 
    Maintains the highest priority items on the front
    """

    def __init__(self):
        self.heapItems = BinaryHeapMax()

    def __str__(self):
        return str(self.heapItems)

    def is_empty(self):
        """ Checks if the queue is empty """
        return self.heapItems.is_empty()

    def enqueue(self, item):
        """ Adds item to the queue """
        self.heapItems.insert(item)

    def dequeue(self):
        """ Removes highest priority item from the queue """
        return self.heapItems.del_max()

    def size(self):
        """ Returns size of the queue list """
        return len(self.heapItems)

    def build_heap(self, a_list):
        self.heapItems.build_heap(a_list)


def main():
    import random

    tasks = PriorityQueue()

    for _ in range(10):
        tasks.enqueue(random.randint(0, 100))

    print("Priority Queue's size: {}".format(tasks.size()))
    print("Priority Queue's content is: {}\n".format(tasks))

    for _ in range(tasks.size()):
        print("Item removed: {}".format(tasks.dequeue()))
        print("Priority Queue's content: {}".format(tasks))


if __name__ == "__main__":
    main()
