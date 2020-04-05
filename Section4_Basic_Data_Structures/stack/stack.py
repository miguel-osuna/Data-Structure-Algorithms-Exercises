class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    astack = Stack()
    print("Stack is empty? {}".format(astack.isEmpty()))
    astack.push(1)
    astack.push("dog")
    astack.push(True)
    print("Stack is empty? {}".format(astack.isEmpty()))
    print("Last value is: {}".format(astack.peek()))
    print("Stack size is: {}".format(astack.size()))
    print("Stack items are: {}".format(astack))
