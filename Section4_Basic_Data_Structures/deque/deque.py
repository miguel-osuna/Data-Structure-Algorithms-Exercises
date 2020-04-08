class Deque:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    deque = Deque()
    deque.add_front("Dog")
    print(deque)
    deque.add_rear(True)
    print(deque)
    deque.add_front(23)
    print(deque)
    print(deque.size())


if __name__ == "__main__":
    main()
