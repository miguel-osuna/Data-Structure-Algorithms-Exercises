# Local application imports
from binary_heap_min import BinaryHeapMin


class LimitedBinaryHeapMin(BinaryHeapMin):
    """ Limited Binary Heap Minimum implementation """

    def __init__(self, size_limit):
        super().__init__()
        self.size_limit = size_limit
        self.current_size = 0

    def insert(self, i):
        """ Insert a value into the binary heap """

        # Size of binary heap is under it's limit
        if self.current_size < self.size_limit:
            super().insert(i)

        # Maintain binary heap size under it's limit
        else:
            super().insert(i)
            self.current_size -= 1
            self.heap_list.pop()


def main():
    import random

    binary_heap = LimitedBinaryHeapMin(10)
    num_list = [random.randint(0, 100) for _ in range(10)]
    num_list2 = [random.randint(0, 10) for _ in range(5)]

    print("Adding first items")
    for num in num_list:
        binary_heap.insert(num)
        print(num, binary_heap)

    print("\nAdding new items")
    for num in num_list2:
        binary_heap.insert(num)
        print(num, binary_heap)


if __name__ == "__main__":
    main()
