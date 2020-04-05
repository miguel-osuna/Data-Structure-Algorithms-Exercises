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


class UnorderedList:
    def __init__(self):
        self.head = None
        self.nodes = 0

    def __str__(self):
        current = self.head
        ul = str(self.head)
        while current != None:
            ul += "->" + str(current.getNext())
            current = current.getNext()
        return ul

    # Slice method for unordered list
    def __getitem__(self, start, end, step):
        pass

    # Adds new new node to the unordered list: O(1)
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.nodes += 1

    # Checks for a value in the unordered list: O(n)
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    # Returns number of nodes in the unordered list: O(n)
    def size(self):
        return self.nodes

    # Removes node from the unordered listk: O(n)
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        # Looks for item in the node's data
        while not found:
            # If item is found
            if current.getData() == item:
                found = True

            # Else keep searching through the unordered list
            else:
                previous = current
                current = current.getNext()

        # Item was found in the first node
        if previous == None:
            self.head = current.getNext()

        # Set pervious next node to current next node
        else:
            previous.setNext(current.getNext())

    # Append node to the end of the unordered list: O(n)
    def append(self, item):
        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = Node(item)
        else:
            previous.setNext(Node(item))

    # Insert node into the unordered list index: O(n)
    def insert(self, index, item):
        current = self.head
        previous = None
        temp = Node(item)
        node = 0

        while node != index and current != None:
            node += 1
            previous = current
            current = current.getNext()

        if previous == None:
            temp.setNext(current)
            self.head = temp

        else:
            temp.setNext(current)
            previous.setNext(temp)

    # Returns index located in unordered list: O(n)
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
                node += 1
                previous = current
                current = current.getNext()

        if node == index:
            previous.setNext(current.getNext())
            return current.getData()

        elif current == None:
            temp = previous.getData()
            previous = None
            return temp.getData()

    # Checks if unordered list is empty: O(1)
    def isEmpty(self):
        return self.head == None

    # Reverse the unordered list: O(n)
    def reverse(self):
        pass


def main():
    linkedlist = UnorderedList()
    linkedlist.insert(0, 0)
    linkedlist.insert(1, 1)
    linkedlist.insert(2, 2)

    print(linkedlist)


if __name__ == "__main__":
    main()
