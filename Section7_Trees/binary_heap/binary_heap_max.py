class BinaryHeapMax():
    ''' Binary Heap maximum order implementation '''

    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def __str__(self):
        return str(self.heaplist)

    def percUp(self, i):
        ''' Percolate (filtrate) value in index i to proper position '''
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                temp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = temp
            i //= 2

    def insert(self, i):
        ''' Insert a value into the binary heap '''
        self.heaplist.append(i)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def findMaxChild(self, i):
        ''' Finds the index of the maximum child '''
        if i * 2 + 1 > self.currentSize:
            return i
        else:
            if self.heaplist[i * 2] > self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        ''' Percolate (filtrate) value in index i to proper position '''
        while (i * 2) <= self.currentSize:
            maxchild = self.findMaxChild(i)

            # If parent node is smaller than maximum child, change them
            if self.heaplist[i] < self.heaplist[maxchild]:
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[maxchild]
                self.heaplist[maxchild] = temp

            # Moves root index to child node
            i = maxchild

    def delMax(self):
        ''' Deletes maximum value of the binary heap '''
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        ''' Checks if binary heap is empty '''
        if len(self.heaplist) > 1:
            return False
        else:
            return True

    def size(self):
        ''' Returns size of the binary heap '''
        return self.currentSize

    def buildHeap(self, alist):
        ''' Builds a binary heap with a list '''
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]

        while i > 0:
            self.percDown(i)
            i -= 1


if __name__ == "__main__":
    import random
    numlist = [random.randint(0, 100) for i in range(100)]
    binaryheap = BinaryHeapMax()
