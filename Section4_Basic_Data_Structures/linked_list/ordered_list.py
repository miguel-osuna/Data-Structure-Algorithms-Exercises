class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnode):
        self.next = newnode


class OrderedList:
    def __init__(self):
        self.head = None
        self.nodes = 0

    def __str__(self):
        current = self.head
        ol = str(self.head)
        while current != None:
            ol += "->" + str(current.get_next())
            current = current.get_next()
        return ol

    # Adds new new node to the ordered list: O(n)
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)

        if previous == None:
            temp.set_next(current)
            self.head = temp

        else:
            temp.set_next(current)
            previous.set_next(temp)

        self.nodes += 1

    # Removes node from the ordered list: O(n)
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        # Looks for item in the node's data
        while not found:
            # If item is found
            if current.get_data() == item:
                found = True

            # Else keep searching through the ordered list
            else:
                previous = current
                current = current.get_next()

        # Item was found in the first node
        if previous == None:
            self.head = current.get_next()

        # Set pervious next node to current next node
        else:
            previous.set_next(current.get_next())

    # Checks for a value in the ordered list: O(n)
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    # Returns number of nodes in the ordered list: O(n)
    def size(self):
        return self.nodes

    # Returns index located in ordered list index: O(n)
    def index(self, item):
        current = self.head
        index = 0

        while current.get_data() != item:
            index += 1
            current = current.get_next()

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
                current = current.get_next()

        if node == index:
            previous.set_next(current.get_next())
            return current.get_data()

        elif current == None:
            temp = previous.get_data()
            previous = None
            return temp.get_data()

    # Checks if ordered list is empty: O(1)
    def is_empty(self):
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
