class BinaryHeapMin():
    ''' Binary Heap minimum order implementation '''

    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def __str__(self):
        return str(self.heaplist)

    def percUp(self, i):
        ''' Percolate (filtrate) value in index i to proper position '''
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                temp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = temp
            i //= 2

    def insert(self, i):
        ''' Insert a value into the binary heap '''
        self.heaplist.append(i)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def findMinChild(self, i):
        ''' Finds the index of the minimum child '''
        if i * 2 + 1 > self.currentSize:
            return i
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        ''' Percolate (filtrate) value in index i to proper position '''
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
        ''' Deletes minimum value of the binary heap '''
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
    bhm = BinaryHeapMin()
    numlist = [9, 5, 6, 2, 3]

    print(bhm.size())
    print(bhm.isEmpty())
    bhm.buildHeap(numlist)

    print(bhm.size())
    print(bhm.isEmpty())
    print(bhm)

    bhm.insert(1)
    print(bhm)

    bhm.delMin()
    print(bhm)
