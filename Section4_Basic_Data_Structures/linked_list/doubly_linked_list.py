class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node

    def setPrevious(self, node):
        self.previous = node


class DoublyLinkedList():
    def __init__(self):
        self.front = None
        self.end = None
        self.nodes = 0

    def __str__(self):
        dllstr = ""
        current = self.front
        while current != None:
            dllstr += "<=>" + str(current)
            current = current.getNext()
        dllstr += "<=>"
        return dllstr

    # Gets node that matches the index
    def getNodeWithIndex(self, index):
        current = self.front
        found = False
        num_node = 0

        while num_node != index and current != None:
            num_node += 1
            current = current.getNext()

        return current

    # Gets node that matches the item
    def getNodeWithItem(self, item):
        current = self.front
        found = False

        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return current

    # Gets node's index
    def getIndex(self, item):
        current = self.front
        index = 0
        while current.getData() != item:
            index += 1
            current = current.getNext()
        return index

    # Adds new node after some node in the linked list
    def addAfter(self, item, new_item):
        # Create nodes
        temp = Node(new_item)
        current = self.getNodeWithItem(item)

        # if current == None:
        #     self.AddFront(new_item)

        # If current.next is None, then set End to temp
        if current.getNext() == None:
            temp.setPrevious(current)
            self.end = temp
            temp.getPrevious().setNext(temp)

        # Else insert temp between current and current.next
        else:
            temp.setNext(current.getNext())
            temp.getNext().setPrevious(temp)
            temp.setPrevious(current)
            temp.getPrevious().setNext(temp)

        # Increment nodes in the list
        self.nodes += 1

    # Adds new node before some node in the linked list
    def addBefore(self, item, new_item):
        # Create nodes
        temp = Node(new_item)
        current = self.getNodeWithItem(item)

        # if current == None:
        #     self.addEnd(new_item)

        # If current.previous is None, the set Front to temp
        if current.getPrevious() == None:
            temp.setNext(current)
            self.front = temp
            temp.getNext().setPrevious(temp)

        # Else insert temp between current and current.previous
        else:
            current.getPrevious().setNext(temp)
            temp.setPrevious(current.getPrevious())
            current.setPrevious(temp)
            temp.setNext(current)

        # Increment nodes in the list
        self.nodes += 1

    # Adds new node to the front of the linked list
    def addFront(self, item):

        # Sets Front and End if there's no Front Node
        if self.front == None:
            temp = Node(item)
            self.front = temp
            self.end = temp

        # Moves the front node to the right
        else:
            self.addBefore(self.front.getData(), item)

        # Increment nodes in the list
        self.nodes += 1

    # Adds new node to the end of the linked list
    def addEnd(self, item):

        # Sets End and Front if there's no End Node
        if self.end == None:
            temp = Node(item)
            self.end = temp
            self.front = temp

            # Increment nodes in the list
            self.nodes += 1

        # Moves the end node to the left
        else:
            self.addAfter(self.end.getData(), item)

    # Removes node from the linked list
    def remove(self, item):
        # Look for the node
        current = self.getNodeWithItem(item)

        # If previous is None, the Front is the
        if current.getPrevious() == None:
            self.front = current.getNext()
        else:
            current.getPrevious().setNext(current.getNext())

        if current.getNext() == None:
            self.end = current.getPrevious()
        else:
            current.getNext().setPrevious(current.getPrevious())

        # Decrement nodes in the list
        self.nodes -= 1

    # Returns the number of nodes in the linked list
    def size(self):
        return self.nodes

    # Checks if the linked list is empty
    def isEmpty(self):
        return self.front == None and self.end == None


if __name__ == "__main__":
    dll = DoublyLinkedList()
    print(dll.size())

    dll.addFront(1)
    print(dll.size())

    dll.addEnd(2)
    print(dll.size())

    dll.addAfter(1, "After front")
    print(dll.size())

    dll.addBefore(2, "Before end")
    print(dll.size())

    print(dll.isEmpty())
    print(dll)

    dll2 = DoublyLinkedList()
    print(dll2)
    dll2.addEnd("Testing")
    print(dll2)
