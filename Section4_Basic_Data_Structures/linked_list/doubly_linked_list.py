class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node

    def set_previous(self, node):
        self.previous = node


class DoublyLinkedList:
    def __init__(self):
        self.front = None
        self.end = None
        self.nodes = 0

    def __str__(self):
        dllstr = ""
        current = self.front
        while current != None:
            dllstr += "<=>" + str(current)
            current = current.get_next()
        dllstr += "<=>"
        return dllstr

    def get_node_with_index(self, index):
        """Gets node that matches the index"""
        current = self.front
        found = False
        num_node = 0

        while num_node != index and current != None:
            num_node += 1
            current = current.get_next()

        return current

    def get_node_with_item(self, item):
        """Gets node that matches the item"""
        current = self.front
        found = False

        while not found and current != None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return current

    def get_index(self, item):
        """Gets node's index"""
        current = self.front
        index = 0
        while current.get_data() != item:
            index += 1
            current = current.get_next()
        return index

    def add_after(self, item, new_item):
        """Adds new node after some node in the linked list"""
        # Create nodes
        temp = Node(new_item)
        current = self.get_node_with_item(item)

        # if current == None:
        #     self.add_fronts(new_item)

        # If current.next is None, then set End to temp
        if current.get_next() == None:
            temp.set_previous(current)
            self.end = temp
            temp.get_previous().set_next(temp)

        # Else insert temp between current and current.next
        else:
            temp.set_next(current.get_next())
            temp.get_next().set_previous(temp)
            temp.set_previous(current)
            temp.get_previous().set_next(temp)

        # Increment nodes in the list
        self.nodes += 1

    def add_before(self, item, new_item):
        """Adds new node before some node in the linked list"""
        # Create nodes
        temp = Node(new_item)
        current = self.get_node_with_item(item)

        # if current == None:
        #     self.add_end(new_item)

        # If current.previous is None, the set Front to temp
        if current.get_previous() == None:
            temp.set_next(current)
            self.front = temp
            temp.get_next().set_previous(temp)

        # Else insert temp between current and current.previous
        else:
            current.get_previous().set_next(temp)
            temp.set_previous(current.get_previous())
            current.set_previous(temp)
            temp.set_next(current)

        # Increment nodes in the list
        self.nodes += 1

    def add_fronts(self, item):
        """Adds new node to the front of the linked list"""

        # Sets Front and End if there's no Front Node
        if self.front == None:
            temp = Node(item)
            self.front = temp
            self.end = temp

        # Moves the front node to the right
        else:
            self.add_before(self.front.get_data(), item)

        # Increment nodes in the list
        self.nodes += 1

    def add_end(self, item):
        """Adds new node to the end of the linked list"""

        # Sets End and Front if there's no End Node
        if self.end == None:
            temp = Node(item)
            self.end = temp
            self.front = temp

            # Increment nodes in the list
            self.nodes += 1

        # Moves the end node to the left
        else:
            self.add_after(self.end.get_data(), item)

    def remove(self, item):
        """Removes node from the linked list"""
        # Look for the node
        current = self.get_node_with_item(item)

        # If previous is None, the Front is the
        if current.get_previous() == None:
            self.front = current.get_next()
        else:
            current.get_previous().set_next(current.get_next())

        if current.get_next() == None:
            self.end = current.get_previous()
        else:
            current.get_next().set_previous(current.get_previous())

        # Decrement nodes in the list
        self.nodes -= 1

    def size(self):
        """Returns the number of nodes in the linked list"""
        return self.nodes

    def is_empty(self):
        """Checks if the linked list is empty"""
        return self.front == None and self.end == None


def main():
    dll = DoublyLinkedList()
    print(dll.size())

    dll.add_fronts(1)
    print(dll.size())

    dll.add_end(2)
    print(dll.size())

    dll.add_after(1, "After front")
    print(dll.size())

    dll.add_before(2, "Before end")
    print(dll.size())

    print(dll.is_empty())
    print(dll)

    dll2 = DoublyLinkedList()
    print(dll2)
    dll2.add_end("Testing")
    print(dll2)


if __name__ == "__main__":
    main()
