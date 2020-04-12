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


class UnorderedList:
    def __init__(self):
        self.head = None
        self.nodes = 0

    def __str__(self):
        current = self.head
        ul = str(self.head)
        while current != None:
            ul += "->" + str(current.get_next())
            current = current.get_next()
        return ul

    def __getitem__(self, start, end, step):
        """Slice method for unordered list"""
        pass

    def add(self, item):
        """Adds new new node to the unordered list: O(1)"""
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.nodes += 1

    def search(self, item):
        """Checks for a value in the unordered list: O(n)"""
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def size(self):
        """Returns number of nodes in the unordered list: O(n)"""
        return self.nodes

    def remove(self, item):
        """Removes node from the unordered listk: O(n)"""
        current = self.head
        previous = None
        found = False

        # Looks for item in the node's data
        while not found:
            # If item is found
            if current.get_data() == item:
                found = True

            # Else keep searching through the unordered list
            else:
                previous = current
                current = current.get_next()

        # Item was found in the first node
        if previous == None:
            self.head = current.get_next()

        # Set pervious next node to current next node
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        """Append node to the end of the unordered list: O(n)"""
        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.get_next()

        if previous == None:
            self.head = Node(item)
        else:
            previous.set_next(Node(item))

    def insert(self, index, item):
        """Insert node into the unordered list index: O(n)"""
        current = self.head
        previous = None
        temp = Node(item)
        node = 0

        while node != index and current != None:
            node += 1
            previous = current
            current = current.get_next()

        if previous == None:
            temp.set_next(current)
            self.head = temp

        else:
            temp.set_next(current)
            previous.set_next(temp)

    def index(self, item):
        """Returns index located in unordered list: O(n)"""
        current = self.head
        index = 0

        while current.get_data() != item:
            index += 1
            current = current.get_next()

        return index

    def pop(self, index):
        """Removes node located in the index. By default is the last one: O(n)"""
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
                current = current.get_next()

        if node == index:
            previous.set_next(current.get_next())
            return current.get_data()

        elif current == None:
            temp = previous.get_data()
            previous = None
            return temp.get_data()

    def is_empty(self):
        """Checks if unordered list is empty: O(1)"""
        return self.head == None

    def reverse(self):
        """Reverse the unordered list: O(n)"""
        pass


def main():
    linkedlist = UnorderedList()
    linkedlist.insert(0, 0)
    linkedlist.insert(1, 1)
    linkedlist.insert(2, 2)

    print(linkedlist)


if __name__ == "__main__":
    main()
