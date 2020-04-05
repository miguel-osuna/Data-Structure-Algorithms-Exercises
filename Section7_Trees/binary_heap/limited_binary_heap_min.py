from binary_heap_min import BinaryHeapMin


class LimitedBinaryHeapMin(BinaryHeapMin):
    def __init__(self, sizeLimit):
        super().__init__()
        self.sizeLimit = sizeLimit

    def insert(self, i):
        """ Insert a value into the binary heap """

        # Size of binary heap is under it's limit
        if self.currentSize < self.sizeLimit:
            super().insert(i)

        # Maintain binary heap size under it's limit
        else:
            super().insert(i)
            self.currentSize -= 1
            self.heaplist.pop()


if __name__ == "__main__":
    import random

    binary_heap = LimitedBinaryHeapMin(10)
    numlist = [random.randint(0, 100) for _ in range(10)]
    numlist2 = [random.randint(0, 10) for _ in range(5)]

    print("Adding first items")
    for num in numlist:
        binary_heap.insert(num)
        print(num, binary_heap)

    print("\nAdding new items")
    for num in numlist2:
        binary_heap.insert(num)
        print(num, binary_heap)
