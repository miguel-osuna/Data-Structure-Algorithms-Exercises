class BinaryHeapMax:
    """ Binary Heap maximum order implementation """

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
            if self.heap_list[i] > self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i //= 2

    def insert(self, value):
        """ Insert a value into the binary heap """
        self.heap_list.append(value)
        self.current_size += 1
        self.perc_up(self.current_size)

    def find_max_child(self, i):
        """ Finds the index of the maximum child """
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        """ Percolate (filtrate) value in index i to proper position """
        while (i * 2) <= self.current_size:
            maxchild = self.find_max_child(i)

            # If parent node is smaller than maximum child, change them
            if self.heap_list[i] < self.heap_list[maxchild]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[maxchild]
                self.heap_list[maxchild] = temp

            # Moves root index to child node
            i = maxchild

    def del_max(self):
        """ Deletes maximum value of the binary heap """
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

    def build_heap(self, a_list):
        """ Builds a binary heap with a list """
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]

        while i > 0:
            self.perc_down(i)
            i -= 1


def main():
    import random

    numlist = [random.randint(0, 100) for i in range(100)]
    binary_heap = BinaryHeapMax()
    binary_heap.build_heap(numlist)
    print(binary_heap)


if __name__ == "__main__":
    main()
