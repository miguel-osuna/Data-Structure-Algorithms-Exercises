class Queue2:
    """ Front -> Rear implementation"""

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
