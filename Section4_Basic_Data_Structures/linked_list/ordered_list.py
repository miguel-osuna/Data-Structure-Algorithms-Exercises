class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnode):
        self.next = newnode


class OrderedList:
    def __init__(self):
        self.head = None
        self.nodes = 0

    def __str__(self):
        current = self.head
        ol = str(self.head)
        while current != None:
            ol += "->" + str(current.getNext())
            current = current.getNext()
        return ol

    # Adds new new node to the ordered list: O(n)
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)

        if previous == None:
            temp.setNext(current)
            self.head = temp

        else:
            temp.setNext(current)
            previous.setNext(temp)

        self.nodes += 1

    # Removes node from the ordered list: O(n)
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        # Looks for item in the node's data
        while not found:
            # If item is found
            if current.getData() == item:
                found = True

            # Else keep searching through the ordered list
            else:
                previous = current
                current = current.getNext()

        # Item was found in the first node
        if previous == None:
            self.head = current.getNext()

        # Set pervious next node to current next node
        else:
            previous.setNext(current.getNext())

    # Checks for a value in the ordered list: O(n)
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    # Returns number of nodes in the ordered list: O(n)
    def size(self):
        return self.nodes

    # Returns index located in ordered list index: O(n)
    def index(self, item):
        current = self.head
        index = 0

        while current.getData() != item:
            index += 1
            current = current.getNext()

        return index

    # Removes node located in the index. By default is the last one: O(n)
    def pop(self, index):
        current = self.head
        previous = None
        node = 0
        same = False

        while not same:
            if node == index:
                same = True
            else:
                nodes += 1
                previous = current
                current = current.getNext()

        if node == index:
            previous.setNext(current.getNext())
            return current.getData()

        elif current == None:
            temp = previous.getData()
            previous = None
            return temp.getData()

    # Checks if ordered list is empty: O(1)
    def isEmpty(self):
        return self.head == None

    # Reverse the ordered list: O(n)
    def reverse(self):
        pass


if __name__ == "__main__":
    ol = OrderedList()

    ol.add(31)
    ol.add(77)
    ol.add(17)
    ol.add(93)
    ol.add(26)
    ol.add(54)

    print(ol)
