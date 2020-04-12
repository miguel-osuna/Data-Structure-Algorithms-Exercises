class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def main():
    a_stack = Stack()
    print("Stack is empty? {}".format(a_stack.is_empty()))
    a_stack.push(1)
    a_stack.push("dog")
    a_stack.push(True)
    print("Stack is empty? {}".format(a_stack.is_empty()))
    print("Last value is: {}".format(a_stack.peek()))
    print("Stack size is: {}".format(a_stack.size()))
    print("Stack items are: {}".format(a_stack))


if __name__ == "__main__":
    main()
