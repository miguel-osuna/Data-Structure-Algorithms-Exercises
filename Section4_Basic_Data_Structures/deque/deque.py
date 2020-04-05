class Deque:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    deque = Deque()
    deque.addFront("Dog")
    print(deque)
    deque.addRear(True)
    print(deque)
    deque.addFront(23)
    print(deque)
    print(deque.size())


if __name__ == "__main__":
    main()
