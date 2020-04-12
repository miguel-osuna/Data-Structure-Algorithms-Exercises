# Standard library imports
import sys

# Local application imports
sys.path.insert(0, "Section6_Sorting_Searching/sorting")
from quick_sort import quick_sort


class BinaryHeapMin:
    """ Binary Heap minimum order implementation """

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def __str__(self):
        return str(self.heap_list)

    def __len__(self):
        return self.current_size

    def perc_up(self, i):
        """ Percolate (filtrate) value in index i to proper position """
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i //= 2

    def insert(self, value):
        """ Insert a value into the binary heap """
        self.heap_list.append(value)
        self.current_size += 1
        self.perc_up(self.current_size)

    def find_min_child(self, i):
        """ Finds the index of the minimum child """
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        """ Percolate (filtrate) value in index i to proper position """
        while (i * 2) <= self.current_size:
            min_child = self.find_min_child(i)

            # If parent node is bigger than minimum child node, change them
            if self.heap_list[i] > self.heap_list[min_child]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child]
                self.heap_list[min_child] = temp

            # Moves root index to child node
            i = min_child

    def del_min(self):
        """ Deletes minimum value of the binary heap """
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def is_empty(self):
        """ Checks if binary heap is empty """
        if len(self.heap_list) > 1:
            return False
        else:
            return True

    def size(self):
        """ Returns size of the binary heap """
        return self.current_size

    def build_heap(self, l):
        """ Builds a binary heap with a list """
        num_list = l
        quick_sort(num_list)

        i = len(num_list) // 2
        self.current_size = len(num_list)
        self.heap_list = [0] + num_list[:]

        # Starts from the middle of the tree and goes it's way up
        while i > 0:
            self.perc_down(i)
            i -= 1


def main():
    import random

    # Using insert method
    num_list = [random.randint(0, 100) for i in range(20)]
    binary_heap = BinaryHeapMin()

    print("Using insert class method")
    for num in num_list:
        binary_heap.insert(num)
        print("Adding {}: {}".format(num, binary_heap))

    # Using build_heap method
    num_list2 = [random.randint(0, 100) for i in range(10)]
    print("\nUsing build_heap class method")
    print("Initial number list: {}".format(str(num_list2)))

    bh = BinaryHeapMin()
    bh.build_heap(num_list2)
    print(bh)


if __name__ == "__main__":
    main()
