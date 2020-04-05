from stack import Stack


def check_sequence(string):
    # Define stack
    stack = Stack()
    balanced = True
    index = 0

    # Helper nested function to check index
    def matches(open, close):
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)

    while index < len(string) and balanced:
        symbol = string[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and stack.isEmpty():
        return True

    else:
        return False


def main():
    print(check_sequence("{({([][])}())}"))
    print(check_sequence("[{()]"))


if __name__ == "__main__":
    main()
