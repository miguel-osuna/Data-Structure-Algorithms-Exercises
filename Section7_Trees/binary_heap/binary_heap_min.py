import sys

sys.path.insert(0, "Section6_Sorting_Searching/sorting")
from quick_sort import quickSort


class BinaryHeapMin:
    """ Binary Heap minimum order implementation """

    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def __str__(self):
        return str(self.heaplist)

    def __len__(self):
        return self.currentSize

    def percUp(self, i):
        """ Percolate (filtrate) value in index i to proper position """
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                temp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = temp
            i //= 2

    def insert(self, value):
        """ Insert a value into the binary heap """
        self.heaplist.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def findMinChild(self, i):
        """ Finds the index of the minimum child """
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        """ Percolate (filtrate) value in index i to proper position """
        while (i * 2) <= self.currentSize:
            minchild = self.findMinChild(i)

            # If parent node is bigger than minimum child node, change them
            if self.heaplist[i] > self.heaplist[minchild]:
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[minchild]
                self.heaplist[minchild] = temp

            # Moves root index to child node
            i = minchild

    def delMin(self):
        """ Deletes minimum value of the binary heap """
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        """ Checks if binary heap is empty """
        if len(self.heaplist) > 1:
            return False
        else:
            return True

    def size(self):
        """ Returns size of the binary heap """
        return self.currentSize

    def buildHeap(self, l):
        """ Builds a binary heap with a list """
        numlist = l
        quickSort(numlist)

        i = len(numlist) // 2
        self.currentSize = len(numlist)
        self.heaplist = [0] + numlist[:]

        # Starts from the middle of the tree and goes it's way up
        while i > 0:
            self.percDown(i)
            i -= 1


def main():
    import random

    # Using insert method
    numlist = [random.randint(0, 100) for i in range(20)]
    binaryheap = BinaryHeapMin()

    print("Using insert class method")
    for num in numlist:
        binaryheap.insert(num)
        print("Adding {}: {}".format(num, binaryheap))

    # Using buildHeap method
    numlist2 = [random.randint(0, 100) for i in range(10)]
    print("\nUsing buildHeap class method")
    print("Initial number list: {}".format(str(numlist2)))

    bh = BinaryHeapMin()
    bh.buildHeap(numlist2)
    print(bh)


if __name__ == "__main__":
    main()
